from github import Github

from base_security_settings_check import BaseSecurityCheck

class BranchProtectionManager(BaseSecurityCheck):
    """ Manages branch protection rules."""

    def check_security_config(self):
        # Check branch protection settings
        protection = self.context.branch.get_protection()

        pr_reviews_required = protection.required_pull_request_reviews
        status_checks_required = protection.required_status_checks
        push_restrictions = protection.restrictions

        print(f"Pull Request Reviews Required: {pr_reviews_required is not None}")
        print(f"Status Checks Required: {status_checks_required is not None}")
        print(f"Push Restrictions: {push_restrictions is not None}")

        # Return protection status as a dictionary
        # dictionary-like object that contains the details of the protection rules currently enforced on the branch.
        return {
            "pr_reviews_required": pr_reviews_required is not None,
            "status_checks_required": status_checks_required is not None,
            "push_restrictions": push_restrictions is not None
        }


    def fix_security_config(self):
        # Get current protection settings
        protection = self.check_security_config()
        branch = self.context.branch

        # Fix pull request reviews requirement
        if not protection["pr_reviews_required"]:
            branch.edit_protection(required_approving_review_count=1, enforce_admins=True)
            print(f" Pull request reviews enabled with at least 1 approving review for {branch.name}.")

        # Fix status checks requirement
        if not protection["status_checks_required"]:
            branch.edit_protection(required_status_checks={'strict': True, 'contexts': []})
            #  the pull request must include the latest changes from the base branch before it can be merged.
            print(f" Status checks enabled with strict mode for {branch.name}.")

        # Fix push restrictions
        if not protection["push_restrictions"]:
            branch.edit_protection(restrictions={'users': [], 'teams': []})
            print(f"Push restrictions enabled for {branch.name}.")
