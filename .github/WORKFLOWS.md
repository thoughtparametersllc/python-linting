# GitHub Workflows Documentation

This document describes the GitHub Actions workflows implemented in this repository.

## Overview

The repository includes a comprehensive suite of CI/CD workflows that ensure code quality, security, and automated releases. All workflows follow security best practices and are designed to be modular and maintainable.

## Workflows

### 1. Test Action (`test-action.yml`)

**Purpose**: Validates all features of the Python Linting GitHub Action.

**Triggers**:
- Pull requests to `main` (when action files change)
- Pushes to `main` (when action files change)
- Manual workflow dispatch

**Jobs**:
- **test-basic-linting**: Tests basic linting functionality
- **test-custom-options**: Tests custom linting options
- **test-requirements-file**: Tests with requirements file
- **test-badge-generation**: Tests SVG badge generation
- **test-readme-update**: Tests automatic README updates
- **test-update-badges-script**: Tests `update_badges.py` directly
- **test-python-versions**: Tests multiple Python versions (3.9-3.12)
- **test-summary**: Provides a summary of all tests

**Key Features**:
- Creates test Python files dynamically
- Validates badge generation
- Verifies README update functionality
- Tests across multiple Python versions
- Comprehensive validation of all action features

### 2. Changelog Check (`changelog-check.yml`)

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

### 3. Lint and Test (`lint-test.yml`)

**Purpose**: Runs comprehensive linting and testing on all code changes.

**Triggers**:
- Pull requests to `main`
- Pushes to `main`
- Manual workflow dispatch

**Jobs**:
- **lint-python**: Runs Black, Pylint, MyPy, and Flake8
- **lint-yaml**: Validates YAML syntax
- **test-update-badges**: Tests `update_badges.py` functionality
- **shellcheck**: Validates shell script syntax
- **security-scan**: Runs Bandit and Safety security scans
- **test-summary**: Provides completion summary

**Quality Checks**:
- Code formatting (Black)
- Code quality (Pylint, Flake8)
- Type checking (MyPy)
- YAML validation
- Security vulnerabilities (Bandit, Safety)

### 4. Release and Marketplace (`release.yml`)

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

### 5. Security Audit (`security-audit.yml`)

**Purpose**: Performs comprehensive security scanning and audits.

**Triggers**:
- Schedule (daily at 2 AM UTC)
- Pushes to `main`
- Pull requests to `main`
- Manual workflow dispatch

**Jobs**:
- **dependency-review**: Reviews dependency changes in PRs
- **python-security-scan**: Runs Bandit, pip-audit, and Safety
- **codeql-analysis**: Performs CodeQL security analysis
- **secret-scanning**: Scans for leaked secrets with TruffleHog
- **workflow-security**: Validates workflow security practices
- **security-summary**: Provides audit summary

**Security Checks**:
- Dependency vulnerabilities (Dependency Review, pip-audit, Safety)
- Code security issues (Bandit, CodeQL)
- Secret leakage (TruffleHog)
- Workflow permission review
- Action.yml security validation

**Artifacts**:
- Bandit security report (JSON)
- Safety security report (JSON)
- CodeQL analysis results

### 6. Dependabot Configuration (`dependabot.yml`)

**Purpose**: Automated dependency update management.

**Configuration**:
- **GitHub Actions**: Weekly updates on Mondays
- **Python packages**: Weekly updates on Mondays
- Auto-assigns reviewers
- Limits open PRs to 5 per ecosystem
- Ignores major version updates by default

**Labels**:
- `dependencies`
- `github-actions` or `python` (ecosystem-specific)

## Workflow Permissions

All workflows follow the principle of least privilege:
- Read-only by default
- Write permissions only where required (e.g., release creation, badge commits)
- Explicit permission declarations in workflows

## Security Best Practices

1. **Pinned Actions**: All third-party actions use specific versions
2. **Minimal Permissions**: Workflows request only necessary permissions
3. **Secret Handling**: No secrets exposed in logs or artifacts
4. **Input Validation**: All workflow inputs are validated
5. **Dependency Scanning**: Automated vulnerability detection
6. **Code Analysis**: Static and dynamic security analysis

## Workflow Dependencies

```
test-action.yml (validates action)
     ↓
lint-test.yml (validates code quality)
     ↓
changelog-check.yml (validates documentation)
     ↓
release.yml (creates releases)
     ↓
marketplace submission (manual)
```

Security workflows run independently and continuously.

## Usage Guidelines

### For Contributors

1. **Making Changes**:
   - Update CHANGELOG.md under `[Unreleased]` section
   - Ensure all tests pass in `test-action.yml`
   - Address linting issues from `lint-test.yml`
   - Review security scan results

2. **Creating Releases**:
   - Merge changes to `main` with updated CHANGELOG.md
   - `release.yml` automatically creates releases
   - Manually publish to GitHub Marketplace if desired

3. **Manual Release**:
   ```
   GitHub Actions → release.yml → Run workflow
   Select version: major/minor/patch or specific version
   ```

### For Maintainers

1. **Review Dependabot PRs**: Check and merge dependency updates
2. **Monitor Security Scans**: Review daily security audit results
3. **Release Approval**: Verify changelog before merging to main
4. **Marketplace**: Manually publish new versions to marketplace

## Troubleshooting

### Release Not Created
- Check CHANGELOG.md has `[Unreleased]` section with content
- Verify changelog follows Keep a Changelog format
- Check workflow logs for errors

### Tests Failing
- Review test logs in `test-action.yml`
- Ensure all action features work correctly
- Validate badge generation and README updates

### Security Alerts
- Review security audit job outputs
- Check uploaded security report artifacts
- Address vulnerabilities before merging

## Maintenance

### Regular Tasks
- Weekly: Review and merge Dependabot PRs
- Daily: Monitor security audit results
- Per release: Update CHANGELOG.md
- As needed: Review and update workflow configurations

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
