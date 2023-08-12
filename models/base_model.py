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
