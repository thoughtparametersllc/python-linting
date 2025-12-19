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
     - ✅ Lint & Test - validates YAML syntax, formatting, and action.yml structure
     - ✅ Changelog Check - verifies changelog update

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

### Monitoring Action Usage

1. **Check Workflow Runs**:
   - Monitor the **Actions** tab for workflow results
   - Review any failures promptly

2. **Review Logs**:
   - Click on failed workflow runs to see detailed logs
   - Address YAML syntax errors
   - Fix changelog format issues

## Workflow Triggers

### Automatic Triggers

| Workflow | PR to main | Push to main | Schedule | Manual |
|----------|-----------|--------------|----------|--------|
| changelog-check.yml | ✅ | ❌ | ❌ | ❌ |
| lint-test.yml | ✅ | ✅ | ❌ | ✅ |
| release.yml | ❌ | ✅ | ❌ | ✅ |

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
   - **YAML Lint fails**: Fix YAML syntax errors

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

### YAML Linting Fails

**Symptom**: lint-test.yml fails

**Common causes**:

1. **Action.yml syntax error**: Validate YAML syntax
2. **Workflow file errors**: Check workflow YAML files
3. **Line length issues**: Lines exceeding 120 characters

**Debug**:

1. View workflow logs for specific errors
2. Validate YAML locally:

   ```bash
   python -c "import yaml; yaml.safe_load(open('action.yml'))"
   yamllint .github/workflows/
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
