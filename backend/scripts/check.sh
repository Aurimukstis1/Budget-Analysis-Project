#!/usr/bin/env bash
set -e

echo "Linting..."
poetry run ruff check .

echo "Formatting..."
poetry run black .

echo "Type checking..."
poetry run mypy .