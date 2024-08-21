import subprocess


def simulate_direct_push():
    print("Simulating a direct push to the main branch without protection...")

    # Assuming in a Git repo, try pushing directly to the main branch
    try:
        subprocess.run(["git", "checkout", "main"], check=True)
        subprocess.run(["git", "commit", "--allow-empty", "-m", "Simulating unprotected commit"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("Direct push to main branch completed.")
    except subprocess.CalledProcessError as e:
        print(f"Error during git operations: {e}")


if __name__ == "__main__":
    simulate_direct_push()



