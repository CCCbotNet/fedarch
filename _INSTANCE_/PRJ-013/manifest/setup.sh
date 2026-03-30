#!/bin/bash
# CCC-ID: SHD_2026-W12_006
# Purpose: L-149 Permission Hardening for PRJ-013 Paperless-ngx

echo "🚀 Starting L-149 Infrastructure Hardening for Paperless-ngx..."

# Create all necessary persistence directories
mkdir -p data
mkdir -p media
mkdir -p export
mkdir -p consume
mkdir -p pgdata
mkdir -p caddy_data
mkdir -p caddy_config

# Apply Recursive UID Synchronization (Standard: 1000:1000)
echo "🔒 Applying L-149 Recursive UID Sync (Standard: 1000:1000)..."
chown -R 1000:1000 ./data ./media ./export ./consume ./pgdata ./caddy_data ./caddy_config
chmod -R 777 ./data ./media ./export ./consume ./pgdata ./caddy_data ./caddy_config

echo "✅ Infrastructure Ready. Run 'docker-compose up -d' to start Paperless-ngx."