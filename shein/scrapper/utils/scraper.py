import logging
import re

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from shein.constants import DEBUG

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_driver() -> webdriver.Chrome:
    """Get a headless Selenium driver.

    Returns
    -------
        webdriver.Chrome: Selenium driver
    """
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")

    chromedriver_autoinstaller.install()

    # driver = webdriver.Remote(
    # command_executor="http://localhost:4444/wd/hub",
    # desired_capabilities={},
    # options=options
    # )

    driver = webdriver.Chrome()
    driver.delete_all_cookies()
    return driver


def get_max_pagination(driver: webdriver.Chrome, url: str) -> int:
    """
    Get the maximum number of pages for a category.

    Parameters
    ----------
    driver : webdriver.Chrome
        Selenium driver
    url : str
        The category

    Returns
    -------
    int
        The maximum number of pages
    """
    driver.get(url)
    max_pages = 1

    if not DEBUG:
        pagination_text = driver.find_element(By.CLASS_NAME, "sui-pagination__total").text
        pagination_number = re.findall(r"\b\d{1,2}\b", pagination_text)

        max_pages = int(pagination_number[0])
        logger.info("Found %s pages", max_pages)

    return max_pages
