#!/usr/bin/env bash
set -e

echo "Formatting..."
poetry run black .

echo "Linting..."
poetry run ruff check .

echo "Type checking..."
poetry run mypy .