#!/usr/bin/python3
"""
Module Console
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNB Class"""
    prompt = '(hbnb)'

    classes = {'BaseModel': BaseModel}

    def do_quit(self, arg):
        """ Quit command  to exit the program """
        return True

    def do_EOF(self, arg):
        """ Quit command  to exit the program """
        return True

    def do_empyline(self):
        """ Defines Empty option"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
