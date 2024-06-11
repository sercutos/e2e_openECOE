from playwright.sync_api import Page
import pytest

# https://www.saucedemo.com/
# standard_user / secret_sauce
# https://trace.playwright.dev/
#pytest .\test_1.py 
@pytest.mark.only_browser("chromium") #ejecuta test_title solo en chrome
#@pytest.mark.skip_browser("chromium") # no lo ejecuta en chrome
def test_title(page: Page):    
    page.goto("/")
    assert page.title() == "Swag Labs"

def test_inventory_page(page: Page):
    page.goto("/inventory.html")
    assert page.inner_text("H3") == "Epic sadface: You can only access '/inventory.html' when you are logged in."