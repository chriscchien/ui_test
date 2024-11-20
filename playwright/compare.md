# Playwright and Selenium

## Ease of Setup
**Selenium**
-   Requires manual setup of browsers and WebDriver binaries.
-   More effort needed to manage driver versions compatible with the browser.
-   Installation and setup can be time-consuming for beginners.

**Playwright**
-   Simple setup with `playwright install`, which automatically downloads the required browser binaries.
-   No need to manually manage drivers or browser compatibility.
-   Faster and easier to get started.

## Locators
**Selenium**
- Use `find_element_by_*` and `find_elements_by_*` (e.g., `find_element_by_id`,  fo`find_element_by_xpath`). for locate elements
- Use `find_element(By.*)` in Selenium 4

**Playwright**
- `page.locator(selector)`, which is more declarative
- `page.locator("#allow-collecting-longhorn-usage-metrics")`- by ID
- `page.locator("//form/div[1]")` - by xpath

## Waiting strategy
**Selenium**
 - implicitly_wait : Only wait for element find, not guarantee element is ready(clickable, visible)
 - Extra code for check element ready

**Playwright**
- Auto wait(default 30s) : wait until element is ready
 