import unittest
from pathlib import Path
from pipelines.testers import test_user_visits, test_allowed_file


class TestUserVisits(unittest.TestCase):

    def test_test_user_visits(self):
        path = '\\test_data\\test_log.csv'
        BASE_DIR = Path(__file__).resolve(strict=True).parent
        PATH_DIR = (str(BASE_DIR) + path)
        user_info = test_user_visits(PATH_DIR)
        timestamp = user_info['timestamp']
        id_user = user_info['anonymous_id']
        banned = user_info['banned_user_time']
        self.assertEqual(id_user, '75c738cf-0841-42cf-939a-67e5f3a86325')
        self.assertEqual(timestamp, 1667233287)
        self.assertEqual(banned, 1667236887)


class TestFile(unittest.TestCase):

    def test_allowed_file(self):
        file = 'test-file.csv'
        test_allowed_file(file)
        message = "Test test_allowed_file value is not true"
        self.assertTrue(test_allowed_file(file), message)


if __name__ == 'main':
    unittest.main()



