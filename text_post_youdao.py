import unittest
from post_youdao import *
from unittest import mock

class PostYoudaoText(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_get_ts(self):
        get_ts=mock.Mock(return_value='1586759501704')
        self.assertEqual('1586759501704', get_ts())

    def test_get_salt(self):
        get_salt=mock.Mock(return_value='15867595017047')
        self.assertEqual('15867595017047',get_salt())
    def test_get_sign(self):
        self.assertEqual('c40d36905b5e23c8ca0f21ddc885c6da',get_sign())
if __name__ == '__main__':
    unittest.main()
