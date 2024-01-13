#!/usr/bin/python3
"""
Module Console
"""
import cmd
import shlex
import models
from models.base_model import BaseModel
import sys


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

    def do_create(self, argument):
        """Creates an instance of BaseModel"""
        if argument:
            if argument in self.classes:
                # instance = models.base_model.BaseModel()
                get_class = getattr(sys.modules[__name__], argument)
                instance = get_class()
                print(instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        print(args)
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in self.classes:
                print(arg[0])
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            dic = models.storage.all()
            print(dic)
            keyU = args[0] + '.' + str(args[1])
            if keyU in dic:
                print(dic[keyU])
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()

