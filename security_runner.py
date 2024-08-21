from base_security_settings_check import RepositoryContext
from branch_protection import BranchProtectionManager
from dependabot_security import DependabotManager


class SecurityCheckRunner:
    def __init__(self, checks):
        self.checks = checks

    def run_checks(self):
        print("Running all security checks...")
        for check in self.checks:
            check.check_security_config()

    def run_fixes(self):
        print("Running all security fixes...")
        for check in self.checks:
            check.fix_security_config()


if __name__ == "__main__":
    ACCESS_TOKEN = "personal_access_token"
    REPO_NAME = "username/repository"
    BRANCH_NAME = "main"

    # Create the repository context
    context = RepositoryContext(ACCESS_TOKEN, REPO_NAME, BRANCH_NAME)

    # Initialize security checks with the shared context
    checks = [
        BranchProtectionManager(context),
        SecretsExposureManager(context),
        DependabotManager(context)
    ]

    # Run all checks and fixes
    security_runner = SecurityCheckRunner(checks)
    security_runner.run_checks()
    security_runner.run_fixes()
