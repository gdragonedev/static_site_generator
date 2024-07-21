import os

from static_to_public import copy_static_recursive, clear_destination

def main():

    source = "../static/"
    destination = "../public/"

    # Debugging prints
    print(f"Source directory exists: {os.path.exists(source)}")
    print(f"Destination directory exists: {os.path.exists(destination)}")
    
    if not os.path.exists(source):
        print(f"Error: Source directory '{source}' does not exist.")
        return
    if not os.path.exists(destination):
        os.makedirs(destination)
        print(f"Created destination directory '{destination}'.")
    
    try:
        clear_destination(destination)
        copy_static_recursive(source, destination)
        print(f"Files copied from {source} to {destination} successfully...")
    except Exception as e:
        print(f"Files not copied, error: {e}")

if __name__ == "__main__":
    main()