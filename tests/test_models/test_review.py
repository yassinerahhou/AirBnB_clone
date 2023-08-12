#!/usr/bin/python3
"""Module test_review

tests for Review Class
"""

import sys
import unittest
import uuid
from datetime import datetime
from io import StringIO

import pycodestyle
from models import review
from tests.test_models.test_base_model import BaseModel

Review = review.Review


class TestReviewDocsAndStyle(unittest.TestCase):
    """Tests Review"""

    def test_pycodestyle(self):
        """Tests compliance"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/review.py", "tests/test_models/test_review.py"])
        self.assertEqual(result.total_errors, 0)

    def test_module_docstring(self):
        """Tests whether """
        self.assertTrue(len(review.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests whether"""
        self.assertTrue(len(Review.__doc__) >= 1)

    def test_class_name(self):
        """Test whether"""
        self.assertEqual(Review.__name__, "Review")


class TestReview(unittest.TestCase):
    """Review Class"""

    def setUp(self):
        """creates a test object"""
        self.test_obj = Review()
        self.test_obj.place_id = str(uuid.uuid4())
        self.test_obj.user_id = str(uuid.uuid4())
        self.test_obj.text = "fantastic review"

    def test_review_is_subclass_of_base_model(self):
        self.assertTrue(issubclass(Review, BaseModel))

    def test_public_attributes_exist(self):
        """tests wether the public."""
        req_att = ["id", "created_at", "updated_at",
                   "place_id", "user_id", "text"]
        for attrib in req_att:
            self.assertTrue(hasattr(self.test_obj, attrib))

    def test_public_attributes_have_correct_type(self):
        """tests wether the public."""
        req_att = ["place_id", "user_id", "text"]
        for attrib in req_att:
            self.assertTrue(type(getattr(self.test_obj, attrib)), str)

    def test_bas_str_should_print_formatted_output(self):
        """__str__ should print"""
        self.test_obj.my_number = 89
        cls_name = Review.__name__
        id = self.test_obj.id
        expected = f"[{cls_name}] ({id}) {self.test_obj.__dict__}"
        output = StringIO()
        sys.stdout = output
        print(self.test_obj)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue().strip("\n"), expected)

    def test_to_dict_returns_a_dictionary_of_attributes(self):
        """to_dict should return
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
        """to_dict must have a key
        name
        """
        temp_dict = self.test_obj.to_dict()
        self.assertIn("__class__", temp_dict.keys())
        self.assertEqual(temp_dict["__class__"],
                         Review.__name__)

    def test_init_with_kwargs(self):
        """test that Review"""
        temp_obj_2 = Review(**self.test_obj.to_dict())

        for k, v in self.test_obj.__dict__.items():
            self.assertEqual(v, temp_obj_2.__dict__[k])


if __name__ == "__main__":
    unittest.main()
