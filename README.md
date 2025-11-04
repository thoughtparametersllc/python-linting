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
```

### Advanced Example

```yaml
- name: Python Linting
  uses: thoughtparametersllc/python-linting@v1
  with:
    python-version: '3.11'
    requirements-file: 'requirements.txt'
    pylint_options: '--max-line-length=120'
    black_options: '--line-length=120'
    mypy_options: '--strict'
```

## Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `python-version` | Python version to use for linting | No | `3.x` |
| `requirements-file` | Path to requirements file for additional dependencies | No | `''` |
| `pylint_options` | Additional options to pass to pylint | No | `''` |
| `black_options` | Additional options to pass to black | No | `''` |
| `mypy_options` | Additional options to pass to mypy | No | `''` |

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
