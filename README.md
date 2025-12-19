# python-linting

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-Python%20Linting-blue.svg?colorA=24292e&colorB=0366d6&style=flat&longCache=true&logo=github)](https://github.com/marketplace/actions/python-linting)

A comprehensive GitHub Action for Python code quality enforcement. Runs **Pylint**, **Black**, and **MyPy** with automatic badge generation and detailed reporting.

## Features

- 🐍 **Flexible Python version support** - Specify any Python version using `actions/setup-python`
- 📦 **Custom requirements** - Install additional dependencies from a requirements file
- 🔍 **Comprehensive linting** - Run Pylint, Black, and MyPy in a single action
- 📊 **Detailed reporting** - View results in GitHub Actions summary
- 🏅 **Automatic badge generation** - Creates and commits SVG badges for each linter
- ⚙️ **Highly configurable** - Customize options for each linting tool

## Prerequisites

- Your repository must contain Python code
- For badge commits: the workflow needs `contents: write` permission

## Usage

### Basic Example

```yaml
name: Python Linting
on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    permissions:
      contents: write  # Required for badge commits
    steps:
      - uses: actions/checkout@v4
      
      - name: Python Linting
        uses: thoughtparametersllc/python-linting@v1
```

### Advanced Example with Custom Options

```yaml
name: Python Linting
on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
      
      - name: Python Linting
        uses: thoughtparametersllc/python-linting@v1
        with:
          python-version: '3.11'
          requirements-file: 'requirements.txt'
          pylint-options: '--max-line-length=120 --disable=C0111'
          black-options: '--line-length=120'
          mypy-options: '--strict --ignore-missing-imports'
          commit-badges: 'true'
          badge-directory: '.github/badges'
```

### Example without Badge Commits

```yaml
- name: Python Linting
  uses: thoughtparametersllc/python-linting@v1
  with:
    python-version: '3.10'  # Always quote version numbers
    commit-badges: 'false'  # Disable automatic badge commits
```

### Example with Multiple Python Versions

```yaml
name: Python Linting
on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.9', '3.10', '3.11', '3.12']
    steps:
      - uses: actions/checkout@v4
      
      - name: Python Linting
        uses: thoughtparametersllc/python-linting@v1
        with:
          python-version: ${{ matrix.python-version }}
          commit-badges: 'false'  # Only one job should commit badges
```

## Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `python-version` | Python version to use for linting | No | `3.x` |
| `requirements-file` | Path to requirements file for additional dependencies | No | `requirements.txt` |
| `pylint-options` | Additional options to pass to pylint | No | `''` |
| `black-options` | Additional options to pass to black | No | `''` |
| `mypy-options` | Additional options to pass to mypy | No | `''` |
| `commit-badges` | Whether to commit generated SVG badges back to the repository | No | `true` |
| `badge-directory` | Directory to save the generated SVG badges | No | `.github/badges` |

## Outputs

This action does not produce any outputs. Results are displayed in the GitHub Actions summary and as SVG badges (if enabled).

## Badges

When `commit-badges` is set to `true` (default), the action automatically generates and commits three SVG badge files to your repository:

- `{badge-directory}/pylint.svg` - Pylint status badge
- `{badge-directory}/black.svg` - Black status badge
- `{badge-directory}/mypy.svg` - MyPy status badge

### Displaying Badges in README

Add these badges to your README.md to show linting status:

```markdown
![Pylint](.github/badges/pylint.svg)
![Black](.github/badges/black.svg)
![MyPy](.github/badges/mypy.svg)
```

### Badge Colors

- 🟢 Green (`success`) - No issues found
- 🔴 Red (`failure`) - Issues detected

## Permissions

This action requires the following permissions:

```yaml
permissions:
  contents: write  # Required only if commit-badges is 'true'
```

If you set `commit-badges: 'false'`, you can use:

```yaml
permissions:
  contents: read
```

## Troubleshooting

### Badge Commits Failing

**Issue**: The action fails to commit badges back to the repository.

**Solutions**:
- Ensure `contents: write` permission is set in your workflow
- Verify that branch protection rules allow the `github-actions[bot]` to push
- Check that the badge directory exists or can be created

### Linting Tools Not Found

**Issue**: Pylint, Black, or MyPy commands fail with "command not found".

**Solutions**:
- Ensure Python is properly set up (the action handles this automatically)
- Check that the Python version you specified is available
- Review the "Install Linting Tools" step logs for errors

### Requirements Installation Fails

**Issue**: Additional requirements cannot be installed.

**Solutions**:
- Verify the `requirements-file` path is correct relative to repository root
- Ensure the requirements file exists and is readable
- Check for syntax errors in the requirements file
- Review dependency conflicts in the workflow logs

### False Positive Linting Errors

**Issue**: Linters report issues that you want to ignore.

**Solutions**:
- Use linter-specific options to customize behavior:
  - Pylint: `pylint-options: '--disable=C0111,W0212'`
  - Black: `black-options: '--line-length=120'`
  - MyPy: `mypy-options: '--ignore-missing-imports'`
- Create configuration files (`.pylintrc`, `pyproject.toml`) in your repository

### Action Fails on Pull Requests from Forks

**Issue**: Badge commits fail on pull requests from forked repositories.

**Solution**: This is expected behavior for security reasons. Forks don't have write access. Consider:
- Setting `commit-badges: 'false'` for PRs from forks
- Using a conditional in your workflow:
  ```yaml
  commit-badges: ${{ github.event.pull_request.head.repo.full_name == github.repository && 'true' || 'false' }}
  ```

## How It Works

1. **Setup Python**: Installs specified Python version
2. **Install Tools**: Installs Pylint, Black, and MyPy
3. **Install Requirements**: (Optional) Installs dependencies from your requirements file
4. **Run Linters**: Executes all three linting tools sequentially
5. **Generate Badges**: Creates SVG badges showing pass/fail status
6. **Commit Badges**: (Optional) Commits badges back to your repository
7. **Generate Summary**: Creates detailed GitHub Actions summary with results

## Best Practices

### When to Use This Action

✅ **Good use cases:**
- CI/CD pipelines for Python projects
- Pre-merge checks on pull requests
- Automated code quality enforcement
- Ensuring consistent code style across teams

❌ **Not recommended for:**
- Local development (use pre-commit hooks instead)
- Projects with custom linting workflows requiring specific tool versions
- Repositories with complex multi-language setups

### Recommended Workflow Configuration

```yaml
name: Code Quality
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
      
      - name: Python Linting
        uses: thoughtparametersllc/python-linting@v1
        with:
          python-version: '3.11'
          requirements-file: 'requirements.txt'
```

### Configuration Files

You can customize linter behavior using configuration files in your repository:

- **Pylint**: `.pylintrc` or `pyproject.toml`
- **Black**: `pyproject.toml`
- **MyPy**: `mypy.ini` or `pyproject.toml`

Example `pyproject.toml`:

```toml
[tool.black]
line-length = 120
target-version = ['py311']

[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true

[tool.pylint.format]
max-line-length = 120

[tool.pylint.messages_control]
disable = ["C0111", "C0103"]
```

## Examples

### Example: Python Package with Tests

```yaml
name: Test and Lint
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pytest

  lint:
    runs-on: ubuntu-latest
    needs: test  # Run after tests pass
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
      - uses: thoughtparametersllc/python-linting@v1
        with:
          requirements-file: 'requirements.txt'
```

### Example: Monorepo with Python Subdirectory

```yaml
name: Lint Python Code
on: [push]

jobs:
  lint:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: ./python-service
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
      
      - name: Python Linting
        uses: thoughtparametersllc/python-linting@v1
        with:
          requirements-file: './python-service/requirements.txt'
```

### Example: Read-Only Mode (No Badge Commits)

```yaml
name: PR Linting Check
on: pull_request

jobs:
  lint:
    runs-on: ubuntu-latest
    permissions:
      contents: read  # Read-only for PR checks
    steps:
      - uses: actions/checkout@v4
      
      - name: Python Linting
        uses: thoughtparametersllc/python-linting@v1
        with:
          commit-badges: 'false'
```

## Development

This repository includes comprehensive GitHub workflows for CI/CD:

- **Test Action**: Validates all action features across multiple Python versions
- **Lint & Test**: Ensures code quality with Pylint, Black, MyPy, and Flake8
- **Changelog Check**: Requires changelog updates for substantive changes
- **Release & Marketplace**: Automated semantic versioning and tagging

For detailed workflow documentation, see [.github/WORKFLOWS.md](.github/WORKFLOWS.md).

### Quick Start for Contributors

See [.github/WORKFLOW_QUICK_START.md](.github/WORKFLOW_QUICK_START.md) for a quick reference guide.

### Releasing

The release workflow supports both automatic semantic versioning and manual version specification:

**Automatic Release** (when changes are merged to main):

- Automatically detects version bump from CHANGELOG.md
- Creates release with extracted changelog notes
- Updates major version tag (e.g., v1)

**Manual Release** (for specific versions):

1. Go to Actions → Release and Marketplace → Run workflow
2. Enter version as `1.0.0` or `v1.0.0` (for specific version) or `major`/`minor`/`patch` (for semantic bump)
3. The workflow will create the release and update tags

### Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

**Quick steps:**

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Update CHANGELOG.md under the `[Unreleased]` section
5. Ensure all tests pass
6. Submit a pull request

## Support

- 📚 [Documentation](.github/WORKFLOWS.md)
- 🐛 [Report a Bug](https://github.com/thoughtparametersllc/python-linting/issues/new?template=bug_report.yml)
- 💡 [Request a Feature](https://github.com/thoughtparametersllc/python-linting/issues/new?template=feature_request.yml)
- 🔒 [Security Policy](SECURITY.md)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Built with:
- [Pylint](https://pylint.pycqa.org/) - Python code analysis
- [Black](https://github.com/psf/black) - Python code formatter
- [MyPy](https://mypy-lang.org/) - Static type checker
