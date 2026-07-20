#!/usr/bin/env bash

set -e  # Exit immediately if any command fails

echo "Stopping containers..."
docker compose down -v

echo "Removing Postgis data directory..."
rm -rf ./postgis_data

echo "Starting containers..."
docker compose up -d

echo "Database reset complete. Init scripts reran successfully."
