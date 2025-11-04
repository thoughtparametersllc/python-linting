#!/usr/bin/env python3
"""
Script to update README.md with linting badges.

This script automatically inserts or updates linting badges in a README.md file.
It can use either local file paths or GitHub URLs for the badge SVG files.
"""

import argparse
import os
import re
import sys


def get_badge_markdown(badge_name, badge_path, use_url, github_repo):
    """
    Generate markdown for a badge.
    
    Args:
        badge_name: Name of the badge (e.g., 'pylint')
        badge_path: Local path to the badge
        use_url: Whether to use GitHub URL instead of local path
        github_repo: GitHub repository in format 'owner/repo'
    
    Returns:
        Markdown string for the badge
    """
    if use_url and github_repo:
        # Use GitHub raw URL
        branch = os.getenv('GITHUB_REF_NAME', 'main')
        badge_url = f"https://raw.githubusercontent.com/{github_repo}/{branch}/{badge_path}"
        return f"![{badge_name.capitalize()}]({badge_url})"
    else:
        # Use relative path
        return f"![{badge_name.capitalize()}]({badge_path})"


def find_badge_section(lines):
    """
    Find the badge section in README.md.
    
    Returns:
        Tuple of (start_index, end_index) or (None, None) if not found
    """
    start_idx = None
    end_idx = None
    
    for i, line in enumerate(lines):
        # Look for badge marker comments
        if '<!-- linting-badges-start -->' in line:
            start_idx = i
        elif '<!-- linting-badges-end -->' in line:
            end_idx = i
            break
    
    return start_idx, end_idx


def insert_badges_after_title(lines, badges_md):
    """
    Insert badges after the main title (first # heading).
    
    Args:
        lines: List of README lines
        badges_md: List of badge markdown strings
    
    Returns:
        Updated list of lines
    """
    # Find the first heading
    title_idx = None
    for i, line in enumerate(lines):
        if line.startswith('# '):
            title_idx = i
            break
    
    if title_idx is None:
        # No title found, insert at the beginning
        title_idx = -1
    
    # Check if there's already a badge section
    start_idx, end_idx = find_badge_section(lines)
    
    if start_idx is not None and end_idx is not None:
        # Replace existing badge section
        new_lines = lines[:start_idx + 1]
        new_lines.extend(badges_md)
        new_lines.extend(lines[end_idx:])
        return new_lines
    else:
        # Insert new badge section after title
        insert_position = title_idx + 1
        
        # Skip any existing badges or blank lines after title
        while insert_position < len(lines) and (
            lines[insert_position].strip() == '' or
            lines[insert_position].startswith('[![') or
            lines[insert_position].startswith('![')
        ):
            insert_position += 1
        
        # Build new content
        new_lines = lines[:title_idx + 1]
        new_lines.append('\n')
        new_lines.append('<!-- linting-badges-start -->\n')
        new_lines.extend(badges_md)
        new_lines.append('<!-- linting-badges-end -->\n')
        new_lines.append('\n')
        new_lines.extend(lines[insert_position:])
        
        return new_lines


def update_readme_with_badges(
    readme_path,
    badges_dir,
    use_url=False,
    github_repo=None,
    badge_position='after-title'
):
    """
    Update README.md with linting badges.
    
    Args:
        readme_path: Path to README.md file
        badges_dir: Directory containing badge SVG files
        use_url: Whether to use GitHub URLs instead of local paths
        github_repo: GitHub repository in format 'owner/repo'
        badge_position: Where to insert badges ('after-title' or custom position)
    
    Returns:
        True if successful, False otherwise
    """
    if not os.path.exists(readme_path):
        print(f"Error: README.md not found at {readme_path}")
        return False
    
    # Read README content
    with open(readme_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Generate badge markdown for each linting tool
    badge_tools = ['pylint', 'black', 'mypy']
    badges_md = []
    
    for tool in badge_tools:
        badge_file = os.path.join(badges_dir, f'{tool}.svg')
        if os.path.exists(badge_file) or use_url:
            badge_md = get_badge_markdown(tool, badge_file, use_url, github_repo)
            badges_md.append(f'{badge_md}\n')
    
    if not badges_md:
        print(f"Warning: No badge files found in {badges_dir}")
        return False
    
    # Insert badges based on position
    if badge_position == 'after-title':
        updated_lines = insert_badges_after_title(lines, badges_md)
    else:
        # Default behavior: after title
        updated_lines = insert_badges_after_title(lines, badges_md)
    
    # Write updated README
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.writelines(updated_lines)
    
    print(f"✓ Successfully updated {readme_path} with linting badges")
    return True


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description='Update README.md with linting badges'
    )
    parser.add_argument(
        '--readme',
        default='README.md',
        help='Path to README.md file (default: README.md)'
    )
    parser.add_argument(
        '--badges-dir',
        default='.github/badges',
        help='Directory containing badge SVG files (default: .github/badges)'
    )
    parser.add_argument(
        '--use-url',
        action='store_true',
        help='Use GitHub URLs instead of relative paths'
    )
    parser.add_argument(
        '--github-repo',
        help='GitHub repository in format owner/repo (e.g., user/my-repo)'
    )
    parser.add_argument(
        '--badge-position',
        default='after-title',
        help='Where to insert badges (default: after-title)'
    )
    
    args = parser.parse_args()
    
    # Get GitHub repo from environment if not provided
    github_repo = args.github_repo
    if not github_repo and args.use_url:
        github_repo = os.getenv('GITHUB_REPOSITORY')
        if not github_repo:
            print("Error: --github-repo or GITHUB_REPOSITORY environment variable required when using --use-url")
            sys.exit(1)
    
    success = update_readme_with_badges(
        args.readme,
        args.badges_dir,
        args.use_url,
        github_repo,
        args.badge_position
    )
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
