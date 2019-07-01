#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import sys
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
        """Prints the string representation of an instance based on the
        class name and id
        """

        if not line or line is "":
            print('** class name missing **')
            return
        args = line.split()
        if len(args) == 2:
            if args[0] in self.classes:
                key = args[0] + '.' + args[1]
                rec_of_instances = storage.all()
                if key not in rec_of_instances:
                    print("** no instance found **")
                    return
                else:
                    print(rec_of_instances[key])
                    return
            else:
                print("** class doesn't exist **")
                return
        elif len(args) == 1:
                print("** instance id missing **")
                return

    def do_destroy(self, line):
        rec_of_instances = storage.all()
        if not line or line == "":
            print('** class name missing **')

        args = line.split()
        if len(args) == 2:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            key = args[0] + '.' + args[1]
            if key not in rec_of_instances:
                print('** no instance found **')
                return
            else:
                del rec_of_instances[key]
                storage.save()

        elif len(args) == 1:
            print('** instance id missing **')
            return

    def do_update(self, line):

        rec_of_instances = storage.all()
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        elif len(args) == 1:
            print('** instance id missing **')
            return
        elif len(args) == 2:
            print('** attribute name missing **')
            return
        elif len(args) == 3:
            print('** value missing **')
            return
        else:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            key = args[0] + '.' + args[1]
            if key not in rec_of_instances:
                print('** no instance found **')

            else:
                if isinstance(args[3], str):
                    setattr(rec_of_instances[key], args[2], str(args[3]))
                    storage.save()
                elif isinstance(args[3], int):
                    setattr(rec_of_instances[key], args[2], int(args[3]))
                    storage.save()
                elif isinstance(args[3], float):
                    setattr(rec_of_instances[key], args[2], float(args[3]))
                    storage.save()
                else:
                    return

    def do_all(self, line):
        """Prints all string representation of all instances based or not
        on the class name
        """

        key_list = []
        instances = storage.all()
        if len(line) == 0:
            for v in instances.values():
                key_list.append(v.__str__())
            print(key_list)
            return
        line_list = line.split()
        if line_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        for v in instances.values():
            if line_list[0] == v.__class__.__name__:
                key_list.append(v.__str__())
        print(key_list)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
