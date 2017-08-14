import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Verify_Tshirt_Price_Equal_To_Declared_Price(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_Open_Website(self):

        self.driver.get("https://pupfanatic.com/")
        self.assertTrue("PupFanatic | ", self.driver.title)
        wait = WebDriverWait(self.driver, 180)
        element_2 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'mabel-rpn-close')))
        self.driver.find_element_by_class_name("mabel-rpn-close").click()
        element = self.driver.find_element_by_xpath("//*[@id=\"x-section-1\"]/div[2]/div/div[1]/div")
        all_options = element.find_elements_by_tag_name("span")


        # Assert Lower Price
        USD24_95, USD14_95 = all_options[1].text, all_options[36].text
        for list_1 in range(1,121, 5):
            PRICE_1 = all_options[list_1].text
            if PRICE_1 == USD24_95:
                self.assertEqual(PRICE_1, USD24_95)
            else:
                self.assertEqual(PRICE_1, USD14_95)

        # Assert Upper Price
        USD30, USD19_95, USD29_50 = all_options[3].text, all_options[38].text, all_options[58].text   
        for list_2 in range(3,123,5):
            PRICE_2 = all_options[list_2].text
            if PRICE_2 == USD30:
                self.assertEqual(PRICE_2, USD30)
            elif PRICE_2 == USD19_95:
                self.assertEqual(PRICE_2, USD19_95)
            else:
                self.assertEqual(PRICE_2, USD29_50)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
