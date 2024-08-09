import allure
from Utils.logger import setup_logger

logger = setup_logger("TestLogin")

@allure.feature('Login Feature')
@allure.story('Valid Login')
def test_login(login):
    driver = login
