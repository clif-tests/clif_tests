import os
from evolving.remove_targetted_folder import remove_targetted_folder_by_path


def remove_targetted_folders_from_scope_by_name(
        target_scope_root_folder: str,
        target_folder_name: str):
    for root, dirs, files in os.walk(target_scope_root_folder):
        for directory in dirs:
            if directory == 'target_folder_name':
                remove_targetted_folder_by_path(
                    os.path.join(root, directory))
