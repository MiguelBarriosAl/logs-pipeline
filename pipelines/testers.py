import csv

LIMIT_TIME = 5 * 60
BANNED_TIME = 60 * 60
UPLOAD_FOLDER = 'data/'
ALLOWED_EXTENSIONS = {'csv'}


def test_allowed_file(filename: str):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def test_out_of_order(init_log: int, pre_log: int):
    return pre_log < init_log


def test_user_visits(path: str):
    with open(path, "r") as file:
        reader_csv = csv.reader(file, delimiter=";")
        next(reader_csv)
        chunked_list = list(reader_csv)
    count = 0
    for n in range(len(chunked_list[0])):
        user = chunked_list[n][1]
        timestamp = int(chunked_list[n][0])
        limit_time = timestamp + LIMIT_TIME
        for logs in chunked_list:
            if user in logs and timestamp < limit_time and timestamp and count < 10:
                count += 1
            elif count >= 10:
                banned = timestamp + BANNED_TIME
                return {
                    "timestamp": timestamp,
                    "anonymous_id": user,
                    "banned_user_time": banned}
