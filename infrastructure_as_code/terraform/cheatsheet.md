🧠 Terraform CLI Commands --- Cheat Sheet
=======================================

> "Treat Terraform like a chainsaw: powerful, but you better know what each button does."

* * * * *

🔧 **Everyday Commands**
------------------------

| Command | Purpose | Example |
| --- | --- | --- |
| `terraform init` | Initializes the directory, downloads providers | `terraform init` |
| `terraform validate` | Checks if your `.tf` files are syntactically valid | `terraform validate` |
| `terraform fmt` | Formats your files to standard style | `terraform fmt -recursive` |
| `terraform plan` | Shows a preview of what will change | `terraform plan -out=tfplan` |
| `terraform apply` | Applies the changes from your `.tf` files | `terraform apply` or `terraform apply tfplan` |
| `terraform destroy` | Destroys all resources defined in your config | `terraform destroy` |

* * * * *

🔍 **Working with State**
-------------------------

| Command | Purpose | Example |
| --- | --- | --- |
| `terraform state list` | Lists all tracked resources | `terraform state list` |
| `terraform state show <resource>` | Shows the attributes of a resource in state | `terraform state show aws_instance.web` |
| `terraform state rm <resource>` | Removes resource from state (without destroying it) | `terraform state rm aws_s3_bucket.broken` |
| `terraform state mv <old> <new>` | Renames or moves a resource in the state | `terraform state mv aws_s3_bucket.old aws_s3_bucket.new` |

* * * * *

📥 **Importing Existing Infra**
-------------------------------

| Command | Purpose | Example |
| --- | --- | --- |
| `terraform import` | Brings an existing resource into state | `terraform import aws_instance.web i-12345678` |

> 🚨 You must manually write the `.tf` code to match the imported resource.

* * * * *

🧪 **Debugging & Metadata**
---------------------------

| Command | Purpose | Example |
| --- | --- | --- |
| `terraform show` | Shows the current state or plan output | `terraform show` |
| `terraform providers` | Lists all required providers & their versions | `terraform providers` |
| `terraform version` | Displays the current Terraform version | `terraform version` |
| `terraform graph` | Outputs a visual dependency graph (DOT format) | `terraform graph | dot -Tsvg > graph.svg` |

* * * * *

⚠️ **Special Use / Edge Cases**
-------------------------------

| Command | Purpose | Example |
| --- | --- | --- |
| `terraform taint` | Marks a resource to be destroyed and recreated | `terraform taint aws_instance.web` |
| `terraform untaint` | Cancels the taint | `terraform untaint aws_instance.web` |
| `terraform refresh` | Refreshes the state file (deprecated-ish) | `terraform refresh` |

* * * * *

🏗 **Modules & Workspaces**
---------------------------

| Command | Purpose | Example |
| --- | --- | --- |
| `terraform get` | Downloads modules used in the configuration | `terraform get` |
| `terraform workspace list` | Lists all workspaces | `terraform workspace list` |
| `terraform workspace new <name>` | Creates a new workspace | `terraform workspace new staging` |
| `terraform workspace select <name>` | Switches workspace | `terraform workspace select prod` |

* * * * *

🧠 Tips for Interviews & Real Life
----------------------------------

-   Always `init` after changing backends or providers.

-   Use `plan -out=tfplan` before `apply` for safe reviews.

-   `state rm` ≠ destroy --- it only forgets.

-   NEVER edit the `.tfstate` file manually unless you're into stress-eating.

-   Learn `taint` for break-glass situations (e.g. an EC2 instance goes rogue).

-   Use `graph` + DOT if you want to impress someone with infrastructure art 🧠🎨