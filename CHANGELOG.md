## v0.2.7 (2025-08-23)

### Fix

- **mypy**: remove explicit_package_bases to avoid duplicate __main__ error

## v0.2.6 (2025-08-23)

### Fix

- **pre-commit**: add missing newline in .vscode/extensions.json

## v0.2.5 (2025-08-23)

### Fix

- **pre-commit**: resolve pre-commit formatting errors

## v0.2.4 (2025-08-22)

### Fix

- **ci**: install Poetry with runner's Python instead of action

## v0.2.3 (2025-08-22)

### Fix

- **ci**: set poetry config before selecting python version

## v0.2.2 (2025-08-22)

### Fix

- **ci**: ensure poetry uses correct python version from setup-python

## v0.2.1 (2025-08-20)

### Fix

- **ci**: prepend `v` to release tag in GitHub Actions workflow

## v0.2.0 (2025-08-20)

### Feat

- **scheduler**: add player task preferences to assignment logic
- initial project setup with task planner

### Refactor

- **main**: extract run_with_args and remove hardcoded filenames
