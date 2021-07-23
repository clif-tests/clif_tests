import shutil


def remove_targetted_folder_by_path(
            target_folder_path: str):
    shutil.rmtree(
        target_folder_path)

