#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import argparse 


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

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

    def create(self, line)











if __name__ == '__main__':
    HBNBCommand().cmdloop()
    