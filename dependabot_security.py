
from base_security_settings_check import BaseSecurityCheck


class DependabotManager(BaseSecurityCheck):
    """Manages Dependabot alerts and security updates."""

    def check_security_config(self):
        dependabot_alerts_enabled = self.context.repo.get_vulnerability_alert()
        dependabot_security_updates_enabled = self.context.repo.get_dependabot_security_updates_enabled()

        print("Dependabot Settings:")
        print(f"  - Alerts Enabled: {dependabot_alerts_enabled}")
        print(f"  - Security Updates Enabled: {dependabot_security_updates_enabled}")

        return dependabot_alerts_enabled, dependabot_security_updates_enabled

    def fix_dependabot_settings(self):
        dependabot_alerts_enabled, dependabot_security_updates_enabled = self.check_security_config()

        if not dependabot_alerts_enabled:
            self.context.repo.enable_vulnerability_alert()
            print("  - Dependabot alerts have been enabled.")

        if not dependabot_security_updates_enabled:
            self.context.repo.enable_dependabot_security_updates()
            print("  - Dependabot security updates have been enabled.")
