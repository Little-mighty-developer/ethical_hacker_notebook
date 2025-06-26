📘 Key Definitions --- Speak DevOps Without the Jargon
====================================================

> Because understanding should never be gatekept. Learn it. Use it. Bake it in. 🧁

* * * * *

### 🪵 **Trunk-Based Development**

**What is it?**\
All developers commit to the main branch (aka "trunk") frequently --- often daily. Instead of long-lived feature branches, you keep things short, small, and merge-ready.

**Think of it like...**\
Everyone baking in the same kitchen, updating the menu as they go --- not hiding away with solo secret recipes.

**Benefits:**

-   Faster feedback loops

-   Less painful merges

-   Safer deploys

-   Encourages collaboration

**Common misconceptions:**

-   "No branches allowed" → False! It just means *short-lived* ones.

-   "We'll break prod more" → Actually, you'll break less *and* fix faster.

**How to get started:**

-   Keep PRs small and merge often

-   Use feature flags to hide in-progress work

-   Automate testing + code reviews

-   Educate the team with pair sessions or mob reviews

* * * * *

### 🌪️ **Chaos Engineering**

**What is it?**\
The practice of intentionally introducing failure into your system --- in a controlled, observable way --- to improve resilience.

**Think of it like...**\
Testing what happens when the power goes out in your bakery... on purpose.

**Benefits:**

-   Builds confidence in your recovery plans

-   Identifies hidden weaknesses

-   Prepares you for real outages

**Common misconceptions:**

-   "It's just breaking stuff" → Nope. It's scientific and planned.

-   "Only huge companies need this" → Any system can benefit.

**How to get started:**

-   Pick a low-risk service and simulate a timeout or crash

-   Monitor what happens (alerts? fallback?)

-   Use tools like Gremlin or Chaos Monkey

-   Debrief what worked --- and what didn't

* * * * *

### 🧪 **Shift-Left Testing**

**What is it?**\
Bringing testing earlier in the development lifecycle --- as early as writing the code itself.

**Think of it like...**\
Tasting your batter *before* baking the cake, not after it's frosted and served.

**Benefits:**

-   Catch bugs early = cheaper fixes

-   Less rework

-   More confident deploys

-   Culture of quality

**Common misconceptions:**

-   "We already test at the end" → That's *right-shifted* testing

-   "Slows down devs" → Actually saves time overall

**How to get started:**

-   Use unit tests with every PR

-   Add testing to your CI pipeline

-   Use Test-Driven Development (TDD) where it fits

-   Train the team to write testable code

* * * * *

### 🔁 **Automated Rollback Strategies**

**What is it?**\
When a deployment fails, the system automatically reverts to the last known good state --- without human panic.

**Think of it like...**\
Your oven senses a burning cake and swaps in yesterday's perfect batch.

**Benefits:**

-   Reduces downtime

-   Builds deployment confidence

-   Protects the user experience

**Common misconceptions:**

-   "We'll become careless" → No --- it supports safe risk-taking

-   "It's hard to set up" → Not with modern CI/CD tools

**How to get started:**

-   Use tools that support versioned deploys (ArgoCD, Spinnaker)

-   Define success/failure conditions

-   Automate rollback on failure detection (e.g., failed health checks)

-   Test rollback in staging first!

* * * * *

### 🕵🏽‍♀️ **Root Cause Tracking Strategies**

**What is it?**\
A systematic way to understand *why* something broke --- not just *what* broke.

**Think of it like...**\
Instead of blaming the burnt croissant, you check the oven temp, timer, and flour batch.

**Benefits:**

-   Prevents recurring issues

-   Shifts focus from blame to learning

-   Encourages systemic fixes

**Common misconceptions:**

-   "It takes too long" → Faster than fixing the same bug 5x

-   "We know what went wrong" → But *why* did it happen?

**How to get started:**

-   Use a postmortem template (blameless!)

-   Track contributing factors, not just symptoms

-   Use RCA tools (5 Whys, Fishbone diagrams)

-   Track action items in public team docs

* * * * *

### 🚩 **Spotting Risky PRs (Pull Requests)**

**What is it?**\
Recognizing signs that a pull request might cause problems if merged as-is.

**Think of it like...**\
A baker tries to sneak in 14 mystery ingredients with no labels. Someone has to ask: "What's that?"

**Benefits:**

-   Safer code merges

-   Better peer reviews

-   Less firefighting after deploys

**Common misconceptions:**

-   "More rules = less agility" → Actually, it reduces chaos

-   "Only juniors write risky PRs" → Everyone does, occasionally

**How to get started:**

-   Set PR size limits (e.g., max 300 lines)

-   Flag missing tests or lint failures

-   Scan for secrets or bad patterns (with Snyk, GitHub Advanced Security)

-   Create a checklist for reviewers