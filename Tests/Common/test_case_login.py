import pytest
import time
from Drivers.chrome_driver import get_chrome_driver
from Pages.Common.login_page import LoginPage
from Utils.config import Config
from Utils.logger import setup_logger

logger = setup_logger("TestLogin")

@pytest.fixture
def setup():
    driver = get_chrome_driver()
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()

def test_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    logger.info("Starting login test")
    login_page.enter_username(Config.USERNAME)
    login_page.enter_password(Config.PASSWORD)
    login_page.click_login()
    time.sleep(1)
    logger.info("Login test completed")
    # Add assertions to verify login success, e.g., check for a specific element after login
