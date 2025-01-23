
import sys
import pkg_resources
import pandas as pd
import matplotlib.pyplot as plt
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))


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


df = pd.read_csv("athlete_events.csv")

test = df["Team"].value_counts().reset_index()
test_top = test.head(10)


fig, ax = plt.subplots(1, figsize=(12, 6))
ax.bar(x = test_top["Team"], height = test_top["count"])
ax.set_ylabel("Antal tävlande")
ax.set_xlabel("Land")
ax.set_title("Top 10 nationer för antal tävlande i OS historien")

plt.savefig("top_10nationer.jpeg", format = "jpeg", dpi = 300)

plt.show()

print("Nu är ploten skapad")



# classes = df["Team"].value_counts().reset_index()
# classes




