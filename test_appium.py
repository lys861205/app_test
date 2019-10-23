#!/usr/bin/python3

# coding=utf-8

from appium import webdriver

desired_capabilities = {}
desired_capabilities["platformVersion"] =  "11.0"
desired_capabilities["deviceName"] =  "iPhone 8"
desired_capabilities["automationName"] =  "XCUITest"
desired_capabilities["udid"] =  "34855823045694534883"
desired_capabilities["bundleId"] =  "com.wemomo.momoappdemo1"
desired_capabilities["platformName"] =  "iOS"

def start_living():
  try:
    print(desired_capabilities)
    #driver = webdriver.Remote("http://10.129.148.209:4723/wd/hub", desired_capabilities)
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
    print(driver.session)
    driver.quit()
  except Exception as err:
    print(err)

if __name__ == "__main__":
  try:
    print("testing appium...")
    start_living()
  except KeyboardInterrupt:
    print("program is quit")
  
  

