import os
from pathlib import Path
from process import Process_Log
from testers import test_allowed_file, test_user_visits
from load import sink_file

UPLOAD_FOLDER = '\\data\\'
BASE_DIR = Path(__file__).resolve(strict=True).parent
PATH_DIR = (str(BASE_DIR) + UPLOAD_FOLDER)
files = os.listdir(PATH_DIR)
for file in files:
    if test_allowed_file(file):
        test_user_visits(PATH_DIR + file)
        chunked_list = sink_file(PATH_DIR + file)
        process_log = Process_Log(chunked_list)
        print(process_log.campaign())
        print(process_log.source())
        print(process_log.medium())

    else:
        print('The file is not in .csv format')

