from evolving.common_configuration import get_source_data_folder_absolute_path, get_target_folder_path


def CreateFullExcludingCounterExamplesTest(
target_test_run_schema_folder_path: str):
    source_data_folder_absolute_path = \
        get_source_data_folder_absolute_path()

    FullExcludingCounterExamplesTest_folder_name = \
        'FullExcludingCounterExamplesTest'

    # Create FullExcludingCounterExamplesTest folder

    target_test_folder_path = target_test_run_schema_folder_path + '\\' + FullExcludingCounterExamplesTest_folder_name
    os.mkdir(outroot)
