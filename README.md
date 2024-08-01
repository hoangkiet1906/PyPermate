# PyPermate
python3 -m venv venv
source venv/bin/activate

deactivate

pip install pytest

pytest
pytest -s xem log

Chạy tất cả các test case trong một file cụ thể:
pytest Test/test_login.py
Chạy một test case cụ thể trong file:
pytest Test/test_login.py::test_login
Chạy các test case được đánh dấu bằng marker:
pytest -m login
Chạy các test case với keyword expression:
pytest -k "test_login"

pip install allure-pytest
brew install allure

allure serve ./allure-results

allure generate allure-results -o allure-report
allure open allure-report


