import unittest
from post_youdao import *
from unittest import mock

class PostYoudaoText(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_get_ts(self):
        # import time
        # t = time.time()
        # ts = str(int(round(t * 1000)))
        # print(ts)
        get_ts=mock.Mock(return_value='1586759501704')
        self.assertEqual('1586759501704', get_ts())

if __name__ == '__main__':
    unittest.main()
