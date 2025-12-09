Here is a comprehensive `CONTRIBUTING.md` tailored for your repository. It incorporates the specific tools (Black, Pylint, MyPy, Flake8) and the release workflow we discussed.

-----

# Contributing to Python Linting Action

First off, thank you for considering contributing to this project\! It's people like you that make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

## 🚀 Getting Started

1.  **Fork the repository** on GitHub.
2.  **Clone your fork** locally:
    ```bash
    git clone https://github.com/your-username/python-linting.git
    cd python-linting
    ```
3.  **Create a new branch** for your feature or fix:
    ```bash
    git checkout -b feature/amazing-new-feature
    ```

## 🛠️ Development Workflow

### Coding Standards

We want to keep the codebase clean and consistent. Before submitting your code, please ensure it passes the same quality checks that this Action enforces:

  * **Formatting:** We use [Black](https://github.com/psf/black).
  * **Linting:** We use [Pylint](https://pylint.pycqa.org/) and [Flake8](https://flake8.pycqa.org/).
  * **Type Checking:** We use [MyPy](https://mypy-lang.org/).

You can run these tools locally to verify your changes:

```bash
# Example local checks
black .
pylint src/
mypy src/
flake8 .
```

### Updating the Changelog

**Crucial Step:** All substantive changes (features, fixes, breaking changes) must be documented.

  * Open `CHANGELOG.md`.
  * Add a bullet point describing your change under the `[Unreleased]` section.
  * Follow the format: `* Description of change (@your-username)`

## 📮 Submitting a Pull Request

1.  **Push your branch** to GitHub:
    ```bash
    git push origin feature/amazing-new-feature
    ```
2.  **Open a Pull Request** against the `main` branch.
3.  **Fill out the PR Template:** Describe your changes clearly and link to any relevant issues (e.g., `Fixes #123`).
4.  **Wait for CI:** Ensure all GitHub Actions workflows (Tests, Linting, Changelog Check) pass.

-----

## 🔄 Release Process (For Maintainers)

This repository uses a specific workflow to handle semantic versioning and "floating tags" (e.g., keeping `v1` pointing to the latest `v1.x.x` release).

### Automated Release

When a PR is merged to `main` with a valid `CHANGELOG.md` entry:

1.  The system automatically detects the version bump.
2.  A new release is created with notes from the changelog.
3.  The major version tag (e.g., `v1`) is automatically moved to the new release.

### Manual Release / Tag Correction

If you need to manually retarget the major version tag (e.g., `v1`) to a specific release (e.g., `v1.0.1`), use the following commands locally:

```bash
# 1. Delete the old major version tag locally and remotely
git tag -d v1
git push origin --delete v1

# 2. Create the tag pointing to the specific commit/release
git tag v1 v1.0.1
git push origin v1
```
