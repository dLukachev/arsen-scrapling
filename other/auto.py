from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(
        chromium_sandbox=False,
        channel="chrome",
        headless=False,
    )

    context = browser.new_context(storage_state="sadovod.json")

    page = context.new_page()

    page.goto("https://catalog-sadovod.ru/")

    # ТУТ СОХРАНЧИК
    context.storage_state(path="sadovod.json")

    input("Нажми любую клавишу для выхода...")