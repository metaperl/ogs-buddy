# importing webdriver from selenium
from lib2to3.pgen2 import driver
from selenium import webdriver

import time
from loguru import logger

from PIL import Image

# Here Chrome will be used
from autoselenium import Driver

from traitlets import HasTraits, Int, Unicode, default, Any    
import PySimpleGUI as sg


def filename_from_url(url, append=None):
    parts = url.split("/")
    logger.debug(f"{parts=}")
    game_number = parts[-1]
    # import datetime module
    from datetime import datetime

    # consider date in string format
    my_date = datetime.now()

    # convert datetime format into %Y-%m-%d-%H:%M:%S
    # format using strftime
    filename = "{}-{}".format(
        game_number,
        my_date.strftime("%Y-%m-%d-%H-%M-%S"))

    if append:
        filename += f"-{append}"

    return filename

class OGS(HasTraits):

    driver = Any()

    def toggle_ai(self):
        from selenium.webdriver.common.action_chains import ActionChains
        actions = ActionChains(self.driver)
        actions.send_keys('I')
        actions.perform()

    def make_flashcard(self):
        for side in "front back".split():
            current_url=self.driver.current_url
            logger.debug(f"{current_url=}")
            filename = filename_from_url(self.driver.current_url, append=f"{side}.png")
            logger.debug(filename)
            self.toggle_ai()
            self.driver.save_screenshot(filename)
        # # Loading the image
        # image = Image.open("image33.png")

        # # Showing the image
        # image.show()

def main():
    with Driver('chrome', root='drivers') as driver:

        # URL of website
        url = "https://online-go.com/game/46749656"
        
        # Opening the website
        driver.get(url)

        ogs = OGS(driver=driver)

        gui_loop(ogs)


def gui_loop(ogs):
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('')],
                [sg.Text('Enter something on Row 2'), sg.InputText()],
                [sg.Button('MakeFlashCard'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('OGS BUDDY', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        print(f'{event} entered ', values[0])

        if event == 'MakeFlashCard': # if user closes window or clicks cancel
            ogs.make_flashcard()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break

    window.close()


if __name__ == '__main__':
    main()
    
