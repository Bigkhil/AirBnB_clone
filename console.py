#!/usr/bin/python3
'''this is the entry point to our console'''
import cmd

class HBNBCommand(cmd.Cmd):
    '''HBNB console for the webserver'''
    prompt = "(hbnb)"
    def do_quit(self):
        '''quit the interpreter'''
        return True
    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
