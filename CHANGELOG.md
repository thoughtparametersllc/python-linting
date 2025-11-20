# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.1] - 2025-11-04

## [0.0.2] - 2025-11-04

## [0.0.3] - 2025-11-04

## [0.0.4] - 2025-11-04

## [0.0.5] - 2025-11-04

## [0.0.6] - 2025-11-04

## [0.0.7] - 2025-11-10

## [0.0.8] - 2025-11-10

## [0.0.9] - 2025-11-10

## [0.0.10] - 2025-11-15

## [0.0.11] - 2025-11-15

## [0.0.12] - 2025-11-16

## [0.0.13] - 2025-11-16

## [0.0.14] - 2025-11-16

## [0.0.15] - 2025-11-16

## [0.0.16] - 2025-11-16

## [0.0.17] - 2025-11-16

## [0.0.18] - 2025-11-16

## [0.0.19] - 2025-11-16

## [0.0.20] - 2025-11-16

## [0.0.21] - 2025-11-17

## [0.0.22] - 2025-11-17

## [0.0.23] - 2025-11-17

## [0.0.24] - 2025-11-19

## [0.0.25] - 2025-11-19

## [Unreleased]

### Added
- `generate-badges` input to control badge generation (default: false)
- `update-readme` input to automatically update README with badges (default: false)
- `readme-path` input to specify README file location (default: README.md)
- `badge-style` input to choose between relative paths or GitHub URLs (default: path)
- Automatic README update functionality with marker support
- Badge markers for controlled placement in README files

### Changed
- Badge generation is now opt-in via `generate-badges` input instead of always running
- README updates are now opt-in via `update-readme` input
- Improved badge generation logic with better error handling

### Fixed
- Aligned action.yml inputs with documented features in README.md
- Corrected CHANGELOG.md version history

## [0.0.25] - 2025-11-19

### Added
- Comprehensive GitHub workflows for CI/CD
- Workflow to test all GitHub Action features
- Automatic tagging workflow for main branch with semantic versioning
- GitHub Marketplace submission workflow
- Changelog validation in release process
- Security audit workflow with Dependabot
- Lint and test workflow for PRs and pushes
- Initial Python linting action with Pylint, Black, and MyPy support
- Flexible Python version support
- Custom requirements file support
- Comprehensive linting with detailed reporting
