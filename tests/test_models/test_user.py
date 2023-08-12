#!/usr/bin/python3
"""Module test_user

tests for User Class
"""

import inspect
import sys
import unittest
from datetime import datetime
from io import StringIO

import pycodestyle
from models import user
from tests.test_models.test_base_model import BaseModel

User = user.User


class TestUserDocsAndStyle(unittest.TestCase):
    """Tests User class"""

    def test_pycodestyle(self):
        """Tests compliance"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/user.py", "tests/test_models/test_user.py"])
        self.assertEqual(result.total_errors, 0)

    def test_module_docstring(self):
        """Tests whether"""
        self.assertTrue(len(user.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests whether"""
        self.assertTrue(len(User.__doc__) >= 1)

    def test_class_name(self):
        """Test whether"""
        self.assertEqual(User.__name__, "User")


class TestUser(unittest.TestCase):
    """Test cases for User Class"""

    def setUp(self):
        """creates a test"""
        self.test_obj = User()
        self.test_obj.email = "test@example.com"
        self.test_obj.password = "p@$$w0rd"
        self.test_obj.first_name = "John"
        self.test_obj.last_name = "Doe"

    def test_user_is_subclass_of_base_model(self):
        self.assertTrue(issubclass(User, BaseModel))

    def test_public_attributes_exist(self):
        """tests wether"""
        req_att = ["id", "created_at", "updated_at",
                   "email", "password", "first_name", "last_name"]
        for attrib in req_att:
            self.assertTrue(hasattr(self.test_obj, attrib))

    def test_public_attributes_have_correct_type(self):
        """tests wether the public"""
        req_att = ["email", "password", "first_name", "last_name"]
        for attrib in req_att:
            self.assertTrue(type(getattr(self.test_obj, attrib)), str)

    def test_bas_str_should_print_formatted_output(self):
        """__str__ should print"""
        self.test_obj.my_number = 89
        cls_name = User.__name__
        id = self.test_obj.id
        expected = f"[{cls_name}] ({id}) {self.test_obj.__dict__}"
        output = StringIO()
        sys.stdout = output
        print(self.test_obj)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue().strip("\n"), expected)

    def test_to_dict_returns_a_dictionary_of_attributes(self):
        """to_dict should
        self.__dict__
        """
        temp_dict = self.test_obj.to_dict()
        self.assertIsInstance(temp_dict, dict)
        keys = temp_dict.keys()

        for k, v in self.test_obj.__dict__.items():
            self.assertIn(k, keys)
            if not isinstance(self.test_obj.__dict__[k], datetime):
                self.assertEqual(temp_dict[k], v)

    def test_to_dict_has_a_key_with_the_class_name(self):
        """to_dict must have
        name
        """
        temp_dict = self.test_obj.to_dict()
        self.assertIn("__class__", temp_dict.keys())
        self.assertEqual(temp_dict["__class__"],
                         User.__name__)

    def test_init_with_kwargs(self):
        """test that User"""
        temp_obj_2 = User(**self.test_obj.to_dict())

        for k, v in self.test_obj.__dict__.items():
            self.assertEqual(v, temp_obj_2.__dict__[k])


if __name__ == "__main__":
    unittest.main()
