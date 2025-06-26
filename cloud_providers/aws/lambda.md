🧞‍♂️ AWS Lambda --- Your Island's Magical Elf
============================================

Imagine you clap your hands and *poof!* an elf appears, performs a task, and disappears. That's **AWS Lambda** --- a **serverless compute service** that runs your code **only when needed**, charging you **only for the time it runs**.

No servers. No maintenance. Just magic.

* * * * *

🧠 What Is Lambda?
------------------

Lambda lets you run **code without provisioning servers**.

You define:

-   **Trigger** (what calls it)

-   **Code** (what it does)

-   **Permissions** (what it can access)

* * * * *

🪄 How It Works
---------------

1.  **You write a function** (in Python, Node.js, Go, Java, etc.)

2.  **You define a trigger** (e.g., S3 upload, API Gateway call, cron job)

3.  **Lambda runs the function**, scales automatically, and shuts down when done.

🪶 *You only pay for compute time used, down to the millisecond.*

* * * * *

🔌 Lambda Triggers (What Starts the Elf)
----------------------------------------

| Source | Example Use Case |
| --- | --- |
| **S3** | Run image resizer on file upload |
| **API Gateway** | Backend for serverless web API |
| **EventBridge** | Scheduled tasks (e.g., clean temp files) |
| **DynamoDB** | React to table changes |
| **CloudWatch Logs** | Alert on error patterns |

* * * * *

🧙🏽 What Makes Lambda Magical?
-------------------------------

| Feature | Description |
| --- | --- |
| **Stateless** | Each invocation is isolated |
| **Automatic scaling** | Handles 1 or 10,000 events seamlessly |
| **Integrated logging** | Built-in logs via CloudWatch |
| **Environment variables** | Securely configure secrets/paths |
| **Layers** | Share libraries across functions |
| **Provisioned concurrency** | Keep Lambdas warm for zero-latency apps |

* * * * *

🛡️ IAM and Lambda
------------------

Lambda needs **permissions to act on your behalf**.

-   Assign an **IAM Role to the function**

-   Example: "This function can read from S3 and write to DynamoDB"

Use the **principle of least privilege** --- only grant what's truly needed.

* * * * *

📦 Packaging Lambda Code
------------------------

| Option | Used When... |
| --- | --- |
| Inline code editor | For tiny scripts or quick tests |
| Zip archive upload | For most functions + dependencies |
| Lambda container | For complex apps or custom runtimes (Docker) |

* * * * *

🧊 Cold Starts & Warm Starts
----------------------------

-   **Cold start**: Lambda spins up from scratch --- slight delay (~100--500ms)

-   **Warm start**: Lambda reuses a previous instance --- super fast

Use **provisioned concurrency** if latency matters.

* * * * *

🔐 Security Tips
----------------

-   Use **Secrets Manager** or **Parameter Store** for sensitive info

-   Set **timeouts** to avoid runaway bills

-   Monitor with **CloudWatch Alarms** and **X-Ray tracing**

* * * * *

📈 Monitoring
-------------

-   CloudWatch for **logs and metrics**

-   AWS X-Ray for **performance tracing**

-   Use **custom metrics** if you need deeper insight

* * * * *

🧠 Thinking Questions
---------------------

-   Do you have any cron jobs or one-off scripts that could be Lambdas?

-   Are you using Lambda for glue between AWS services?

-   Have you split monolithic Lambdas into focused single-purpose ones?

* * * * *

✅ Best Practices Checklist
--------------------------

-   Keep functions single-purpose and under 10 seconds where possible

-   Use **layers** for shared dependencies

-   Use **provisioned concurrency** for latency-sensitive apps

-   Log intelligently (no print spam!)

-   Set **tight IAM roles**

-   Monitor costs and timeouts