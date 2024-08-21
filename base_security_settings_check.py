from abc import ABC, abstractmethod

from github import Github


class RepositoryContext:
    """ This class holds all the necessary repository and branch data. It is created once and then shared among all
     the security check classes."""

    def __init__(self, access_token, repo_name, branch_name="main"):
        self.github = Github(access_token)
        self.repo = self.github.get_repo(repo_name)
        self.branch_name = branch_name
        self.branch = self.repo.get_branch(branch_name)


class BaseSecurityCheck(ABC):
    """
        BaseSecurityCheck is an abstract base class that provides a common interface
        for all security checks on a GitHub repository.
    """
    def __init__(self, context: RepositoryContext):
        self.context = context

    @abstractmethod
    def check_security_config(self):  # checks security setting and prints status
        """Abstract method for checking security configuration"""
        pass

    @abstractmethod
    def fix_security_config(self):  # fixes security setting
        """Abstract method for fixing security configuration"""
        pass
