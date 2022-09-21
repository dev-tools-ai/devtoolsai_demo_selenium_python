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
    driver.get("https://github.com/login")
    sleep(1)

    # Find the login field and input username"
    login_field = driver.find_element(By.XPATH, '//input[@id="login_field"]')
    login_field.send_keys("my_username")

    sleep(2)

    driver.quit()


if __name__ == "__main__":
    _main()
