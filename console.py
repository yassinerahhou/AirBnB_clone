import cmd
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    def do_quit(self , arg) :
        return True
    def do_EOF(self, arg):
        return True
    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass    
if __name__ == '__main__':
    HBNBCommand().cmdloop()

