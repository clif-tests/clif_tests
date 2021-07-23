
def remove_targetted_folders_from_scope_by_name(
        target_scope_root_folder: str,
        target_folder_name: str):

    for root, dirs, files in os.walk(target_scope):
        for dir in dirs:
            if dir == 'target_folder_name' :
                remove_targetted_folder_by_path(
                    os.path.join(root,dir))