import re
from playwright.sync_api import Playwright, sync_playwright, expect



def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://test-openecoe.umh.es/")
    page.goto("https://test-openecoe.umh.es/login?returnUrl=%2Fecoe")
    page.get_by_placeholder("Correo electrónico").click()
    page.get_by_placeholder("Correo electrónico").fill("sergio.cubero@uv.es")
    page.get_by_placeholder("Contraseña").click()
    page.get_by_placeholder("Contraseña").fill("ecoe20jornada")
    page.get_by_role("button", name="Iniciar sesión").click()
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)