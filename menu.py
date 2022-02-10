from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem

from loading.config_parser import get_exit_message


class Menu:
    def __init__(self, title, subtitle=""):
        self.menu = ConsoleMenu(title, subtitle)
        self.add_item(get_exit_message(), exit())

    def add_item(self, message, function, args=None):
        menu_item = FunctionItem(message, function)
        self.menu.append_item(menu_item)

    def start_menu(self):
        self.menu.start()
