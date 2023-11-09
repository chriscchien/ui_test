import pytest
from playwright.sync_api import sync_playwright, expect, Page

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    
    print("before the test runs")

    # Go to the starting url before each test.
    page.goto("http://18.206.190.244/")

    yield
    
    print("after the test runs")
    print("after the test runs")
    print("after the test runs")


def test_run(page: Page):
    
    
    page.get_by_role("link", name="icon: database Volume").click()

    examin_volume_info(page, "vol1", "Health", "ReadWriteOnce")
    examin_volume_info(page, "vol2", "Health", "ReadWriteOnce")
    examin_volume_info(page, "vol3", "Health", "ReadWriteOnce")
    examin_volume_info(page, "vol4", "Health", "ReadWriteOnce")
    examin_volume_info(page, "vol5", "Health", "ReadWriteOnce")

def examin_volume_info(page: Page, volume_name, health, access_mode):

    page.get_by_role("link", name=volume_name).click()
    page.wait_for_url("**/{}".format(volume_name))
    
    expect(page.get_by_text("{}".format(volume_name),exact=True)).to_be_visible()
    

    page.go_back()
