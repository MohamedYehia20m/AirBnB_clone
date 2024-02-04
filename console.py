#!/usr/bin/python3
"""the entry point of the command interpreter"""

import cmd
import json
import uuid
from datetime import datetime

class BaseModel:
    """
    Placeholder for BaseModel class.
    You can replace this with your actual implementation.
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Handle EOF (Ctrl+D) to exit the program.
        """
        print("")
        return True

    def emptyline(self):
        """
        Override emptyline to do nothing on an empty line.
        """
        pass


def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it to the JSON file, and print the id.
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            instance = eval(arg)()
            instance.save()
            print(instance.id)
        except NameError:
            print("** class doesn't exist **")

def do_show(self, arg):
        """
        Print the string representation of an instance based on the class name and id.
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in globals():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = self.load_objects()
        if key not in objects:
            print("** no instance found **")
        else:
            print(objects[key])

def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (saves the change into the JSON file).
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in globals():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = self.load_objects()
        if key not in objects:
            print("** no instance found **")
        else:
            del objects[key]
            self.save_objects(objects)

def do_all(self, arg):
        """
        Print all string representations of all instances based or not on the class name.
        """
        objects = self.load_objects()

        if arg:
            if arg not in globals():
                print("** class doesn't exist **")
                return

            filtered_objects = {k: v for k, v in objects.items() if k.split('.')[0] == arg}
            objects = filtered_objects

        print([str(obj) for obj in objects.values()])

def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in globals():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = self.load_objects()
        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[3]
        attribute_value = args[4]

        instance = objects[key]
        setattr(instance, attribute_name, attribute_value)
        instance.updated_at = datetime.now()
        self.save_objects(objects)

def load_objects(self):
        try:
            with open("file.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

def save_objects(self, objects):
        with open("file.json", "w") as file:
            json.dump(objects, file)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
