# importing webdriver from selenium
from selenium import webdriver

import time
from loguru import logger

from PIL import Image

# Here Chrome will be used
from autoselenium import Driver

with Driver('chrome', root='drivers') as driver:

    # URL of website
    url = "https://online-go.com/game/46749656"
    
 

    # Opening the website
    driver.get(url)
    logger.info("Waiting 10 seconds...")
    time.sleep(10)
    logger.info("Starting screenshot.")

    driver.save_screenshot("image.png")

    # Loading the image
    image = Image.open("image.png")

    # Showing the image
    image.show()
