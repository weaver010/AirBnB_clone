#!/usr/bin/python3
"""
Module: base_model.py
This is the "base class" module.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class 

    """
    def __init__(self, *args, **kwargs):
        """ the instance
        """

        asm = "%Y-%m-%dT%H:%M:%S.%f"

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, asm)
                setattr(self, k, v)

    def save(self):
        """
        save obj 
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        return all
        """
        awes = self.__dict__.copy()
        awes['__class__'] = self.__class__.__name__
        awes['created_at'] = self.created_at.isoformat()
        awes['updated_at'] = self.updated_at.isoformat()
        return awes

    def __str__(self):
        """
        return str 
        """
        return f"[{type(self).__name__}] ({self.id}) {str(self.__dict__)}"
