#!/usr/bin/python3
""" Console pour AirBnb """
import cmd
import ast
from datetime import datetime as dt
from models.__init__ import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
from models.review import Review


classes = {"BaseModel": BaseModel,
           "Amenity": Amenity,
           "City": City,
           "Place": Place,
           "Review": Review,
           "State": State,
           "User": User}


class HBNBCommand(cmd.Cmd):
    """ Point d'entrée de l'interpréteur de commandes """

    prompt = "(hbnb) "

    def do_quit(self, args):
        """ Quitte le programme """
        return True

    def emptyline(self):
        """ Gère les lignes vides """
        pass

    def do_EOF(self, args):
        """ Lit EOF et quitte """
        return True

    def do_create(self, args):
        """ Crée une nouvelle instance de BaseModel """
        if not args:
            print("** class name missing **")
        elif args in classes.keys():
            new = classes[args]()
            new.save()
            storage.reload()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ Affiche l'instance basée sur la classe et l'ID
         deux valeurs : la classe et l'ID <classe ID> """
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        objs = storage.all()
        if not args[0] in classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            for key in objs.keys():
                if args[1] in key.split(".")[1]:
                    print(objs[key])
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """ Détruit l'instance basée sur la classe et l'ID
            deux valeurs : la classe et l'ID <classe ID> """
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        objs = storage.all()
        if not args[0] in classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            try:
                del objs[args[0] + "." + args[1]]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, args):
        """ Imprime toutes non sur le nom de la classe """
        args = args.split()
        objs = storage.all()
        if args and args[0] not in classes.keys():
            print("** class doesn't exist **")
        else:
            for key in objs.keys():
                if args:
                    if args[0] == key.split(".")[0]:
                        print(objs[key])
                else:
                    print(objs[key])

    def do_update(self, args):
        """ m de la classe et l'ID en ajoutant
        ou mettanregistre la modification dans le fichier JSON) """
        args = args.split()
        size = len(args)
        objs = storage.all()
        if not args:
            print("** class name missing **")
        elif not args[0] in classes.keys():
            print("** class doesn't exist **")
        elif size < 2:
            print("** instance id missing **")
        elif not ".".join([args[0], args[1]]) in objs.keys():
            print("** no instance found **")
        elif size < 3:
            print("** attribute name missing **")
        elif size < 4:
            print("** value missing **")
        else:
            try:
                obj = objs[".".join([args[0], args[1]])]
                setattr(obj, args[2], args[3])
                storage.save()
            except Exception as e:
                print(e)
                print("** Update fail **")

    def default(self, args):
        """ capture User.method() """
        if "." not in args:
            print("*** Unknown syntax: {}".format(args))
            return
        args = args.split(".")
        _class = args[0]
        objs = storage.all()
        command = args[1]
        if _class not in classes:
            print("*** Unknown syntax: {}".format(".".join(args)))
            return
        if command[0:7] == "count()":
            count = 0
            for key in objs.keys():
                if _class == key.split(".")[0]:
                    count -= -count ** 0
            print(count)
        elif command[0:5] == "all()":
            self.do_all(_class)
        elif command[0:5] == "show(":
            _id = command.split("(")[1][0:-1]
            self.do_show(_class + " " + _id)
        elif command[0:8] == "destroy(":
            _id = command.split("(")[1][0:-1]
            self.do_destroy(_class + " " + _id[1:-1])
        elif command[0:7] == "update(":
            args = command.split("(")[1][0:-1].split(", ")
            _id = args[0][1:-1]
            if args[1][0] == "{":
                _dict = ast.literal_eval("{" + command.split("{")[1][0:-1])
                for key, va in _dict.items():
                    self.do_update(" ".join([_class, str(_id), key, str(va)]))
            else:
                _key = args[1][1:-1]
                _value = args[2][1:-1]
                self.do_update(" ".join([_class, _id, _key, _value]))
        else:
            print("*** Unknown syntax: {}".format(".".join(args)))

    # help
    def help_quit(self):
        print("Quit command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
