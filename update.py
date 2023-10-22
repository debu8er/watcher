import os
import git

def update_project(branch_name):
    try:
        # Get the current working directory, which is the project directory
        local_dir = os.getcwd()

        repo = git.Repo(local_dir)

        # Fetch the latest changes from the remote repository
        origin = repo.remote()
        origin.fetch()

        # Check out the branch you want to update
        repo.git.checkout(branch_name)

        # Pull the latest changes from the branch
        repo.git.pull(origin, branch_name)

        print("Project has been updated successfully using GitPython.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    branch_name = "main"  # Change this to the branch you want to update from

    update_project(branch_name)
