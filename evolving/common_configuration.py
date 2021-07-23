import os


def get_source_folder_path():
    source_folder_path = \
        'c:\\s'

    return \
        source_folder_path


def get_target_folder_path():
    target_folder_path = \
        'c:\\s'

    return \
        target_folder_path


def get_timestamp():
    timestamp = \
        '220859'

    return \
        timestamp

def get_source_data_folder_relative_path():
    source_data_folder_relative_path = \
        'Constructional'

    return \
        source_data_folder_relative_path


def get_source_data_folder_absolute_path():
    source_data_folder_absolute_path = \
        os.path.join(get_source_folder_path(), get_source_data_folder_relative_path())

    return \
        source_data_folder_absolute_path
