from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'UEEDU18424003423'
desired_caps['appPackage'] = 'com.twitter.android'
desired_caps['appActivity'] = '.StartActivity'
desired_caps['autoGrantPermissions'] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

driver.implicitly_wait(5)
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]').click()
driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="New Tweet"]').click()
tweet_box = driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="Edit Tweet 1 of 1"]/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText')
tweet_box.clear()
tweet_box.send_keys("Hello world! #SentFromAppium")
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.Button').click()

