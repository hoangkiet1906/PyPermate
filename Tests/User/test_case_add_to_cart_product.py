import time
import allure
from Pages.User.home_page import HomePage
from Utils.logger import setup_logger

logger = setup_logger("TestAddToCartProduct")

@allure.feature('Add To Cart Feature')
@allure.story('Valid Add To Cart')
def test_add_to_cart_product(login):
    driver = login
    home_page = HomePage(driver)
    logger.info("Starting add to cart test")
    home_page.check_title_product("Sauce Labs Backpack")
    logger.info("Product correct")
    home_page.click_add_to_cart("Sauce Labs Backpack")
    time.sleep(1)
    logger.info("Add to cart test completed")
