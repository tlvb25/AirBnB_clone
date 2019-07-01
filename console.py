#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import argparse
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    classes = {"BaseModel"}

    def do_quit(self, line):
        """ """
        return True

    def emptyline(self):
        """ """
        pass

    def do_EOF(self, line):
        """ """
        print()
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel"""

        if len(line) == 0:
            print("** class name missing **")
            return
        line_list = line.split()
        try:
            inst1 = eval(line_list[0])
            inst1.save()
            print(inst1.id)
        except Exception:
            print("** class doesn't exist **")
            return

    def do_show(self, line):
        """Prints the string representation of an instance based on the class
        name and ID
        """

        try:
            if not line:
                raise SyntaxError()
            line_list = line.split()
            inst1 = eval(line_list[0])
            if line_list[1] is not in self.classes:
                raise NameError()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")





if __name__ == '__main__':
    HBNBCommand().cmdloop()
