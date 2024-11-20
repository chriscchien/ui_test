from playwright.sync_api import sync_playwright, expect, Page
import os
import pytest

URL = 'http://10.76.102.215/'

@pytest.fixture(scope="function", autouse=True)
def access_longhorn(page: Page):
    print("\n=== test start")
    print("go to {}".format(URL))
    page.goto(URL)

    yield
    print("\n=== test complete")

def go_to_setting_general(page: Page):
    page.get_by_text("Setting").click()
    page.get_by_role("link", name="icon: setting General").click()
    