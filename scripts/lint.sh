#!/bin/sh

set -e

CURRENT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
BASE_DIR="$(dirname "$CURRENT_DIR")"

black --config "${BASE_DIR}/pyproject.toml" "${BASE_DIR}"
isort --recursive --settings-path "${BASE_DIR}/pyproject.toml" "${BASE_DIR}"
