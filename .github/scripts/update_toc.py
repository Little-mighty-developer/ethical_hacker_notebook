"""
Script to automatically generate a table of contents from markdown files.
This script scans markdown files in the engineering_management directory and creates
a table of contents based on their first-level headings.
"""

import re
from pathlib import Path


def extract_title_from_md(file_path):
    """Extract the title from a markdown file's first heading.

    Args:
        file_path: Path to the markdown file.

    Returns:
        str: The extracted title if found, None otherwise.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            # Look for the first heading (starts with #)
            match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
            if match:
                return match.group(1).strip()
    except (IOError, OSError) as err:
        print(f"Error reading {file_path}: {err}")
    return None


def main():
    """Main function to generate the table of contents."""
    # Paths
    base = Path("./../../engineering_management/")
    toc_file = Path("./../../table_of_contents.md")

    # Get all markdown files
    md_files = list(base.rglob("*.md"))

    # Sort files by their path
    md_files.sort()

    # Write table of contents
    with open(toc_file, "w", encoding="utf-8") as file:
        file.write("# 📚 Table of Contents\n\n")

        for md_file in md_files:
            # Get relative path for the link
            rel_path = md_file.relative_to(base.parent)

            # Extract title from the file
            title = extract_title_from_md(md_file)
            if title:
                file.write(f"- [{title}]({rel_path})\n")
            else:
                # If no title found, use the filename
                title = md_file.stem.replace("-", " ").title()
                file.write(f"- [{title}]({rel_path})\n")


if __name__ == "__main__":
    main()
