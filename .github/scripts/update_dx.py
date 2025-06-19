import requests
from datetime import datetime
import os

TOKEN = os.getenv("GH_TOKEN")
REPO = "Little-mighty-developer/ethical_hacker_notebook"

headers = {"Authorization": f"Bearer {TOKEN}"}
api_url = f"https://api.github.com/repos/{REPO}/pulls?state=closed&per_page=100"

response = requests.get(api_url, headers=headers, timeout=30)
pulls = response.json()

print(pulls)

if not isinstance(pulls, list):
    print("GitHub API error:", pulls)
    exit(1)

total_lines = 0
merge_times = []
review_times = []
unreviewed = 0
count = 0

for pr in pulls:
    if pr.get("merged_at"):
        count += 1
        pr_details = requests.get(pr["url"], headers=headers, timeout=30).json()
        total_lines += pr_details["additions"] + pr_details["deletions"]
        created = datetime.fromisoformat(pr["created_at"][:-1])
        merged = datetime.fromisoformat(pr["merged_at"][:-1])
        merge_times.append((merged - created).total_seconds() / 3600)

        reviews_url = pr["_links"]["review_comments"]["href"]
        reviews = requests.get(reviews_url, headers=headers, timeout=30).json()
        if reviews:
            first_review_time = datetime.fromisoformat(reviews[0]["created_at"][:-1])
            review_times.append((first_review_time - created).total_seconds() / 3600)
        else:
            unreviewed += 1

avg_pr_size = round(total_lines / count, 1)
avg_merge_time = round(sum(merge_times) / len(merge_times), 1)
avg_review_time = (
    round(sum(review_times) / len(review_times), 1) if review_times else "N/A"
)
unreviewed_pct = round((unreviewed / count) * 100, 1)

metrics = f"""

**Last updated:** {datetime.now().strftime("%Y-%m-%d")}

| Metric                      | Value        | Notes |
|-----------------------------|--------------|-------|
| 🔁 Avg PR Size              | {avg_pr_size} LOC | Lines of code added/removed |
| ⏱️ Avg Time to Review       | {avg_review_time} hours | Time to first comment |
| 🧵 Avg Time to Merge        | {avg_merge_time} hours | From PR open to merge |
| ⚠️ % Merged Without Review  | {unreviewed_pct}% | PRs with 0 comments |
| 🚑 Last Incident Recovery   | —            | Manually filled |
| 🧠 DX Label Trends          | —            | Labels like `dx:blocked` |
"""

with open("README.md", "r") as f:
    content = f.read()

marker = "# 📊 Developer Experience Metrics"
if marker in content:
    parts = content.split(marker)
    new_content = parts[0] + marker + metrics + parts[1]
    with open("README.md", "w") as f:
        f.write(new_content)
else:
    print("Marker not found in README.md")
