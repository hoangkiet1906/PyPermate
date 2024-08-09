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
Debug
pytest -k "test_add_to_cart_product" --pdb -s

n (next): Thực thi câu lệnh tiếp theo trong cùng một hàm.
s (step): Bước vào hàm gọi.
c (continue): Tiếp tục thực thi mã cho đến khi gặp breakpoint tiếp theo.
q (quit): Thoát khỏi debugger và dừng chương trình.
p <biến>: In giá trị của biến.
l (list): Hiển thị mã nguồn xung quanh dòng hiện tại.


pip install allure-pytest
brew install allure

allure serve ./allure-results

pytest --alluredir=allure-results
allure generate allure-results -o allure-report
allure open allure-report

git pull origin main
git merge main


