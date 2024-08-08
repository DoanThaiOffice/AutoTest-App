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
    
}

appium_server_url = 'http://localhost:4723/wd/hub'
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

class TestAppium(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)
        logging.info("Start Appium")
        self.driver.implicitly_wait(10)

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

        # Login sucessful
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.Button[3]')
        self.wait_and_send_keys(AppiumBy.XPATH, '//android.widget.EditText[1]', "thaild.tt")
        self.wait_and_send_keys(AppiumBy.XPATH, '//android.widget.EditText[2]', "Thai12345")
        self.wait_and_click(AppiumBy.XPATH, '//android.view.View[@content-desc="ĐĂNG NHẬP"]')
        time.sleep(5)

        # TC_BUY_01
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[4]')
        time.sleep(3)
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Cần mua"]')

        # TC_BUY_02
        search_input = self.wait_and_click(AppiumBy.XPATH, '//android.widget.EditText')
        time.sleep(3)
        search_input.send_keys("Mua")
        time.sleep(2)
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.EditText')
        search_input.click()
        time.sleep(3)
        search_input.clear()

        # TC_BUY_03
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Khu vực"]')
        self.wait_and_click(AppiumBy.XPATH, '//android.view.View[@content-desc="Xã An Bình"]')
        time.sleep(2)
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Xã An Bình"]')
        time.sleep(2)
        self.wait_and_click(AppiumBy.XPATH, '//android.view.View[@content-desc="Khu vực"]')

        # TC_BUY_04
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Thể loại"]')
        self.wait_and_click(AppiumBy.XPATH, '//android.view.View[@content-desc="Ngành thủy sản"]')
        time.sleep(2)
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Ngành thủy sản"]')
        time.sleep(2)
        self.wait_and_click(AppiumBy.XPATH, '//android.view.View[@content-desc="Thể loại"]')
        time.sleep(2)

        # TC_BUY_05
        self.wait_and_click(AppiumBy.XPATH, '//android.view.View[@content-desc="[Mua] Măng Tre Mạnh Tông Giá bán: 80,000 VND / 1 cây Đăng bởi: Trần Thanh Quang Số lượng mua: 20 cây 0 quan tâm 1 bình luận Ngày đăng: 14:10 01/01/24"]')
        time.sleep(5)
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button')
        time.sleep(5)

        # TC_BUY_06
        self.wait_and_click(AppiumBy.XPATH, '//android.view.View[@content-desc="[Mua] Măng Tre Mạnh Tông Giá bán: 80,000 VND / 1 cây Đăng bởi: Trần Thanh Quang Số lượng mua: 20 cây 0 quan tâm 1 bình luận Ngày đăng: 14:10 01/01/24"]/android.widget.Button[1]')

        # TC_BUY_07
        self.wait_and_click(AppiumBy.XPATH, '//android.view.View[@content-desc="[Mua] Măng Tre Mạnh Tông Giá bán: 80,000 VND / 1 cây Đăng bởi: Trần Thanh Quang Số lượng mua: 20 cây 0 quan tâm 1 bình luận Ngày đăng: 14:10 01/01/24"]/android.widget.Button[2]')
        
        # TC_BUY_08
        self.wait_and_click(AppiumBy.XPATH, '//android.view.View[@content-desc="[Mua] Măng Tre Mạnh Tông Giá bán: 80,000 VND / 1 cây Đăng bởi: Trần Thanh Quang Số lượng mua: 20 cây 0 quan tâm 1 bình luận Ngày đăng: 14:10 01/01/24"]/android.view.View/android.view.View/android.widget.ImageView')
        self.wait_and_send_keys(AppiumBy.XPATH, '//android.widget.EditText',"Oke")
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button')

        # TC_BUY_09
        self.wait_and_click(AppiumBy.XPATH, '//android.view.View[@content-desc="[Mua] Măng Tre Mạnh Tông Giá bán: 80,000 VND / 1 cây Đăng bởi: Trần Thanh Quang Số lượng mua: 20 cây 0 quan tâm 1 bình luận Ngày đăng: 14:10 01/01/24"]/android.view.View/android.view.View/android.widget.ImageView')
        time.sleep(5)
        self.wait_and_click(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button')
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()
