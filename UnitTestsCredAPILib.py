#! usr/bin/env python3
import unittest
import praw

from mycredentials import reddit_cred

class TestConnections(unittest.TestCase):

    def test_reddit(self):
        c = reddit_cred.get_cred_dict()
        try:
            reddit = praw.Reddit(client_id=c["client_id"], client_secret=c["client_secret"], user_agent=c["user_agent"],username=c["username"], password=c["password"])
            print("Successfully logged in as " + str(reddit.user.me()))
        except:
            reddit = None

        self.assertIsNotNone(reddit,"Could Not connect to Reddit with the given credentials. "
                                    "Check the mycredentials.py file")

if __name__ == '__main__':
    unittest.main()

