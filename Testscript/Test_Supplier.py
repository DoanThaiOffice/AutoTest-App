import time
import unittest
import logging
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO)

capabilities = {
    'platformName': 'Android',
    'platformVersion': '14',
    'automationName': 'UiAutomator2',
    'deviceName': 'RFCT80P643Y',
    'appPackage': 'vn.binhduong.nongnghiepphugiao',
    'appActivity': 'vn.binhduong.nongnghiepphugiao.MainActivity'
}

appium_server_url = 'http://localhost:4723/wd/hub'
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

class TestAppium(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)
        logging.info("Start Appium")
        self.driver.implicitly_wait(10)  # Implicit wait for 10 seconds

    def tearDown(self):
        if self.driver:
            self.driver.quit()
            logging.info("End Appium")

    def wait_and_click(self, by, locator, timeout=20):
        logging.info(f"Waiting for element by {by} with locator: {locator}")
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, locator))
        )
        logging.info(f"Clicking on element by {by} with locator: {locator}")
        element.click()
        return element

    def wait_and_send_keys(self, by, locator, text, timeout=20):
        logging.info(f"Waiting for element by {by} with locator: {locator} to send keys")
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, locator))
        )
        element.click()
        logging.info(f"Sending keys to element by {by} with locator: {locator}")
        element.send_keys(text)
        return element

    def test_find_nongnghiepphugiao(self):
        logging.info("Starting test_find_nongnghiepphugiao")
        
        # Login successful
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.Button[3]')
        self.wait_and_send_keys(AppiumBy.XPATH, '//android.widget.EditText[1]', "thaild.tt")
        self.wait_and_send_keys(AppiumBy.XPATH, '//android.widget.EditText[2]', "Thai12345")
        self.wait_and_click(AppiumBy.XPATH, '//android.view.View[@content-desc="ĐĂNG NHẬP"]')
        time.sleep(5)

        # TC_Supplier_01
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[4]')
        time.sleep(3)  # Adding sleep to avoid quick interactions
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Đơn vị cung ứng"]')

        # TC_Supplier_02
        search_input = self.wait_and_click(AppiumBy.XPATH, '//android.widget.EditText')
        time.sleep(3)
        search_input.send_keys("bưởi Ông Phong")
        time.sleep(2)
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Tìm kiếm"]')
        search_input.click()
        time.sleep(3)
        search_input.clear()

        # TC_Supplier_03
        search_input = self.wait_and_click(AppiumBy.XPATH, '//android.widget.EditText')
        time.sleep(3)
        search_input.send_keys("Sầu riêng")
        time.sleep(2)
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Tìm kiếm"]')
        search_input.click()
        time.sleep(3)
        search_input.clear()

        # TC_Supplier_04
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button[1]')
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Xã An Bình"]')
        time.sleep(2)
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button[1]')
        time.sleep(2)
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Khu vực"]')
        time.sleep(2)

        # TC_Supplier_05
        search_input = self.wait_and_click(AppiumBy.XPATH, '//android.widget.EditText')
        time.sleep(3)
        search_input.send_keys("Quang")
        time.sleep(2)
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Tìm kiếm"]')
        search_input.click()
        time.sleep(3)
        search_input.clear()

        # TC_Supplier_06
        search_input = self.wait_and_click(AppiumBy.XPATH, '//android.widget.EditText')
        time.sleep(3)
        search_input.send_keys("0833976669")
        time.sleep(2)
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Tìm kiếm"]')
        search_input.click()
        time.sleep(3)
        search_input.clear()

        # TC_Supplier_07
        search_input = self.wait_and_click(AppiumBy.XPATH, '//android.widget.EditText')
        time.sleep(3)
        search_input.send_keys("abcxyz")
        time.sleep(2)
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Tìm kiếm"]')
        search_input.click()
        time.sleep(3)
        search_input.clear()

        # TC_Supplier_08
        search_input = self.wait_and_click(AppiumBy.XPATH, '//android.widget.EditText')
        time.sleep(3)
        search_input.send_keys(" ")
        time.sleep(2)
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Tìm kiếm"]')
        search_input.click()
        time.sleep(3)
        search_input.clear()

        # TC_Supplier_09
        search_input = self.wait_and_click(AppiumBy.XPATH, '//android.widget.EditText')
        time.sleep(3)
        search_input.send_keys("@#%")
        time.sleep(2)
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Tìm kiếm"]')
        search_input.click()
        time.sleep(3)
        search_input.clear()

if __name__ == '__main__':
    unittest.main()