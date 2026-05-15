#!/usr/bin/env python3
"""
PRJ-020: Intern Application Data Migration Script
==================================================
Injects 92 intern applicants from consolidated JSON into popdb.

⚠️ CRITICAL: n8n automation was SKIPPED for speed to delivery.
   If this workflow is reused for future cohorts, n8n automation
   MUST be built.

⚠️ NO CONTACT/INTERVIEW DATA:
   All contact/interview fields are NULL.
   pipeline_status = 'EVALUATED' for all candidates.
   Manual data entry required after receiving info from Stef.

Usage:
    .venv/bin/python3 migrate-prj020.py

Requirements:
    pip install psycopg2-binary

Author: @RMN (Roman Di Domizio) + AI:@RMN (Surge) + AI:Windsurf (Cascade)
Date: 2026-04-06
CCC-ID: RMN_2026-W15_1004
"""

import json
import sys
import os
import getpass
import psycopg2
from psycopg2 import sql, extras
from psycopg2.extras import Json
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple

# =====================================================
# CONFIGURATION
# =====================================================

JSON_FILE = "/Users/romandidomizio/WeOwn/n8n-recovery/eval-results/intern_eval_comprehensive_2026-03-18.json"

# Connection config — password loaded from environment variable
DB_CONNECTION = {
    "host": "db-postgresql-atl1-weownnet-do-user-24194004-0.i.db.ondigitalocean.com",
    "port": 25060,
    "database": "popdb",
    "user": "pop_write",
    "password": None,  # Set at runtime via env var or getpass prompt
    "sslmode": "require",
    "sslrootcert": os.path.expanduser("~/.postgresql/ca-certificate.crt")
}

# Evaluation timestamp (proxy for submitted_at — actual form timestamps not in data)
EVAL_TIMESTAMP = "2026-03-18T03:36:16.103Z"
FORM_ID = "8"  # All from Fluent Form 8
DATA_SOURCE = "Fluent Forms"

# =====================================================
# HELPER FUNCTIONS
# =====================================================

def split_name(full_name: str) -> Tuple[str, str]:
    """
    Split full name into first_name and last_name.
    First token = first_name, remaining tokens = last_name.
    Preserves original case.
    """
    if not full_name or not isinstance(full_name, str):
        return ("Unknown", "Unknown")
    
    parts = full_name.strip().split()
    if len(parts) == 0:
        return ("Unknown", "Unknown")
    elif len(parts) == 1:
        return (parts[0], "Unknown")
    else:
        return (parts[0], " ".join(parts[1:]))

def parse_iso_timestamp(iso_string: str) -> str:
    """Convert ISO timestamp to PostgreSQL format."""
    if not iso_string:
        return datetime.now().isoformat()
    iso_string = iso_string.replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(iso_string)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def compute_global_rank(category: str, category_rank: int) -> int:
    """
    Compute global rank across all 92 candidates.
    Order: ADVANCE (1-11) → MAYBE (12-39) → PASS (40-68) → DQ (69-92)
    """
    if category == "ADVANCE":
        return category_rank
    elif category == "MAYBE":
        return 11 + category_rank
    elif category == "PASS":
        return 11 + 28 + category_rank
    elif category == "AUTO-DISQUALIFIED":
        return 11 + 28 + 29 + category_rank
    else:
        return 92

def is_hour_valid(hours: Any) -> Optional[int]:
    """Validate hours_per_week is 10, 20, or 40."""
    if hours is None:
        return None
    try:
        hours_int = int(hours)
        if hours_int in [10, 20, 40]:
            return hours_int
        return None
    except:
        return None

def extract_array(json_obj: Dict, key: str) -> List[str]:
    """Safely extract array from JSON."""
    val = json_obj.get(key, [])
    if val is None:
        return []
    if isinstance(val, list):
        return [str(v) for v in val if v]
    return []

def verify_schema(conn) -> bool:
    """Verify all 5 new columns exist before migration."""
    required_columns = [
        'college_major', 'graduation_date', 'resume_pages', 
        'track_fit', 'status_reason'
    ]
    
    with conn.cursor() as cur:
        cur.execute("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = 'applications' 
              AND column_name = ANY(%s)
            ORDER BY column_name
        """, (required_columns,))
        
        found = [row[0] for row in cur.fetchall()]
    
    if len(found) == len(required_columns):
        print(f"✅ Schema verified: All {len(required_columns)} new columns exist")
        return True
    else:
        missing = set(required_columns) - set(found)
        print(f"❌ Schema verification FAILED: Missing columns: {missing}")
        print("   Run ALTER TABLE statements before migration.")
        return False

def check_existing_data(conn) -> bool:
    """Check if data already exists — warn if so."""
    with conn.cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM applicants")
        count = cur.fetchone()[0]
    
    if count > 0:
        print(f"⚠️  WARNING: applicants table already has {count} rows.")
        print("   Script uses ON CONFLICT (email) DO UPDATE for idempotency.")
        print("   Existing records will be updated, new ones inserted.")
    return True

# =====================================================
# DATA PROCESSING
# =====================================================

def process_scored_candidate(candidate: Dict, global_rank: int) -> Dict:
    """Process a scored candidate (ADVANCE, MAYBE, PASS)."""
    first_name, last_name = split_name(candidate.get("name", ""))
    
    hours = candidate.get("hours_per_week") or candidate.get("hours")
    hours_valid = is_hour_valid(hours)
    
    work_auth = True
    
    status_reason = None
    if candidate.get("category") == "PASS":
        status_reason = candidate.get("pass_reason")
    
    applicant_data = {
        "email": candidate.get("email", "").lower().strip(),
        "first_name": first_name,
        "last_name": last_name,
        "phone": candidate.get("phone"),
        "location": candidate.get("location"),
        "linkedin": candidate.get("linkedin_url"),
        "github": candidate.get("github_url"),
        "portfolio": candidate.get("website_url"),
        "resume_url": candidate.get("resume_url")
    }
    
    application_data = {
        "form_id": FORM_ID,
        "submitted_at": parse_iso_timestamp(EVAL_TIMESTAMP),
        "hours_per_week": hours_valid,
        "start_timeframe": candidate.get("start_timeframe"),
        "start_date": None,
        "work_authorization": work_auth,
        "track_interest": extract_array(candidate, "track_interest"),
        "track_experience": extract_array(candidate, "track_experience"),
        "skills_matrix": Json(candidate.get("skills_matrix", {})),
        "short_answer_1": candidate.get("short_answer_1", "[NO RESPONSE]"),
        "short_answer_2": candidate.get("short_answer_2", "[NO RESPONSE]"),
        "short_answer_3": candidate.get("short_answer_3"),
        "country": candidate.get("country"),
        "country_mismatch": candidate.get("country_mismatch", False),
        "country_mismatch_detail": None,
        "structured_raw": candidate.get("structured_scores", {}).get("structured_raw"),
        "structured_max": candidate.get("structured_scores", {}).get("structured_max", 56),
        "structured_normalized": candidate.get("structured_normalized"),
        "bonus_military": candidate.get("bonus_military", False),
        "bonus_athlete": candidate.get("bonus_athlete", False),
        "bonus_total": candidate.get("bonus_total", 0),
        "inflation_flag": candidate.get("pass2_sorting", {}).get("flag_inflation", False),
        "strong_count": None,
        "valid_skill_count": candidate.get("structured_scores", {}).get("valid_skill_count"),
        "raw_response": None,
        "data_source": DATA_SOURCE,
        "evaluation_status": "SCORED",
        "final_score": candidate.get("final_score"),
        "recommendation": candidate.get("recommendation") or candidate.get("category"),
        "confidence": candidate.get("confidence"),
        "rank": global_rank,
        "college_major": candidate.get("major"),
        "graduation_date": candidate.get("graduation_date"),
        "resume_pages": candidate.get("resume_pages"),
        "track_fit": candidate.get("track_fit"),
        "status_reason": status_reason,
        "flag_ai_content": candidate.get("ai_content_flag") or candidate.get("pass2_sorting", {}).get("flag_ai_content", "no"),
        "flag_inflation": candidate.get("pass2_sorting", {}).get("flag_inflation", False),
        "flag_country": candidate.get("country_mismatch") or candidate.get("pass2_sorting", {}).get("country_flag", False)
    }
    
    # Evaluation data (3 rows per scored candidate)
    structured_scores = candidate.get("structured_scores", {})
    pass2_scores = candidate.get("pass2_scores", {})
    pass2_sorting = candidate.get("pass2_sorting", {})
    pass2_bonus = candidate.get("pass2_bonus_confirmed", {})
    pass3_meta = candidate.get("pass3_meta", {})
    
    pass2_composite = {
        "scores": pass2_scores,
        "sorting": pass2_sorting,
        "bonus_confirmed": pass2_bonus
    }
    
    evaluations_data = [
        {
            "evaluation_type": "pass1_structured",
            "score": structured_scores.get("structured_raw"),
            "max_score": structured_scores.get("structured_max", 56),
            "normalized_score": candidate.get("structured_normalized"),
            "evaluator": "n8n Workflow (Automated)",
            "evaluation_data": Json(structured_scores),
            "interview_scheduled": False,
            "interview_date": None,
            "interviewers": None,
            "interview_outcome": None,
            "interview_notes": None
        },
        {
            "evaluation_type": "pass2_llm",
            "score": candidate.get("llm_total"),
            "max_score": 100,
            "normalized_score": candidate.get("llm_normalized"),
            "evaluator": "n8n Workflow (AI: Qwen3.5-397B)",
            "evaluation_data": Json(pass2_composite),
            "interview_scheduled": False,
            "interview_date": None,
            "interviewers": None,
            "interview_outcome": None,
            "interview_notes": None
        },
        {
            "evaluation_type": "pass3_meta",
            "score": candidate.get("final_score"),
            "max_score": 100,
            "normalized_score": candidate.get("final_score"),
            "evaluator": "n8n Workflow (AI: Meta Evaluation)",
            "evaluation_data": Json(pass3_meta),
            "interview_scheduled": False,
            "interview_date": None,
            "interviewers": None,
            "interview_outcome": None,
            "interview_notes": None
        }
    ]
    
    rank_data = {
        "rank": global_rank,
        "final_score": candidate.get("final_score", 0),
        "structured_normalized": candidate.get("structured_normalized"),
        "llm_normalized": candidate.get("llm_normalized"),
        "bonus_total": candidate.get("bonus_total", 0),
        "recommendation": candidate.get("recommendation") or candidate.get("category"),
        "confidence": candidate.get("confidence"),
        "pipeline_status": "EVALUATED",
        "contacted_at": None,
        "contacted_by": None,
        "interview_scheduled": False,
        "interview_date": None,
        "interviewers": None,
        "interview_outcome": None,
        "final_decision": None,
        "final_decision_date": None,
        "final_decision_by": None,
        "rejection_reason": status_reason,
        "notes": "n8n automated eval — PRJ-020. n8n automation SKIPPED for speed; build automation if workflow reused."
    }
    
    return {
        "applicant": applicant_data,
        "application": application_data,
        "evaluations": evaluations_data,
        "rank": rank_data
    }

def process_dq_candidate(candidate: Dict, global_rank: int) -> Dict:
    """Process a disqualified candidate (limited data, no scoring)."""
    first_name, last_name = split_name(candidate.get("name", ""))
    
    hours = candidate.get("hours")
    hours_valid = is_hour_valid(hours)
    
    dq_reason = candidate.get("disqualify_reason", "")
    work_auth = "HF-2" not in dq_reason
    
    applicant_data = {
        "email": candidate.get("email", "").lower().strip(),
        "first_name": first_name,
        "last_name": last_name,
        "phone": None,
        "location": candidate.get("location"),
        "linkedin": None,
        "github": candidate.get("github_url"),
        "portfolio": None,
        "resume_url": None
    }
    
    application_data = {
        "form_id": FORM_ID,
        "submitted_at": parse_iso_timestamp(EVAL_TIMESTAMP),
        "hours_per_week": hours_valid,
        "start_timeframe": None,
        "start_date": None,
        "work_authorization": work_auth,
        "track_interest": [],
        "track_experience": [],
        "skills_matrix": Json({}),
        "short_answer_1": "[DISQUALIFIED BEFORE SCORING]",
        "short_answer_2": "[DISQUALIFIED BEFORE SCORING]",
        "short_answer_3": None,
        "country": candidate.get("country"),
        "country_mismatch": False,
        "country_mismatch_detail": None,
        "structured_raw": None,
        "structured_max": 56,
        "structured_normalized": None,
        "bonus_military": False,
        "bonus_athlete": False,
        "bonus_total": 0,
        "inflation_flag": False,
        "strong_count": None,
        "valid_skill_count": None,
        "raw_response": None,
        "data_source": DATA_SOURCE,
        "evaluation_status": "DISQUALIFIED",
        "final_score": None,
        "recommendation": "AUTO-DISQUALIFIED",
        "confidence": None,
        "rank": global_rank,
        "college_major": candidate.get("major") if candidate.get("major") else None,
        "graduation_date": None,
        "resume_pages": None,
        "track_fit": None,
        "status_reason": dq_reason,
        "flag_ai_content": "no",
        "flag_inflation": False,
        "flag_country": False
    }
    
    rank_data = {
        "rank": global_rank,
        "final_score": 0,
        "structured_normalized": None,
        "llm_normalized": None,
        "bonus_total": 0,
        "recommendation": "AUTO-DISQUALIFIED",
        "confidence": None,
        "pipeline_status": "EVALUATED",
        "contacted_at": None,
        "contacted_by": None,
        "interview_scheduled": False,
        "interview_date": None,
        "interviewers": None,
        "interview_outcome": None,
        "final_decision": None,
        "final_decision_date": None,
        "final_decision_by": None,
        "rejection_reason": dq_reason,
        "notes": "Auto-disqualified before scoring. n8n automation SKIPPED for speed; build automation if workflow reused."
    }
    
    return {
        "applicant": applicant_data,
        "application": application_data,
        "evaluations": [],
        "rank": rank_data
    }

# =====================================================
# DATABASE OPERATIONS
# =====================================================

def insert_applicant(cur, data: Dict) -> int:
    """Insert applicant, return ID. ON CONFLICT UPDATE for idempotency."""
    cur.execute("""
        INSERT INTO applicants (
            email, first_name, last_name, phone, location, linkedin, 
            github, portfolio, resume_url
        ) VALUES (
            %(email)s, %(first_name)s, %(last_name)s, %(phone)s, 
            %(location)s, %(linkedin)s, %(github)s, %(portfolio)s, 
            %(resume_url)s
        )
        ON CONFLICT (email) DO UPDATE SET
            first_name = EXCLUDED.first_name,
            last_name = EXCLUDED.last_name,
            phone = COALESCE(EXCLUDED.phone, applicants.phone),
            location = COALESCE(EXCLUDED.location, applicants.location),
            linkedin = COALESCE(EXCLUDED.linkedin, applicants.linkedin),
            github = COALESCE(EXCLUDED.github, applicants.github),
            portfolio = COALESCE(EXCLUDED.portfolio, applicants.portfolio),
            resume_url = COALESCE(EXCLUDED.resume_url, applicants.resume_url),
            updated_at = CURRENT_TIMESTAMP
        RETURNING id
    """, data)
    return cur.fetchone()[0]

def insert_application(cur, applicant_id: int, data: Dict) -> int:
    """Insert application, return ID."""
    cur.execute("""
        INSERT INTO applications (
            applicant_id, form_id, submitted_at, hours_per_week, 
            start_timeframe, start_date, work_authorization, 
            track_interest, track_experience, skills_matrix,
            short_answer_1, short_answer_2, short_answer_3, country,
            country_mismatch, country_mismatch_detail, structured_raw,
            structured_max, structured_normalized, bonus_military,
            bonus_athlete, bonus_total, inflation_flag, strong_count,
            valid_skill_count, raw_response, data_source, 
            evaluation_status, final_score, recommendation, confidence,
            rank, college_major, graduation_date, resume_pages, 
            track_fit, status_reason, flag_ai_content, flag_inflation,
            flag_country
        ) VALUES (
            %(applicant_id)s, %(form_id)s, %(submitted_at)s, 
            %(hours_per_week)s, %(start_timeframe)s, %(start_date)s,
            %(work_authorization)s, %(track_interest)s, 
            %(track_experience)s, %(skills_matrix)s,
            %(short_answer_1)s, %(short_answer_2)s, %(short_answer_3)s,
            %(country)s, %(country_mismatch)s, %(country_mismatch_detail)s,
            %(structured_raw)s, %(structured_max)s, %(structured_normalized)s,
            %(bonus_military)s, %(bonus_athlete)s, %(bonus_total)s,
            %(inflation_flag)s, %(strong_count)s, %(valid_skill_count)s,
            %(raw_response)s, %(data_source)s, %(evaluation_status)s,
            %(final_score)s, %(recommendation)s, %(confidence)s,
            %(rank)s, %(college_major)s, %(graduation_date)s, 
            %(resume_pages)s, %(track_fit)s, %(status_reason)s,
            %(flag_ai_content)s, %(flag_inflation)s, %(flag_country)s
        )
        RETURNING id
    """, {**data, "applicant_id": applicant_id})
    return cur.fetchone()[0]

def insert_evaluation(cur, application_id: int, data: Dict) -> None:
    """Insert single evaluation row."""
    cur.execute("""
        INSERT INTO application_evaluations (
            application_id, evaluation_type, score, max_score, 
            normalized_score, evaluator, evaluation_data,
            interview_scheduled, interview_date, interviewers,
            interview_outcome, interview_notes
        ) VALUES (
            %(application_id)s, %(evaluation_type)s, %(score)s, 
            %(max_score)s, %(normalized_score)s, %(evaluator)s,
            %(evaluation_data)s, %(interview_scheduled)s, 
            %(interview_date)s, %(interviewers)s, %(interview_outcome)s,
            %(interview_notes)s
        )
    """, {**data, "application_id": application_id})

def insert_rank(cur, application_id: int, data: Dict) -> None:
    """Insert rank row."""
    cur.execute("""
        INSERT INTO application_ranks (
            application_id, rank, final_score, structured_normalized,
            llm_normalized, bonus_total, recommendation, confidence,
            pipeline_status, contacted_at, contacted_by, 
            interview_scheduled, interview_date, interviewers,
            interview_outcome, final_decision, final_decision_date,
            final_decision_by, rejection_reason, notes
        ) VALUES (
            %(application_id)s, %(rank)s, %(final_score)s,
            %(structured_normalized)s, %(llm_normalized)s,
            %(bonus_total)s, %(recommendation)s, %(confidence)s,
            %(pipeline_status)s, %(contacted_at)s, %(contacted_by)s,
            %(interview_scheduled)s, %(interview_date)s, %(interviewers)s,
            %(interview_outcome)s, %(final_decision)s, 
            %(final_decision_date)s, %(final_decision_by)s,
            %(rejection_reason)s, %(notes)s
        )
    """, {**data, "application_id": application_id})

# =====================================================
# MAIN MIGRATION
# =====================================================

def main():
    print("=" * 60)
    print("PRJ-020: Intern Application Data Migration")
    print("=" * 60)
    print(f"Source: {JSON_FILE}")
    print(f"Target: popdb (PostgreSQL)")
    print(f"User: {DB_CONNECTION['user']}")
    print()
    
    # Load password securely: env var first, then interactive prompt
    pw = os.environ.get("POP_WRITE_PASSWORD", "")
    if pw:
        print("🔑 Password loaded from POP_WRITE_PASSWORD env var")
    else:
        pw = getpass.getpass("🔑 Enter pop_write password: ")
    if not pw:
        print("❌ ERROR: No password provided.")
        sys.exit(1)
    DB_CONNECTION["password"] = pw
    
    # Load JSON data
    print("📂 Loading JSON file...")
    try:
        with open(JSON_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ ERROR: File not found: {JSON_FILE}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ ERROR: Invalid JSON: {e}")
        sys.exit(1)
    
    advance = data.get("all_advance", [])
    maybe = data.get("all_maybe", [])
    passt = data.get("all_pass", [])
    disqualified = data.get("all_disqualified", [])
    
    total = len(advance) + len(maybe) + len(passt) + len(disqualified)
    print(f"📊 Candidates loaded: {total} total")
    print(f"   ADVANCE: {len(advance)}")
    print(f"   MAYBE: {len(maybe)}")
    print(f"   PASS: {len(passt)}")
    print(f"   AUTO-DISQUALIFIED: {len(disqualified)}")
    print()
    
    if total != 92:
        print(f"⚠️  WARNING: Expected 92 candidates, got {total}")
    
    # Connect to database
    print("🔌 Connecting to database...")
    try:
        conn = psycopg2.connect(**DB_CONNECTION)
        conn.autocommit = True  # For pre-flight checks
        print("✅ Connected")
    except Exception as e:
        print(f"❌ ERROR: Database connection failed: {e}")
        sys.exit(1)
    
    # Verify schema
    print("🔍 Verifying schema...")
    if not verify_schema(conn):
        conn.close()
        sys.exit(1)
    
    # Check existing data
    check_existing_data(conn)
    
    # Begin transaction
    print("\n🔄 Starting transaction...")
    conn.autocommit = False
    cur = conn.cursor()
    
    try:
        applicant_count = 0
        application_count = 0
        evaluation_count = 0
        rank_count = 0
        global_rank = 0
        
        for category, candidates in [
            ("ADVANCE", advance),
            ("MAYBE", maybe),
            ("PASS", passt),
            ("AUTO-DISQUALIFIED", disqualified)
        ]:
            print(f"\n📋 Processing {category} ({len(candidates)} candidates)...")
            
            for candidate in candidates:
                global_rank += 1
                
                if category == "AUTO-DISQUALIFIED":
                    processed = process_dq_candidate(candidate, global_rank)
                else:
                    processed = process_scored_candidate(candidate, global_rank)
                
                # Insert applicant
                applicant_id = insert_applicant(cur, processed["applicant"])
                applicant_count += 1
                
                # Insert application
                app_id = insert_application(cur, applicant_id, processed["application"])
                application_count += 1
                
                # Insert evaluations (3 per scored candidate, 0 for DQ)
                for eval_data in processed["evaluations"]:
                    insert_evaluation(cur, app_id, eval_data)
                    evaluation_count += 1
                
                # Insert rank
                insert_rank(cur, app_id, processed["rank"])
                rank_count += 1
                
                if global_rank % 10 == 0:
                    print(f"   ✓ {global_rank}/92 processed...")
        
        # Final progress
        if global_rank % 10 != 0:
            print(f"   ✓ {global_rank}/92 processed...")
        
        # Commit transaction
        print("\n💾 Committing transaction...")
        conn.commit()
        print("✅ Transaction committed")
        
        # Print summary
        print()
        print("=" * 60)
        print("✅ MIGRATION SUCCESSFUL")
        print("=" * 60)
        print(f"📊 Final counts:")
        print(f"   applicants:  {applicant_count}")
        print(f"   applications: {application_count}")
        print(f"   evaluations: {evaluation_count}")
        print(f"   ranks:       {rank_count}")
        print(f"   TOTAL ROWS:  {applicant_count + application_count + evaluation_count + rank_count}")
        print()
        print(f"⚠️  REMINDER: n8n automation SKIPPED for speed.")
        print(f"   Build automation if workflow is reused.")
        print()
        print(f"⚠️  REMINDER: No contact/interview data inserted.")
        print(f"   Manual entry required after info from Stef.")
        
    except Exception as e:
        print(f"\n❌ ERROR during migration: {e}")
        import traceback
        traceback.print_exc()
        print("\n🔄 Rolling back transaction...")
        conn.rollback()
        print("✅ Transaction rolled back — no data was committed")
        sys.exit(1)
    
    finally:
        cur.close()
        conn.close()
        print("\n🔌 Database connection closed")
    
    print()
    print("=" * 60)
    print("Migration complete. Run validation queries next.")
    print("=" * 60)

if __name__ == "__main__":
    main()
