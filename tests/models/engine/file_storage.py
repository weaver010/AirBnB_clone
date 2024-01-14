#!/usr/bin/python3
"""File_storage
"""

import models
from models.base_model import BaseModel
import json
import os
from models.amenity import Amenity
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage:
    """FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return all objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """Create obj
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Save obj
        """
        lok = FileStorage.__objects
        ksm = {}

        for object in lok.keys():
            ksm[object] = lok[object].to_dict()

        ml = {}
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as e:
                try:
                    ml = json.load(e)
                except Exception:
                    pass

        ml.update(ksm)

        with open(FileStorage.__file_path, "w") as e:
            json.dump(ml, e)

    def reload(self):
        """return all objects
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as e:
                try:
                    hl = json.loads(e)
                    for key, value in hl.items():
                        class_name, obj_id = key.split('.')
                        ah = eval(class_name)
                        sy = ah(**value)
                        FileStorage.__objects[key] = sy
                except Exception:
                    pass
