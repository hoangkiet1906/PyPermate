import pytest
import time
from Drivers.chrome_driver import get_chrome_driver
from Pages.Common.login_page import LoginPage
from Utils.config import Config
from Utils.logger import setup_logger

logger = setup_logger("TestSetup")

@pytest.fixture(scope="function")
def setup():
    # Tạo đối tượng driver
    driver = get_chrome_driver()
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login(setup):
    driver = setup
    login_page = LoginPage(driver)
    logger.info("Starting login")
    login_page.enter_username(Config.USERNAME)
    login_page.enter_password(Config.PASSWORD)
    login_page.click_login()
    time.sleep(1)  # Chờ để đảm bảo đăng nhập hoàn tất
    logger.info("Login completed")
    yield driver
    # Optional: Nếu bạn cần đăng xuất sau khi test xong, bạn có thể thêm mã đăng xuất ở đây
    # Example:
    # login_page.logout() # Phương thức giả định để đăng xuất
    # logger.info("Logout completed")
