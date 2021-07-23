import os

from evolving.common_configuration import get_target_folder_path
from evolving.test_runs.orchestrate_test_run_full_excluding_counter_examples import \
    CreateFullExcludingCounterExamplesTest


def orchestrate_test_run_schema_trs001():
    test_run_schema_trs00_folder_name = \
        'TRS001'

    target_folder_path = \
        get_target_folder_path()

    # Create test_run_schema folder
    target_test_run_schema_folder_path = target_folder_path + '\\' + test_run_schema_trs00_folder_name
    os.mkdir(target_test_run_schema_folder_path)


CreateFullExcludingCounterExamplesTest(
    target_test_run_schema_folder_path)
