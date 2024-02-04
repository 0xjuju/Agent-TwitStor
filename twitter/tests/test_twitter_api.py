
import unittest

from twitter.twitter_api import Twitter


class TestTwitterApi(unittest.TestCase):
    def setUp(self):
        self.twitter = Twitter()

    def test_get_user(self):
        pass


if __name__ == "__main__":
    unittest.main()

