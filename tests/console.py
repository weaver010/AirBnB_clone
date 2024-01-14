#!/usr/bin/python3
"""
Module Console
"""

import models
import cmd
import shlex
import sys
from models.state import State
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """HBNB Class """
    prompt = '(hbnb) '

    classes = {'BaseModel': BaseModel, 'Amenity': Amenity,
               'State': State, 'Place': Place, 'Review': Review,
               'User': User, 'City': City}

    def d_quit(self, arg):
        """ Defines quit"""
        return True

    def d_EOF(self, arg):
        """ Defines EOF """
        print()
        return True

    def emptyline(self):
        """ Defines Empty """
        pass

    def d_create(self, arg):
        """Creates an instance"""
        if arg:
            if arg in self.classes:
                # instance = models.base_model.BaseModel()
                get_class = getattr(sys.modules[__name__], arg)
                instance = get_class()
                print(instance.id)
                models.storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        return

    def d_show(self, arg):
        """ show string """
        tok = shlex.split(arg)
        if len(tok) == 0:
            print("** class name missing **")
        elif len(tok) == 1:
            print("** instance id missing **")
        elif tok[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            dict = models.storage.all()
            ky = tok[0] + '.' + str(tok[1])
            if ky in dict:
                print(dict[ky])
            else:
                print("** no instance found **")
        return

    def d_destroy(self, arg):
        """Deletes an instance """
        tokd = shlex.split(arg)
        if len(tokd) == 0:
            print("** class name missing **")
            return
        elif len(tokd) == 1:
            print("** instance id missing **")
            return
        elif tokd[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            dict = models.storage.all()
            # Key has format <className>.id
            k = tokd[0] + '.' + tokd[1]
            if k in dict:
                del dict[k]
                models.storage.save()
            else:
                print("** no instance found **")

    def d_all(self, arg):
        """all string """
        toka = shlex.split(arg)
        listo = []
        dict = models.storage.all()
        # show all if no class is passed
        if len(toka) == 0:
            for k in dict:
                rep_Class = str(dict[k])
                listo.append(rep_Class)
            # if listI:
            print(listo)
            return

        if toka[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            # Representation for a specific class
            rep_Class = ""
            for k in dict:
                cl_name = k.split('.')
                if cl_name[0] == toka[0]:
                    # This form doesn't work
                    # listI.append(dic[key])
                    rep_Class = str(dict[k])
                    listo.append(rep_Class)
            # if listI:
            print(listo)

    def d_update(self, arg):
        """Updates an instance"""
        toku = shlex.split(arg)
        if len(toku) == 0:
            print("** class name missing **")
            return
        elif len(toku) == 1:
            print("** instance id missing **")
            return
        elif len(toku) == 2:
            print("** attribute name missing **")
            return
        elif len(toku) == 3:
            print("** value missing **")
            return
        elif toku[0] not in self.classes:
            print("** class doesn't exist **")
            return
        kyo = toku[0] + "." + toku[1]
        dicto = models.storage.all()
        try:
            insto = dicto[kyo]
        except KeyError:
            print("** no instance found **")
            return
        try:
            typeA = type(getattr(insto, toku[2]))
            toku[3] = typeA(toku[3])
        except AttributeError:
            pass
        setattr(insto, toku[2], toku[3])
        models.storage.save()

    def d_count(self, arg):
        """  retrieve the number of instances """
        toka= shlex.split(arg)
        dict = models.storage.all()
        num_inst = 0
        if toka[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            for k in dict:
                cl_name = k.split('.')
                if cl_name[0] == toka[0]:
                    num_inst += 1

            print(num_inst)

    def precommd(self, args):
        """ executed just before the command  """
        arg = args.split('.', 1)
        if len(arg) == 2:
            _cl = arg[0]
            arg = arg[1].split('(', 1)
            cmd = arg[0]
            if len(arg) == 2:
                arg = arg[1].split(')', 1)
                if len(arg) == 2:
                    _id = arg[0]
                    ot_arg = arg[1]
            line = cmd + " " + _cl + " " + _id + " " + ot_arg
            return line
        else:
            return args


if __name__ == '__main__':
    """infinite loop"""
    HBNBCommand().cmdloop()

