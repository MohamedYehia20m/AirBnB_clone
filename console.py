#!/usr/bin/python3
"""the entry point of the command interpreter"""

import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
