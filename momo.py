# coding=utf-8

import wda
import time
import unittest

class MyTest(unittest.TestCase):

  def setUp(self):
    try:
      self.c = wda.Client("http://localhost:8100")
      self.s = self.c.session("com.wemomo.momoappdemo1")
    except Exception as err:
      print(err)

  def test_living(self):
    try:
      #点击直播按钮
      self.s(name="item_live", className="Image").tap()

      #点击开播
      btns = self.s(className="Button").find_elements()
      btns[1].tap()

      #点击"开始直播"
      elems = self.s(className="StaticText").find_elements()
      for e in elems:
        if e.text == u"开始直播":
          e.tap()
          break

      #点击二级页“开始直播”
      elems = self.s(name="", className="Button").tap()
    except AttributeError as err:
      print(err)
  
  def tearDown(self):
    try:
      self.s.close()
    except AttributeError as err:
      print(err)
    
if __name__ == "__main__":
  unittest.main()




