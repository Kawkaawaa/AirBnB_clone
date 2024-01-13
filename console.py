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
    
    def do_quit(self, line):
        """Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """(Ctrl+D): Exit the program.
        """
        print("")
        return True
    
    def emptyline(self):
        """emptyline and enter does nothing anymore.
        """
        pass

if __name__ == "__main__":
    HbnbCommand().cmdloop()
