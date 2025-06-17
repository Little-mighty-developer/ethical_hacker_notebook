import os
import re
from pathlib import Path

def extract_title_from_md(file_path):
    """Extract the title from a markdown file's first heading."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Look for the first heading (starts with #)
            match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if match:
                return match.group(1).strip()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return None

def get_emoji_for_section(section):
    """Get an appropriate emoji for each section."""
    emoji_map = {
        'engineering_management': '🎯',
        'security_fundamentals': '🔍',
        'tools_techniques': '🛠️',
        'case_studies': '📊',
        'templates_resources': '📝'
    }
    return emoji_map.get(section, '📄')

def generate_toc():
    """Generate the table of contents."""
    repo_root = Path('.')
    toc = ["# 📚 Table of Contents\n"]
    toc.append("A comprehensive guide to ethical hacking and security engineering.\n")

    # Get all markdown files except table_of_contents.md and files in .github
    md_files = list(repo_root.rglob('*.md'))
    md_files = [f for f in md_files if f.name != 'table_of_contents.md' and '.github' not in f.parts]

    # Group files by their parent directory
    sections = {}
    for file in md_files:
        section = file.parent.name
        if section not in sections:
            sections[section] = []
        sections[section].append(file)

    # Sort sections and files
    for section in sorted(sections.keys()):
        emoji = get_emoji_for_section(section)
        toc.append(f"\n## {emoji} {section.replace('_', ' ').title()}")
        
        # Sort files within section
        for file in sorted(sections[section]):
            title = extract_title_from_md(file)
            if title:
                # Convert path to relative URL
                rel_path = file.relative_to(repo_root)
                toc.append(f"- [{title}]({rel_path})")

    # Add footer
    toc.append("\n---\n")
    toc.append("*Last updated: " + os.popen('date "+%Y-%m-%d"').read().strip() + "*\n")
    toc.append("\n*This table of contents is automatically generated. Check back regularly for updates and new content.*")

    return '\n'.join(toc)

def main():
    """Main function to update the table_of_contents.md file."""
    toc = generate_toc()
    
    # Write to table_of_contents.md
    with open('table_of_contents.md', 'w', encoding='utf-8') as f:
        f.write(toc)

if __name__ == "__main__":
    main() 