import pytest
from Drivers.chrome_driver import get_chrome_driver
from Utils.config import Config

@pytest.fixture(scope="function")
def setup():
    driver = get_chrome_driver()
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()
