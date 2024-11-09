#!/usr/bin/python3
# v1.0   Ramsey + AI 

import subprocess

def get_installed_apps():
    """Get a list of installed packages on the system."""

    command = "apt list --installed | awk -F'/' '{print $1}' | grep -v 'Listing...'"
    result  = subprocess.run(command, shell=True, text=True, capture_output=True)

    # Split the output into a list
    installed_packages = result.stdout.splitlines()

    return installed_packages

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

    # print(f"\n\nDEBUG: Installed Apps: {installed_apps}")
    # print(f"\n\nDEBUG: Base Apps: {base_apps}")

    missing_from_base, missing_in_installed = compare_apps(installed_apps, base_apps)

    print("\nMissing from base system:")
    for app in sorted(missing_from_base):
        print(f"  - {app}")

    print("\nMissing in installed applications:")
    for app in sorted(missing_in_installed):
        print(f"  - {app}")

if __name__ == '__main__':

    # to refresh this BASELINE, run this command
    #  apt list --installed | awk -F'/' '{print $1}' | grep -v 'Listing...'
    base_apps_file = 'known_default_mint_21_base_apps_apt_list.txt'  # Change this to the path of your base apps list
    main(base_apps_file)
