#!/usr/bin/python3
"""A program containing the entry point
of the command interpreter
"""
import models
from models import storage
import cmd
import re


class HBNBCommand(cmd.Cmd):
    """Represents a Console Program"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Exit at End of File"""
        return True

    def emptyline(self):
        """When empty line + ENTER nothing
        executed"""
        pass

    def do_quit(self, line):
        """Exit the program"""
        return True

    def do_create(self, line):
        """
        create:

        Creates a new instance of BaseModel saves
        it to JSON & prints the id

        This method breaks a string of arguments down into smaller chunks,
        or strings. It will try to return the value of the named attribute.
        That will be stored, saved, and printed. If the named attribute
        doesn't exist, KeyError is raised and handled before "** class
        doesn't exist **" is printed to the screen.
        If the class name is missing, "** class name missing **" will be
        printed to the screen.
        """
        if len(line) == 0:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            cls = storage.classes()[line]()
            cls.save()
            print(cls.id)

    def do_show(self, line):
        """

        show:

        Prints the string representation of an instance based on the
        class name and id Ex $ show BaseModel 1234-1234-1234

        This method splits the arguments into smaller strings before the
        arguments are used. If the length of the arguments is less than two,
        IndexError is raised, handled, and "** instance id missing **" will
        print to the screen since more than one argument is needed. However,
        if an appropriate amount of arguments is available, the result of
        class name and id will print to the screen. Otherwise, KeyError
        will be raised, handled and "** no instance found **" will be printed
        to the screen.
        If the class name is missing, "** class name missing **" will be
        printed to the screen. If the class name doesn't exist, "** class
        doesn't exist **" will be printed to the screen.
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            wrds = line.split(' ')
            if wrds[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(wrds) < 2:
                print("** instance id missing **")
            else:
                obj_id = "{}.{}".format(wrds[0], wrds[1])
                if obj_id in storage.all():
                    print(storage.all()[obj_id])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """
        destroy:

        Deletes an instance based on the class name and id
        save the change into the JSON file

        This method requires two arguments, a class name and id. If the class
        name is missing, "** class name missing **" will be printed to the
        screen. If class name doesn't exist, "** class doesn't exist **"
        will be printed to the screen. If class name does exist, then the
        command will search for the id, or the second argument. If the id is
        missing, IndexError is raised and "** instance id missing **" will
        print to the screen. However, if found, the instance will be deleted.
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            wrds = line.split(' ')
            if wrds[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(wrds) < 2:
                print("** instance id missing **")
            else:
                obj_id = "{}.{}".format(wrds[0], wrds[1])
                if obj_id in storage.all():
                    storage.all().pop(obj_id)
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """
        all:

        Prints all string representation of all instances based or not on the
        class name

        This method will print out the string representation of the value
        of every instance of a class or not a class. If the class doesn't
        exist, "** class doesn't exist **" will print to the screen.
        """
        if len(line) == 0:
            full_list = [str(obj) for key, obj in storage.all().items()]
            print(full_list)
        if len(line) >= 1:
            wrds = line.split(' ')
            if wrds[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                instance_list = [str(obj) for key, obj in storage.all().items()
                                 if type(obj).__name__ == wrds[0]]
                print(instance_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute(save the change into
        the JSON file"""
        if len(line) == 0:
            print("** class name missing **")
            return

        pattern = re.compile(r'(\S+)')
        wrds = re.findall(pattern, line)
        classname = wrds[0]
        uid = wrds[1]
        attribute = wrds[2]
        value = wrds[3]
        if len(wrds) == 0:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                datatype = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        datatype = float
                    else:
                        datatype = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif datatype:
                    try:
                        value = datatype(value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
