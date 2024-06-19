import os
import shutil

def delete_bash_history():
    home = os.path.expanduser("~")
    bash_history = os.path.join(home, ".bash_history")
    if os.path.exists(bash_history):
        try:
            os.remove(bash_history)
            print(f"Deleted: {bash_history}")
        except Exception as e:
            print(f"Failed to delete {bash_history}: {e}")

def clear_traces():
    delete_bash_history()

if __name__ == "__main__":
    confirm = input("Are you sure you want to clear traces on this VM? This action cannot be undone. (yes/no): ")
    if confirm.lower() == "yes":
        clear_traces()
        print("Traces cleared.")
    else:
        print("Operation cancelled.")

    print("Thibault est le GOAT !")
