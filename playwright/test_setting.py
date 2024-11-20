import pytest
from playwright.sync_api import Page

from pages.base_page import access_longhorn # NOQA
from pages.base_page import go_to_setting_general
from pages.setting_page import SettingPage as setting

def test_setting_content(page: Page, access_longhorn):
    go_to_setting_general(page)
    assert page.locator(setting().allow_collecting_longhorn_usage_metrics).inner_text() \
        == "Allow Collecting Longhorn Usage Metrics:"

    assert page.locator(setting().allow_collecting_longhorn_usage_metrics_enable).is_checked() \
        is True

    assert "anticon-question-circle-o" in \
        page.locator(setting().allow_collecting_longhorn_usage_metrics_require_icon).get_attribute("class")
    
    assert page.locator(setting().allow_collecting_longhorn_usage_detail_description).inner_text() == \
        "Required.\n\nEnabling this setting will allow Longhorn to provide additional usage metrics to https://metrics.longhorn.io/. This information will help us better understand how Longhorn is being used, which will ultimately contribute to future improvements."
