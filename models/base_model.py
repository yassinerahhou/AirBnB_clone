<<<<<<< HEAD
import uuid
from datetime import datetime
class BaseModel:
    """ clase baseModel
    """
    name = str
    my_number =     int
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    def __str__(self):
        """
        str fonction
        """
        self.__dict__= {
        "my number" : self.my_number,
        "name":self.name,
        "__class__":self.__class__.__name__,
        "updated_at":self.updated_at,
        "id":self.id,
        "created_at":self.created_at,
        }
        return f"[{type(self).__name__}] {self.id} {self.__dict__}"
    def save(self):
        """ save fonction"""
        self.updated_at = datetime.now()
    def to_dict(self):
        """ to_dict fonction"""
        mydictionair = {
            "my number" : self.my_number,
            "name":self.name,
            "__class__":self.__class__.__name__,
            "updated_at":self.updated_at.isoformat(),
            "id":self.id,
            "created_at":self.created_at.isoformat(),
           
            }
        return mydictionair
=======
#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel.

        Args:
            *args(any): Unused.
            **kwargs (dict)
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary

        Includes the key/value pair
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the print/str"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
>>>>>>> 8287e6d6e2948de1239053be73732be730f487ec
