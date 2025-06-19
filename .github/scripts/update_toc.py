import re
from pathlib import Path


def extract_title_from_md(file_path):
    """Extract the title from a markdown file's first heading."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            # Look for the first heading (starts with #)
            match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
            if match:
                return match.group(1).strip()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return None


# Paths
base = Path("./../../engineering_management/")
toc_file = Path("./../../table_of_contents.md")

# Get all markdown files
md_files = list(base.rglob("*.md"))

# Sort files by their path
md_files.sort()

# Write table of contents
with toc_file.open("w") as f:
    f.write("# 📚 Table of Contents\n\n")

    for md_file in md_files:
        # Get relative path for the link
        rel_path = md_file.relative_to(base.parent)

        # Extract title from the file
        title = extract_title_from_md(md_file)
        if title:
            f.write(f"- [{title}]({rel_path})\n")
        else:
            # If no title found, use the filename
            title = md_file.stem.replace("-", " ").title()
            f.write(f"- [{title}]({rel_path})\n")
