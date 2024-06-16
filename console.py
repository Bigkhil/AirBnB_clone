#!/usr/bin/python3
"""
Console module for HBNB project
"""

import cmd
import models
import shlex
from models.base_model import BaseModel
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for command interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handles EOF (Ctrl+D) to exit the program"""
        print()  # Print a new line before exiting
        return True

    def emptyline(self):
        """Do nothing if line is empty"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        else:
            try:
                new_instance = models.classes_dict[args[0]]
            except KeyError:
                print("** class doesn't exist **")
                return
        print(new_instance().id)
        models.storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id.
        Usage: show <class name> <id>"""
        args = shlex.split(arg)
        obj_dict = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in models.classes_dict:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] + '.' + args[1] not in obj_dict:
            print("** no instance found **")
            return
        print(obj_dict[args[0] + '.' + args[1]])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (saves the change into the JSON file).
        Usage: destroy <class name> <id>"""
        args = shlex.split(arg)
        obj_dict = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in models.classes_dict:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] + '.' + args[1] not in obj_dict:
            print("** no instance found **")
            return
        del obj_dict[args[0] + '.' + args[1]]
        models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = shlex.split(arg)
        if len(args) != 0 and args[0] not in models.classes_dict:
            print("** class doesn't exist **")
            return
        obj_list = []
        for obj in models.storage.all().values():
            if len(args) == 0:
                obj_list.append(obj.__str__())
            elif args[0] == obj.__class__.__name__:
                obj_list.append(obj.__str__())
        print(obj_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and.
        id by adding or updating attribute
        """
        args = shlex.split(arg)
        obj_dict = models.storage.all()
        if len(args) < 1:
            print("** class name missing **")
            return
        elif args[0] not in models.classes_dict:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif args[0] + '.' + args[1] not in obj_dict:
            print("** no instance found **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        else:
            obj = obj_dict[args[0] + '.' + args[1]]
            attr = type(getattr(obj, args[2], ''))
            setattr(obj, args[2], attr(args[3]))
            obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
