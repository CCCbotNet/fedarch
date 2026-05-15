#!/usr/bin/env python3
"""PRJ-020: Post-Migration Validation"""

import os, getpass, psycopg2

pw = os.environ.get('POP_WRITE_PASSWORD', '') or getpass.getpass('🔑 Enter pop_write password: ')
conn = psycopg2.connect(
    host='db-postgresql-atl1-weownnet-do-user-24194004-0.i.db.ondigitalocean.com',
    port=25060, database='popdb', user='pop_write', password=pw,
    sslmode='require', sslrootcert=os.path.expanduser('~/.postgresql/ca-certificate.crt')
)
conn.autocommit = True
cur = conn.cursor()

queries = [
    ('1. ROW COUNTS', '''
        SELECT 'applicants' as tbl, COUNT(*) FROM applicants
        UNION ALL SELECT 'applications', COUNT(*) FROM applications
        UNION ALL SELECT 'evaluations', COUNT(*) FROM application_evaluations
        UNION ALL SELECT 'ranks', COUNT(*) FROM application_ranks
    '''),
    ('2. CATEGORY DISTRIBUTION', '''
        SELECT recommendation, COUNT(*) FROM applications 
        GROUP BY recommendation 
        ORDER BY CASE recommendation 
            WHEN 'ADVANCE' THEN 1 WHEN 'MAYBE' THEN 2 
            WHEN 'PASS' THEN 3 WHEN 'AUTO-DISQUALIFIED' THEN 4 END
    '''),
    ('3. EVALUATION TYPES', '''
        SELECT evaluation_type, COUNT(*) FROM application_evaluations 
        GROUP BY evaluation_type ORDER BY evaluation_type
    '''),
    ('4. PIPELINE STATUS', '''
        SELECT pipeline_status, COUNT(*) FROM application_ranks GROUP BY pipeline_status
    '''),
    ('5. NO INTERVIEW DATA', '''
        SELECT COUNT(*) as total,
            COUNT(interview_date) as with_interview,
            COUNT(contacted_at) as with_contact,
            COUNT(final_decision) as with_decision
        FROM application_ranks
    '''),
    ('6. TOP 5 ADVANCE', '''
        SELECT a.first_name || ' ' || a.last_name as name,
            app.final_score, r.rank
        FROM applicants a
        JOIN applications app ON a.id = app.applicant_id
        JOIN application_ranks r ON app.id = r.application_id
        WHERE app.recommendation = 'ADVANCE'
        ORDER BY r.rank LIMIT 5
    '''),
    ('7. GLOBAL RANK SEQUENCE', '''
        SELECT MIN(rank) as min_rank, MAX(rank) as max_rank, COUNT(DISTINCT rank) as unique_ranks FROM application_ranks
    '''),
    ('8. NEW COLUMNS DATA', '''
        SELECT COUNT(college_major) as major, COUNT(graduation_date) as grad,
            COUNT(resume_pages) as resume, COUNT(track_fit) as track,
            COUNT(status_reason) as reason
        FROM applications
    '''),
    ('9. DQ EVAL COUNT', '''
        SELECT app.recommendation, COUNT(e.id) as eval_count
        FROM applications app
        LEFT JOIN application_evaluations e ON app.id = e.application_id
        GROUP BY app.recommendation ORDER BY app.recommendation
    '''),
    ('10. AVG SCORES BY CATEGORY', '''
        SELECT recommendation, ROUND(AVG(final_score),2) as avg, MIN(final_score) as min, MAX(final_score) as max
        FROM applications WHERE final_score IS NOT NULL
        GROUP BY recommendation ORDER BY AVG(final_score) DESC
    '''),
]

print("=" * 60)
print("PRJ-020: Post-Migration Validation")
print("=" * 60)

for title, q in queries:
    print(f'\n--- {title} ---')
    cur.execute(q)
    cols = [d[0] for d in cur.description]
    
    # Calculate column widths
    rows = cur.fetchall()
    widths = [max(len(str(c)), max((len(str(r[i])) for r in rows), default=0)) for i, c in enumerate(cols)]
    
    fmt = ' | '.join(f'{{:<{w}}}' for w in widths)
    print(fmt.format(*cols))
    print('-+-'.join('-' * w for w in widths))
    for row in rows:
        print(fmt.format(*[str(v) for v in row]))

cur.close()
conn.close()
print('\n' + '=' * 60)
print('✅ Validation complete')
print('=' * 60)
