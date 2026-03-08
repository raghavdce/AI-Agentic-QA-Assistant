import pytest
from playwright.sync_api import sync_playwright

def test_successful_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/v1/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        assert page.is_visible("text=success message")  # Replace with actual success message selector
        assert page.url == "https://www.saucedemo.com/v1/dashboard"  # Replace with actual dashboard URL
        browser.close()

def test_unsuccessful_login_invalid_credentials():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/v1/")
        page.fill("#user-name", "invalid_user")
        page.fill("#password", "wrong_password")
        page.click("#login-button")
        assert page.is_visible("text=Username and password do not match any user in this service")  # Replace with actual error message selector
        browser.close()

def test_unsuccessful_login_empty_credentials():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/v1/")
        page.fill("#user-name", "")
        page.fill("#password", "")
        page.click("#login-button")
        assert page.is_visible("text=Username is required")  # Replace with actual error message selector
        assert page.is_visible("text=Password is required")  # Replace with actual error message selector
        browser.close()