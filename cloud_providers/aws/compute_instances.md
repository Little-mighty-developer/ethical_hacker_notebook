🛠️ EC2 & Fargate --- The Island's Workforce
==========================================

If your VPC is the island, then **EC2s are your workers** --- chefs, accountants, bouncers --- who run the actual applications. And **Fargate** is your invisible taskmaster that gets things done *without* you hiring and managing the workers yourself.

* * * * *

👷 What Is EC2?
---------------

**EC2 (Elastic Compute Cloud)** gives you resizable virtual machines (VMs) in the cloud.\
You control:

-   OS & software

-   CPU, memory, and disk size

-   Network rules

-   When to start, stop, reboot, terminate

It's like hiring a contractor: you choose what they do, where they work, and what tools they get.

* * * * *

🪢 Key EC2 Concepts
-------------------

| Concept | Think of it like... |
| --- | --- |
| **AMI (Amazon Machine Image)** | The uniform your worker shows up in 🧥 |
| **Instance Type** | How strong your worker is (CPU, RAM, etc.) 🏋️‍♀️ |
| **Key Pair** | Your secret handshake to log in securely 🤝 |
| **Elastic IP** | A permanent address for a worker 🏡 |
| **Security Group** | Who can talk to your worker (firewall rules) 🔐 |
| **User Data Script** | The morning checklist your worker runs on arrival 📝 |
| **EBS Volume** | The backpack your worker brings with files 🎒 |
| **Auto Scaling Group** | A manager that hires/fires workers based on need 📈 |

* * * * *

🐳 What Is Fargate?
-------------------

**Fargate** runs containers without you provisioning servers.\
It's perfect when you don't want to think about infrastructure at all.

You give it a **Docker container**, and it handles:

-   Scaling

-   Networking

-   Security

-   Billing by the second

It's like having a **robot butler** that appears, works, and disappears.

* * * * *

🌀 Load Balancers
-----------------

When traffic comes to the island, how do you decide **which worker gets the job**?

-   **ALB (Application Load Balancer)** -- Smart host: routes requests based on *content* (e.g. `/api` goes to X)

-   **NLB (Network Load Balancer)** -- Fast and low-level: routes by IP/port

-   **CLB (Classic Load Balancer)** -- Legacy: avoid unless required

* * * * *

🔄 EC2 Lifecycle
----------------

| Stage | What happens |
| --- | --- |
| Launch | Your worker (VM) comes online |
| Running | It's doing its job |
| Stop/Start | Goes offline/on again (preserves data) |
| Reboot | Restarts like a fresh morning 🛌 |
| Terminate | Fired --- gone forever ❌ |

* * * * *

🧠 When to Choose EC2 vs Fargate
--------------------------------

| Use Case | Go With... |
| --- | --- |
| Full control over OS & software | **EC2** |
| Simple container workloads | **Fargate** |
| GPU-heavy processing (e.g. ML) | **EC2** |
| Short-lived batch jobs | **Fargate** |
| Low-latency performance tuning | **EC2** |

* * * * *

🔐 EC2 Security
---------------

-   Use **IAM Roles for EC2** --- let instances access S3, DynamoDB, etc. *safely*

-   Enable **SSM Session Manager** instead of SSH keys

-   Restrict access with **Security Groups** and **NACLs**

* * * * *

⚡️ EC2 Cost Tips
----------------

-   Use **Spot Instances** for short-lived, interruptible work

-   Turn off test/dev instances overnight

-   Choose **Graviton** (ARM-based) instances for cost/performance

* * * * *

🤖 AI Workloads
---------------

-   EC2 **GPU Instances (e.g. p3, g4)** for training LLMs, image processing, etc.

-   **Fargate + Lambda** great for microservice-style AI pipelines

* * * * *

🧠 Thinking Questions
---------------------

-   Are you overprovisioning EC2s "just in case"?

-   Could Fargate simplify your CI/CD pipeline?

-   Have you reviewed auto-scaling & health check settings recently?

* * * * *

✅ Best Practices Checklist
--------------------------

-   Use **launch templates** for standardizing EC2 configs

-   Keep **user data scripts** versioned and tested

-   Enable **detailed CloudWatch metrics**

-   Use **Auto Scaling Groups** for high-availability apps

-   Replace SSH with **SSM access** wherever possible

-   Choose **Fargate** for lightweight, stateless apps


