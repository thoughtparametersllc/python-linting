# python-linting

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-Python%20Linting-blue.svg?colorA=24292e&colorB=0366d6&style=flat&longCache=true&logo=github)](https://github.com/marketplace/actions/python-linting)

GitHub Action to perform Python linting with Black, Pylint, and MyPy.

## Features

- 🐍 **Flexible Python version support** - Specify any Python version using `actions/setup-python`
- 📦 **Custom requirements** - Install additional dependencies from a requirements file
- 🔍 **Comprehensive linting** - Run Pylint, Black, and MyPy in a single action
- 📊 **Detailed reporting** - View results in GitHub Actions summary

## Usage

### Basic Example

```yaml
- name: Python Linting
  uses: thoughtparametersllc/python-linting@v1
  permissions:
    contents: write
```

### Advanced Example

```yaml
- name: Python Linting
  uses: thoughtparametersllc/python-linting@v1
  permissions:
    contents: write
  with:
    python-version: '3.11'
    requirements-file: 'requirements.txt'
    pylint_options: '--max-line-length=120'
    black_options: '--line-length=120'
    mypy_options: '--strict'
```

**Manual Badge References**:

```markdown
![Pylint](.github/badges/pylint.svg)
![Black](.github/badges/black.svg)
![MyPy](.github/badges/mypy.svg)
```

## Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `python-version` | Python version to use for linting | No | `3.x` |
| `requirements-file` | Path to requirements file for additional dependencies | No | `''` |
| `pylint_options` | Additional options to pass to pylint | No | `''` |
| `black_options` | Additional options to pass to black | No | `''` |
| `mypy_options` | Additional options to pass to mypy | No | `''` |

## Development

This repository includes comprehensive GitHub workflows for CI/CD:

- **Test Action**: Validates all action features across multiple Python versions
- **Lint & Test**: Ensures code quality with Pylint, Black, MyPy, and Flake8
- **Changelog Check**: Requires changelog updates for substantive changes
- **Release & Marketplace**: Automated semantic versioning and tagging

For detailed workflow documentation, see [.github/WORKFLOWS.md](.github/WORKFLOWS.md).

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

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Update CHANGELOG.md under the `[Unreleased]` section
5. Ensure all tests pass
6. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
