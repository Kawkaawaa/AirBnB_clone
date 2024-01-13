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

    do_EOF = do_quit


if __name__ == "__main__":
    HBNBCommand().cmdloop()
