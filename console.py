#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, line):
        if not line:
            print('** class name missing **')
            return
        args = line.split()
        try:
            instance = eval(args[0])()
            instance.save()
            print(instance.id)
        except:
            print("** class doesn't exist **")
            return

    def do_show(self, line):
        if not line or line is "":
            print('** class name missing **')
            return
        else:
            args = line.split()
            if args[0] not in storage._objects:
                print("** class doesn't exist **")
            elif not args[1] or args[1] == "":
                print("** instance id missing **")
            else:
                rec_of_instances = storage.__objects
                key = args[0] + '.' + args[1]
                if key not in dict:
                    print('** no instance found **')
                else:
                    print(rec_of_instances[key])

    def do_destroy(self, line):
        rec_of_instances = storage.__objects
        if not line or line == "":
            print('** class name missing **')
        else:
            args = line.split()
            if args[0] not in rec_of_instances:
                print("** class doesn't exist **")
            elif not args[1] or args[1] == "":
                print('** instance id missing **')
            else:
                key = args[0] + '.' + args[1]
                if key not in rec_of_instances:
                    print('** no instance found **')
                else:
                    del rec_of_instances[key]
                    storage.save()

    def do_update(self, line):
        rec_of_instances = storage.__objects
        if not line or line == "":
            print('** class name missing **')
        else:
            args = line.split()
            if args[0] not in rec_of_instances:
                print("** class doesn't exist **")
            elif not args[1] or args[1] == "":
                print('** instance id missing **')
            key = args[0] + '.' + args[1]
            if key not in rec_of_instances:
                print('** no instance found **')
            elif not args[2]:
                print('** attribute name missing **')
            elif not args[3]:
                print('** value missing **')
            else:
                if isinstance(args[3], str):
                    setattr(rec_of_instances[key], args[2], str(args[3]))
                    storage.save()
                elif isinstance(args[3], int):
                    setattr(rec_of_instances[key], args[2], int(args[3]))
                    storage.save()
                else:
                    setattr(rec_of_instances[key], args[2], float(args[3]))
                    storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

