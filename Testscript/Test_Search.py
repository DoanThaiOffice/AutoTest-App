from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import time
import unittest
import logging

logging.basicConfig(level=logging.INFO)

capabilities = {
    
}

appium_server_url = 'http://localhost:4723/wd/hub'

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

class TestAppium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(command_executor=appium_server_url,
                                       options=capabilities_options)
        logging.info("Start Appium")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
            logging.info("End Appium")
       
    def test_find_nongnghiepphugiao(self):
        logging.info("Finding the 'Phú Giáo Xanh' element")

        # Login successful
        self.click_element(AppiumBy.XPATH, 
            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button[3]')
        time.sleep(2)

        bAccount = self.find_element(AppiumBy.XPATH, 
            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')
        bPassword = self.find_element(AppiumBy.XPATH, 
            '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')
        bLogin = self.find_element(AppiumBy.XPATH, 
            '//android.view.View[@content-desc="ĐĂNG NHẬP"]')
        
        self.input_text(bAccount, "thaild.tt")
        time.sleep(2)
        self.input_text(bPassword, "Thai12345")
        time.sleep(2)
        bLogin.click()
        time.sleep(2)

        # Perform search tests
        search_test_cases = [
            ("Mua", 3),
            ("Dưa", 2),
            ("Dừa", 2),
            ("Dua", 3),
            ("12345", 2),
            ("abcxyz", 2),
            ("", 2),
            ("@#%", 1),
            ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 1),
            (" Dưa", 1),
            ("   ", 1)
        ]

        for query, delay in search_test_cases:
            self.perform_search(query, delay)

    def click_element(self, by, value):
        try:
            element = self.find_element(by, value)
            if element:
                element.click()
        except Exception as e:
            logging.error(f"Error clicking element {value}: {e}")

    def find_element(self, by, value):
        try:
            element = self.driver.find_element(by=by, value=value)
            logging.info(f"Found element: {value}")
            return element
        except Exception as e:
            logging.error(f"Error finding element {value}: {e}")
            return None
    
    def input_text(self, element, text):
        try:
            if element:
                element.click()
                element.clear()
                element.send_keys(text)
        except Exception as e:
            logging.error(f"Error inputting text '{text}' in element: {e}")
    
    def perform_search(self, query, delay):
        try:
            bSearchBox = self.find_element(AppiumBy.XPATH, 
                '//android.widget.ScrollView/android.view.View[4]')
            if bSearchBox:
                bSearchBox.click()
            bBuy = self.find_element(AppiumBy.XPATH, 
                '//android.widget.ImageView[@content-desc="Cần bán"]')
            if bBuy:
                bBuy.click()
            bKeySB = self.find_element(AppiumBy.XPATH, 
                '//android.widget.EditText')
            if bKeySB:
                self.input_text(bKeySB, query)
                time.sleep(delay)
                bSearch = self.find_element(AppiumBy.XPATH, 
                    '//android.widget.Button[@content-desc="Tìm kiếm"]')
                if bSearch:
                    bSearch.click()
                    time.sleep(2)
        except Exception as e:
            logging.error(f"Error performing search with query '{query}': {e}")

if __name__ == '__main__':
    unittest.main()
