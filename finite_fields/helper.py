from unittest import TestSuite, TextTestRunner


def run(rest):
    suite = TestSuite()
    suite.addTest(test)
    TextTestRunner().run(suite)