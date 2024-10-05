import subprocess

def get_installed_apps():
    """Get a list of installed packages on the system."""
    result = subprocess.run(['dpkg', '--get-selections'], capture_output=True, text=True)
    installed_apps = [line.split()[0] for line in result.stdout.splitlines() if line.endswith('\tinstall')]
    return installed_apps

def get_base_apps(base_apps_file):
    """Get a list of applications from a base system file."""
    with open(base_apps_file, 'r') as f:
        base_apps = [line.strip() for line in f.readlines()]
    return base_apps

def compare_apps(installed_apps, base_apps):
    """Compare installed applications with base applications."""
    missing_from_base = set(installed_apps) - set(base_apps)
    missing_in_installed = set(base_apps) - set(installed_apps)
    
    return missing_from_base, missing_in_installed

def main(base_apps_file):
    installed_apps = get_installed_apps()
    base_apps = get_base_apps(base_apps_file)

    missing_from_base, missing_in_installed = compare_apps(installed_apps, base_apps)

    print("Missing from base system:")
    for app in missing_from_base:
        print(f"  - {app}")

    print("\nMissing in installed applications:")
    for app in missing_in_installed:
        print(f"  - {app}")

if __name__ == '__main__':
    base_apps_file = 'base_apps.txt'  # Change this to the path of your base apps list
    main(base_apps_file)
