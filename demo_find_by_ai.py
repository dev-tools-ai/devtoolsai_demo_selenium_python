from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from devtools_ai.selenium import SmartDriver

def _main() -> None:
    """Main driver"""
    chrome_driver = Chrome(service=Service(ChromeDriverManager().install()))

    # Convert chrome_driver to smartDriver
    driver = SmartDriver(chrome_driver, "<<get your api key at dev-tools.ai>>")

    # Navigate to Google.com
    driver.get("https://duckduckgo.com")
    sleep(1)

    # Find the login field and input username"
    search_box = driver.find_by_ai('python_searchbox')
    search_box.send_keys("Hello World!")

    sleep(2)

    driver.quit()


if __name__ == "__main__":
    _main()
