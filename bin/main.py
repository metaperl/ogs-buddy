# importing webdriver from selenium
from lib2to3.pgen2 import driver
from weakref import finalize
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import time
from loguru import logger

from PIL import Image

# Here Chrome will be used
from autoselenium import Driver

from traitlets import HasTraits, Int, Unicode, default, Any    
import PySimpleGUI as sg


def move_upper_right(window):
    screen_width, screen_height = window.get_screen_dimensions()
    win_width, win_height = window.size
    x, y = (screen_width - win_width), 0
    window.move(x, y)



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
    url = Unicode("https://online-go.com/game/46749656")

    def begin(self):
        self.driver.get(self.url)
        self.remove_ogs_logo()

    @property
    def action_chains(self):
        return ActionChains(self.driver)

    def remove_ogs_logo(self):
        elem = self.driver.find_element(By.CLASS_NAME, 'ogs-nav-logo')
        self.driver.execute_script("""
var element = arguments[0];
element.parentNode.removeChild(element);
""", elem)

    def toggle_ai(self):
        actions = self.action_chains
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

    def move_next_to_browser(self, window):
        window_size = self.driver.get_window_size()
        logger.debug(f"{window_size=}")
        window.move(window_size['width'], 0)



def main():
    with Driver('chrome', root='drivers') as driver:
        ogs = OGS(driver=driver)
        ogs.begin()

        gui_loop(ogs)


def gui_loop(ogs):
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [ 
              [sg.Text(' ' * 60)],

                [sg.Button('MakeFlashCard'), sg.Button('Exit')],
                 [sg.Text('')]
                 ]

    # Create the Window
    window = sg.Window('OGS BUDDY', layout, finalize=True)
    ogs.move_next_to_browser(window)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        print(f'{event} entered ', values[0])

        if event == 'MakeFlashCard': # if user closes window or clicks cancel
            ogs.make_flashcard()
        if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
            break

    window.close()


if __name__ == '__main__':
    main()
    
