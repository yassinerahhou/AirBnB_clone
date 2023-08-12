#!/usr/bin/python3
"""FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent storage engine.

    Attributes:
        __file_path .
        __objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
