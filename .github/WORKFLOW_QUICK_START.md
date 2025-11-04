# Workflow Quick Start Guide

This guide provides a quick reference for using the GitHub workflows in this repository.

## For Contributors

### Making a Pull Request

1. **Create your feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**:
   - Edit code files as needed
   - Update `CHANGELOG.md` under the `[Unreleased]` section:
     ```markdown
     ## [Unreleased]
     
     ### Added
     - Your new feature description
     
     ### Changed
     - Any changes you made
     
     ### Fixed
     - Any bugs you fixed
     ```

3. **Commit and push**:
   ```bash
   git add .
   git commit -m "Your descriptive commit message"
   git push origin feature/your-feature-name
   ```

4. **Create Pull Request**:
   - Go to GitHub and create a PR to `main`
   - Wait for automated checks to complete:
     - ✅ Test Action - validates all action features
     - ✅ Lint & Test - checks code quality
     - ✅ Changelog Check - verifies changelog update
     - ✅ Security Audit - scans for vulnerabilities

5. **Address any failures**:
   - Review workflow logs for errors
   - Make fixes and push again
   - Workflows will re-run automatically

### Changelog Format

Follow [Keep a Changelog](https://keepachangelog.com/) format:

```markdown
## [Unreleased]

### Added
- New features

### Changed
- Changes in existing functionality

### Deprecated
- Soon-to-be removed features

### Removed
- Removed features

### Fixed
- Bug fixes

### Security
- Security fixes
```

## For Maintainers

### Merging Pull Requests

1. **Review PR**:
   - Ensure all checks pass (green checkmarks)
   - Review code changes
   - Verify changelog is updated
   - Check security scan results

2. **Merge to main**:
   - Click "Merge pull request"
   - Delete feature branch

3. **Automatic Release** (if changelog has unreleased changes):
   - `release.yml` workflow triggers automatically
   - Creates new version tag (semantic versioning)
   - Updates CHANGELOG.md with version and date
   - Creates GitHub Release with notes
   - Updates major version tag (e.g., v1)

### Manual Release

To trigger a release manually with a specific version:

1. Go to **Actions** → **Release and Marketplace**
2. Click **Run workflow**
3. Select version bump type:
   - `major` - Breaking changes (1.0.0 → 2.0.0)
   - `minor` - New features (1.0.0 → 1.1.0)
   - `patch` - Bug fixes (1.0.0 → 1.0.1)
   - Or specify exact version like `1.2.3`
4. Click **Run workflow**

### Publishing to GitHub Marketplace

After a release is created:

1. Go to **Releases** tab
2. Click **Edit** on the latest release
3. Check **"Publish this Action to the GitHub Marketplace"**
4. Review marketplace information
5. Accept terms
6. Click **Update release**

The action.yml already includes marketplace metadata:
- Name, description, author
- Branding (icon, color)
- All required fields

### Managing Dependabot

Dependabot automatically creates PRs for dependency updates:

1. **Review Dependabot PRs** weekly:
   - Check for breaking changes
   - Review release notes of updated dependencies
   - Ensure all tests pass

2. **Merge safe updates**:
   - Patch updates (e.g., 1.0.1 → 1.0.2) - usually safe
   - Minor updates (e.g., 1.0.0 → 1.1.0) - review changes
   - Major updates are ignored by default

3. **Batch merge**:
   - Can merge multiple Dependabot PRs at once
   - Update changelog with "Updated dependencies" entry

### Monitoring Security

1. **Daily Security Audits**:
   - Runs automatically at 2 AM UTC
   - Check **Actions** tab for results
   - Review any security findings

2. **Security Alerts**:
   - Check **Security** tab regularly
   - Review Dependabot alerts
   - Review CodeQL findings

3. **Artifacts**:
   - Security workflows upload detailed reports
   - Download artifacts from workflow runs for analysis

## Workflow Triggers

### Automatic Triggers

| Workflow | PR to main | Push to main | Schedule | Manual |
|----------|-----------|--------------|----------|--------|
| test-action.yml | ✅ (if action files change) | ✅ (if action files change) | ❌ | ✅ |
| changelog-check.yml | ✅ | ❌ | ❌ | ❌ |
| lint-test.yml | ✅ | ✅ | ❌ | ✅ |
| release.yml | ❌ | ✅ | ❌ | ✅ |
| security-audit.yml | ✅ | ✅ | ✅ (daily) | ✅ |

### Manual Workflow Dispatch

To manually run any workflow:

1. Go to **Actions** tab
2. Select workflow from left sidebar
3. Click **Run workflow** button
4. Select branch and any inputs
5. Click **Run workflow**

## Troubleshooting

### Workflow Fails on PR

**Symptom**: Red X on PR checks

**Solutions**:
1. Click "Details" to view logs
2. Common issues:
   - **Changelog Check fails**: Update CHANGELOG.md
   - **Lint fails**: Fix code formatting with Black
   - **Tests fail**: Review test logs, fix code
   - **Security scan fails**: Review and fix security issues

### Release Not Created

**Symptom**: Merged to main but no release

**Possible causes**:
1. **No unreleased changes**: CHANGELOG.md missing Unreleased section
2. **Empty unreleased section**: No entries under Unreleased
3. **Invalid format**: Changelog doesn't follow Keep a Changelog format

**Solution**:
1. Check CHANGELOG.md has:
   ```markdown
   ## [Unreleased]
   
   ### Added
   - Something here
   ```
2. Push to main or run release workflow manually

### Test Action Workflow Fails

**Symptom**: test-action.yml fails

**Common causes**:
1. **Action.yml syntax error**: Validate YAML
2. **Script error**: Check update_badges.py
3. **Missing dependencies**: Check action setup steps

**Debug**:
1. View workflow logs
2. Test action locally with act (if available)
3. Test update_badges.py manually:
   ```bash
   python3 update_badges.py --help
   ```

## Best Practices

### Commit Messages

Use conventional commits:
- `feat: Add new feature`
- `fix: Fix bug in badge generation`
- `docs: Update documentation`
- `chore: Update dependencies`
- `security: Fix security vulnerability`

### Changelog Entries

- Be descriptive but concise
- Use present tense ("Add" not "Added")
- Reference issues/PRs where applicable
- Group related changes together

### Code Changes

- Keep changes focused and minimal
- Add tests for new features
- Update documentation
- Run local linting before pushing
- Address security scan findings

## Resources

- [Full Workflow Documentation](.github/WORKFLOWS.md)
- [Keep a Changelog](https://keepachangelog.com/)
- [Semantic Versioning](https://semver.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
