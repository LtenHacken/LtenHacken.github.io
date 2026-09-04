#!/usr/bin/env bash

set -euo pipefail

# Always run from the repository root, even when invoked from elsewhere.
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$script_dir"

if ! command -v bundle >/dev/null 2>&1; then
  echo "Bundler is required. Install Ruby and then run: gem install bundler" >&2
  exit 1
fi

if ! bundle check >/dev/null 2>&1; then
  echo "Installing the site's Ruby dependencies..."
  bundle install
fi

echo "Starting the website at http://localhost:4000"
exec bundle exec jekyll serve \
  --host 127.0.0.1 \
  --port 4000 \
  --livereload
