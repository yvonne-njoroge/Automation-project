# tests/test_login.py
from pages.login_page import LoginPage

def test_login_success(driver):
    page = LoginPage(driver)
    page.load()
    page.login("student","Password123")
    assert "Logged In Successfully" in driver.page_source