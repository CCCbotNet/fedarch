#!/bin/bash
# CCC-ID: SHD_2026-W12_005
# Purpose: L-149 Permission Hardening for AnythingLLM

echo "🚀 Starting L-149 Infrastructure Hardening..."

# Create necessary persistence directories
mkdir -p storage
mkdir -p caddy_data
mkdir -p caddy_config

# Apply Recursive UID Synchronization (Standard: 1000:1000)
echo "🔒 Applying L-149 Recursive UID Sync..."
chown -R 1000:1000 ./storage
chmod -R 777 ./storage

echo "✅ Infrastructure Ready. Run 'docker-compose up -d' to start services."