# import json
# import subprocess


# GIT_BASH_DIR = "D:\Software\Git\git-bash.exe"
# #Read form Json
# with open("config.json", "r") as file:
#     config = json.load(file)

# #Show names to the user
# for i, option in enumerate(config, start=1):
#     print(f"{i}. {option['name']}")

# #Ask user for input
# selected = int(input("Select workspace:"))


# #Store it as object 
# selected_item = config[selected - 1]
# #open the path
# path_of_selected_thing = selected_item["path"]
# launch_of_selected_thing = selected_item["launch"]

# subprocess.run(
#     [GIT_BASH_DIR, "-c", f"{launch_of_selected_thing} {path_of_selected_thing}"]
# )
# #idea.bat


import json
import subprocess

# Read config
with open("config.json", "r") as file:
    config = json.load(file)

# Display options
for i, option in enumerate(config, start=1):
    print(f"{i}. {option['name']}")

# Handle user input safely
try:
    selected = int(input("Select workspace: "))
    selected_item = config[selected - 1]
except (ValueError, IndexError):
    print("Invalid selection.")
    exit(1)

path = selected_item["path"]
launch = selected_item["launch"]

# Launch independently without keeping terminal open
subprocess.Popen(
    [launch, path],
    creationflags=subprocess.DETACHED_PROCESS,
    shell=True
)

print(f"Launching {selected_item['name']}...")