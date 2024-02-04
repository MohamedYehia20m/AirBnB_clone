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
    Syntax: create <class_name>
    """
    args = arg.split()

    if not args or len(args) != 1:
        print("** Incorrect syntax. Use: create <class_name> **")
        return

    class_name = args[0]

    try:
        instance = eval(class_name)()
        instance.save()
        print(instance.id)
    except NameError:
        print("** Class doesn't exist **")

def do_show(self, arg):
    """
    Print the string representation of an instance based on the class name and id.
    Syntax: show <class_name> <id>
    """
    args = arg.split()

    if not args or len(args) != 2:
        print("** Incorrect syntax. Use: show <class_name> <id> **")
        return

    class_name, instance_id = args

    try:
        instance = eval(class_name)()
        key = "{}.{}".format(class_name, instance_id)
        objects = self.load_objects()

        if key not in objects:
            print("** No instance found **")
        else:
            print(objects[key])
    except NameError:
        print("** Class doesn't exist **")


def do_destroy(self, arg):
    """
    Deletes an instance based on the class name and id (saves the change into the JSON file).
    Syntax: destroy <class_name> <id>
    """
    args = arg.split()

    if not args or len(args) != 2:
        print("** Incorrect syntax. Use: destroy <class_name> <id> **")
        return

    class_name, instance_id = args

    try:
        instance = eval(class_name)()
        key = "{}.{}".format(class_name, instance_id)
        objects = self.load_objects()

        if key not in objects:
            print("** No instance found **")
        else:
            del objects[key]
            self.save_objects(objects)
    except NameError:
        print("** Class doesn't exist **")


def do_all(self, arg):
    """
    Print all string representations of all instances based or not on the class name.
    Syntax: all [<class_name>]
    """
    args = arg.split()
    objects = self.load_objects()

    if args and len(args) == 1:
        class_name = args[0]

        try:
            eval(class_name)()
            objects = {k: v for k, v in objects.items() if k.split('.')[0] == class_name}
        except NameError:
            print("** Class doesn't exist **")

    print([str(obj) for obj in objects.values()])


def do_update(self, arg):
    """
    Updates an instance based on the class name and id by adding or updating attribute.
    Syntax: update <class_name> <id> <attribute_name> "<attribute_value>"
    """
    args = arg.split()

    if not args or len(args) < 4 or len(args) % 2 != 0:
        print("** Incorrect syntax. Use: update <class_name> <id> <attribute_name> '<attribute_value>' **")
        return

    class_name, instance_id = args[:2]

    try:
        instance = eval(class_name)()
        key = "{}.{}".format(class_name, instance_id)
        objects = self.load_objects()

        if key not in objects:
            print("** No instance found **")
            return

        for i in range(2, len(args), 2):
            attribute_name, attribute_value = args[i], args[i + 1]
            setattr(instance, attribute_name, attribute_value)

        instance.updated_at = datetime.now()
        self.save_objects(objects)
    except NameError:
        print("** Class doesn't exist **")


def load_objects(self):
        """
        Load objects from the JSON file.
        """
        try:
            with open("file.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

def save_objects(self, objects):
        """
        Save objects to the JSON file.
        """
        with open("file.json", "w") as file:
            json.dump(objects, file)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
