from colorama import init, Fore, Back
from pyfiglet import Figlet

class Colored(object):
    def red(self,s):
        return Fore.RED + s + Fore.RESET
    def green(self,s):
        return Fore.GREEN + s + Fore.RESET
    def yellow(self,s):
        return Fore.YELLOW + s + Fore.RESET
    def blue(self,s):
        return Fore.BLUE + s + Fore.RESET
    def magenta(self,s):
        return Fore.MAGENTA + s + Fore.RESET
    def cyan(self,s):
        return Fore.CYAN + s + Fore.RESET
    def white(self,s):
        return Fore.WHITE + s + Fore.RESET
    def black(self,s):
        return Fore.BLACK + s + Fore.RESET
    def white_green(self,s):
        return Fore.WHITE + Back.GREEN + s + Fore.RESET + Back.RESET

class Style(Colored):
    def figlet(text):
        figlet = Figlet()
        return figlet.renderText(text)