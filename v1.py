import subprocess

def create_terraform_vars_file(region: str, environment: str, project_name: str) -> None:
    """Creates a Terraform variables file with the specified inputs."""
    with open("terraform.tfvars", "w") as f:
        f.write(f"""
        region = "{region}"
        environment = "{environment}"
        project_name = "{project_name}"
        """)

def initialize_terraform() -> None:
    """Initializes Terraform in the current directory."""
    subprocess.run(["terraform", "init"])

def plan_terraform_changes() -> None:
    """Generates a Terraform plan file with the planned infrastructure changes."""
    subprocess.run(["terraform", "plan", "-out=terraform.plan"])

def apply_terraform_changes() -> None:
    """Applies the Terraform plan and deploys the infrastructure."""
    subprocess.run(["terraform", "apply", "terraform.plan"])

if __name__ == "__main__":
    # Define inputs
    region = input("Enter the AWS region: ")
    environment = input("Enter the environment (e.g. dev, prod): ")
    project_name = input("Enter the project name: ")

    # Create Terraform variables file
    create_terraform_vars_file(region, environment, project_name)

    # Initialize Terraform
    initialize_terraform()

    # Plan Terraform changes
    plan_terraform_changes()

    # Apply Terraform changes
    apply_terraform_changes()
