# GitHub Workflows Documentation

This document describes the GitHub Actions workflows implemented in this repository.

## Overview

The repository includes CI/CD workflows that ensure code quality and automated releases. All workflows follow security best practices and are designed to be modular and maintainable.

## Workflows

### 1. Changelog Check (`changelog-check.yml`)

**Purpose**: Ensures CHANGELOG.md is updated for substantive changes.

**Triggers**:

- Pull requests to `main` (on open, sync, reopen, ready_for_review)

**Jobs**:

- **check-changelog**: Validates changelog updates

**Logic**:

- Detects if substantive files were changed (not just docs/CI)
- Requires CHANGELOG.md update for substantive changes
- Verifies content exists in the Unreleased section
- Exempts documentation-only changes

**Validation Rules**:

- CHANGELOG.md must be modified if code changes
- Unreleased section must have entries
- Follows Keep a Changelog format

### 2. Lint and Test (`lint-test.yml`)

**Purpose**: Validates YAML syntax and formatting for workflow files and the action.yml using yamllint with strict rules.

**Triggers**:

- Pull requests to `main`
- Pushes to `main`
- Manual workflow dispatch

**Jobs**:

- **lint-yaml**: Validates YAML syntax using yamllint
  - Lints all workflow files in `.github/workflows/`
  - Validates `action.yml` syntax and structure
  - Enforces formatting standards with custom rules

**Quality Checks**:

- YAML syntax validation (ensures valid YAML structure)
- Line length enforcement (max 120 characters)
- Consistent indentation (2 or 4 spaces)
- Comment spacing (minimum 1 space from content)
- Proper YAML formatting standards

### 3. Release and Marketplace (`release.yml`)

**Purpose**: Automates semantic versioning, tagging, and release creation.

**Triggers**:

- Pushes to `main`
- Manual workflow dispatch (with version input)

**Jobs**:

- **check-changelog**: Validates unreleased changes exist
- **determine-version**: Calculates next semantic version
- **create-release**: Creates GitHub release with changelog notes
- **marketplace-submission**: Provides marketplace submission instructions
- **workflow-summary**: Summarizes release process

**Versioning Logic**:

- Automatically determines version bump (major/minor/patch)
- Defaults to patch version increment
- Detects breaking changes from changelog
- Supports manual version override

**Release Process**:

1. Checks for unreleased changes in CHANGELOG.md
2. Determines next version based on changes
3. Updates CHANGELOG.md with version and date
4. Creates and pushes git tag
5. Creates GitHub release with extracted notes
6. Updates major version tag (e.g., v1)
7. Provides marketplace submission instructions

**Requirements**:

- CHANGELOG.md must have Unreleased section with content
- Must follow Keep a Changelog format
- Semantic versioning (MAJOR.MINOR.PATCH)

## Workflow Permissions

All workflows follow the principle of least privilege:

- Read-only by default
- Write permissions only where required (e.g., release creation, badge commits)
- Explicit permission declarations in workflows

## Security Best Practices

1. **Pinned Actions**: All third-party actions use specific versions
2. **Minimal Permissions**: Workflows request only necessary permissions
3. **Input Validation**: All workflow inputs are validated

## Workflow Dependencies

```text
lint-test.yml (validates YAML syntax)
     ↓
changelog-check.yml (validates documentation)
     ↓
release.yml (creates releases)
     ↓
marketplace submission (manual)
```

## Usage Guidelines

### For Contributors

1. **Making Changes**:
   - Update CHANGELOG.md under `[Unreleased]` section
   - Ensure YAML files pass `lint-test.yml` validation
   - Follow changelog format requirements

2. **Creating Releases**:
   - Merge changes to `main` with updated CHANGELOG.md
   - `release.yml` automatically creates releases
   - Manually publish to GitHub Marketplace if desired

3. **Manual Release**:

   ```text
   GitHub Actions → release.yml → Run workflow
   Select version: major/minor/patch or specific version
   ```

### For Maintainers

1. **Release Approval**: Verify changelog before merging to main
2. **Marketplace**: Manually publish new versions to marketplace
3. **Version Tags**: Ensure major version tags (e.g., v1) point to latest release

## Troubleshooting

### Release Not Created

- Check CHANGELOG.md has `[Unreleased]` section with content
- Verify changelog follows Keep a Changelog format
- Check workflow logs for errors

### YAML Linting Fails

- Review lint-test.yml workflow logs
- Check for YAML syntax errors in workflow files
- Ensure action.yml is valid YAML
- Verify line length limits (max 120 characters)

## Maintenance

### Regular Tasks

- Per release: Update CHANGELOG.md
- As needed: Review and update workflow configurations
- Monitor workflow runs for failures

### Workflow Updates

When updating workflows:

1. Test changes in a feature branch
2. Update this documentation
3. Update CHANGELOG.md
4. Create PR and verify all checks pass

## References

- [Keep a Changelog](https://keepachangelog.com/)
- [Semantic Versioning](https://semver.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Marketplace](https://github.com/marketplace)
