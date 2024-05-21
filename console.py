#!/usr/bin/python3
'''this is the entry point to our console'''
import cmd

class HBNBCommand(cmd.Cmd):
    '''HBNB console for the webserver'''
    prompt = "(hbnb)"
    def do_quit(self, line):
        '''quit the interpreter'''
        return True

    def do_EOF(self, line):
        '''handle EOF'''
        if line == '':
            return True
    def emptyline(self):
        '''ignore empty line'''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
