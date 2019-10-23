# coding=utf-8

import wda
import time
import unittest

class MyTest(unittest.TestCase):

  def setUp(self):
    self.c = wda.Client("http://localhost:8100")
    self.s = self.c.session("com.wemomo.momoappdemo1")

  def test_living(self):
    #点击直播按钮
    self.s(name="item_live", className="Image").tap()


    #点击开播
    btns = self.s(className="Button").find_elements()
    btns[1].tap()

    #点击"开始直播"
    self.s(text=u"开始直播", className="StaticText").tap()

    #点击二级页“开始直播”
    self.s(name=u"开始直播", className="Button").tap()

    self.s(name="D",className="Button").tap()
    time.sleep(10)


  
  def tearDown(self):
    self.s.close()





if __name__ == "__main__":
  unittest.main()




