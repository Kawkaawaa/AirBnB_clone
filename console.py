#!/usr/bin/python3
"""
Module Console
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Hbnb Command Line Interface"""

    prompt = '(hbnb)'
    classes = {'BaseModel': BaseModel, 'User': User}

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

    def do_create(self, line):
        """Creates a new instance of a given class, saves it \
        (to the JSON file) and prints the id."""
        if line == '':
            print('** class name missing **')
        elif line not in HBNBCommand.classes:
            print('** class doesn\'t exist **')

    def do_show(self, line):
        """Prints the string representation of an instance based \
        on the class name and id."""
        args = line.split()
        if line == '':
            print('** class name missing **')
        elif args[0] not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
        else:
            if len(args) < 2:
                print('** instance id missing **')
            else:
                classname = args[0]
                objid = args[1]
                key = classname + '.' + objid
                try:
                    print(storage.all()[key])
                except KeyError:
                    print('** no instance found **')

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        args = line.split()
        if line == '':
            print('** class name missing **')
        elif args[0] not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
        else:
            if len(args) < 2:
                print('** instance id missing **')
            else:
                classname = args[0]
                objid = args[1]
                key = classname + '.' + objid
                try:
                    del storage.all()[key]
                    storage.save()
                except KeyError:
                    print('** no instance found **')

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all
        """
        args = line.split()
        result = []
        if len(args) != 0:
            if args[0] not in HBNBCommand.classes:
                print('** class doesn\'t exist **')
                return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
