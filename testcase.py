# coding=utf-8

import unittest

class MyTest(unittest.TestCase):

  def setUp(self):
    print("---setUp---")

  def tearDown(self):
    print("---tearDown---")

  @unittest.skip("one skipping")
  def test_one(self):
    print("+++++++++one")

  def test_two(self):
    print("+++++++++two")

  @classmethod
  def setUpClass(cls):
    print("----set up cls----")

  @classmethod
  def tearDownClass(cls):
    print("----tear down cls----")


if __name__ == "__main__":
  #unittest.main()

  tests = [MyTest("test_one"), MyTest("test_two")]
  suite = unittest.TestSuite()
  suite.addTests(tests)

  runner = unittest.TextTestRunner()
  runner.run(suite)
