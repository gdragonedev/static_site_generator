import os, shutil

def copy_static_recursive(source, destination):
    if not os.path.exists(source):
        raise ValueError(f"Invalid source: path doesn't exist: {source}")
    if not os.path.exists(destination):
        raise ValueError(f"Invalid destination: path doesn't exist: {destination}")
    
    for path_item in os.listdir(source):
        source_file_path = os.path.join(source, path_item)
        destination_file_path = os.path.join(destination, path_item)
        if os.path.isfile(source_file_path):
            print(f"Copying '{source_file_path}' to '{destination_file_path}'")
            shutil.copy(source_file_path, destination_file_path)
        else:
            os.makedirs(destination_file_path, exist_ok=True)
            copy_static_recursive(source_file_path, destination_file_path)

    
#ensure destination dir is empty before copying static
def clear_destination(destination):
    for path_item in os.listdir(destination):
        file_path = os.path.join(destination, path_item)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print (f"Failed to delete {file_path}. Error: {e}")

    if len(os.listdir(destination)) == 0:
        print(f"Destinaton dir ({destination}) is empty, preparing to add content...")
    else:
        raise Exception(f"Destination dir ({destination}) NOT emptied, cannot proceed")