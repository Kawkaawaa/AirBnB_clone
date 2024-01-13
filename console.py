#!/usr/bin/python3
"""
Module Console
"""
import cmd
from models.base_model import BaseModel


class HbnbCommand(cmd.Cmd):
    """Hbnb Command Line Interface"""

    prompt = '(hbnb)'
    classes = {'BaseModel': BaseModel}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()  # Print a newline for a cleaner exit
        return True


if __name__ == "__main__":
    HbnbCommand().cmdloop()
