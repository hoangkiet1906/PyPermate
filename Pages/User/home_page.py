from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.title_product_xpath = "//div[normalize-space()='{}']"
        self.button_add_to_cart_xpath = "//div[normalize-space()='{}']/ancestor::div[@class='inventory_item_label']/following-sibling::div[@class='pricebar']/button"

    def check_title_product(self, actual_title):
        title_xpath = (By.XPATH, self.title_product_xpath.format(actual_title))
        expected_title = self.driver.find_element(*title_xpath).text
        assert expected_title == actual_title, f"Expected title '{expected_title}', but got '{actual_title}'"

    def click_add_to_cart(self, actual_title):
        button_xpath = (By.XPATH, self.button_add_to_cart_xpath.format(actual_title))
        self.driver.find_element(*button_xpath).click()
