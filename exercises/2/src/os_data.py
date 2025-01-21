
import sys
import pkg_resources

def main():
    # Get the Python version
    python_version = sys.version
    print(f"Python version is {python_version}")

    # Get installed packages and their versions
    print("\nInstalled packages:")
    installed_packages = sorted([(d.project_name, d.version) for d in pkg_resources.working_set])
    for package, version in installed_packages:
        print(f"{package} == {version}")

# Ensure the main function runs when the script is executed directly
if __name__ == "__main__":
    main()



