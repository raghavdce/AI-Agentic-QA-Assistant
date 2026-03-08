import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        yield browser
        browser.close()

@pytest.fixture(scope="module")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

def test_successful_login(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("input[data-test='username']", "standard_user")
    page.fill("input[data-test='password']", "secret_sauce")
    page.click("input[data-test='login-button']")
    assert page.locator(".title").is_visible()
    assert page.locator("h4").is_visible()

def test_unsuccessful_login_invalid_credentials(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("input[data-test='username']", "invalid_user")
    page.fill("input[data-test='password']", "wrong_password")
    page.click("input[data-test='login-button']")
    assert page.locator("h3[data-test='error']").is_visible()

def test_unsuccessful_login_empty_credentials(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("input[data-test='username']", "")
    page.fill("input[data-test='password']", "")
    page.click("input[data-test='login-button']")
    assert page.locator("h3[data-test='error']").is_visible()