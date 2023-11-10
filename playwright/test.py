import pytest
from playwright.sync_api import sync_playwright, expect, Page

URL = "http://54.81.171.209"
VOLUME_NAME = "pvc-46569a7c-55c9-4863-af4d-d23d437849e0"
VOLUME_ROBUSTNESS = "//*[@id=\"root\"]/div/div/div/div[3]/div/div/div[2]/div/div[1]/div/div[2]/div/div[2]/span[2]"

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("\n=== test start")
    print("go to {}".format(URL))
    page.goto(URL)

    yield
    print("\n=== test complete")


def go_to_volume_page(page: Page):
    print("navigate to page Volume")
    page.get_by_role("link", name="icon: database Volume").click()


def test_run(page: Page):
    go_to_volume_page(page)
    examin_volume_info(page, VOLUME_NAME, "healthy")
    

def examin_volume_info(page: Page, volume_name, health):
    print("check volume {} is {}".format(volume_name, health))
    
    page.get_by_role("link", name=volume_name).click()
    page.wait_for_url("**/{}".format(volume_name))
    expect(page.get_by_text("{}".format(volume_name),exact=True)).to_be_visible()
    assert page.locator("xpath={}".format(VOLUME_ROBUSTNESS)).text_content().strip() == health
    
    page.go_back()
