"""testing the console"""
import unittest
from unittest.mock import patch, Mock
from io import StringIO
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """theee console"""

    @classmethod
    def setUpClass(cls):
        """consolee"""
        cls.console = HBNBCommand()

    def setUp(self):
        """cons3ole"""
        storage._FileStorage__objects = {}

    def create_mock_storage(self):
        """conso3le"""
        mock_storage = Mock()
        mock_storage.all = Mock(return_value={})
        mock_storage.save = Mock()
        mock_storage.reload = Mock()
        return mock_storage

    def test_default_invalid_command(self):
        """consol3e"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.default("invalid_command")
    self.assertEqual(fake_output.getvalue().strip(), "** invalid command **")

    def test_default_invalid_syntax(self):
        """console3"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.default("User.show()")
    self.assertEqual(fake_output.getvalue().strip(), "** invalid command **")

    def test_default_non_existing_class(self):
        """console3"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.default("NonExistent.show(\"1234\")")
    self.assertEqual(fake_output.getvalue().strip(), "** class doesn't exist **")

    def test_default_show(self):
        """console3"""
        obj = BaseModel()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.default(f"BaseModel.show(\"{obj.id}\")")
            self.assertIn(obj.id, fake_output.getvalue().strip())

    def test_do_create_no_class(self):
        """console3"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.do_create("")
            self.assertEqual(fake_output.getvalue().strip(), "** class name missing **")

    def test_do_create_invalid_class(self):
        """console3"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.do_create("MyModel")
            self.assertEqual(fake_output.getvalue().strip(), "** class doesn't exist **")

    def test_do_create_success(self):
        """console3"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.do_create("BaseModel")
            self.assertRegex(fake_output.getvalue().strip(), "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")

    def test_do_show_no_class(self):
        """console3"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.do_show("")
            self.assertEqual(fake_output.getvalue().strip(), "** class name missing **")

    def test_do_show_no_instance_id(self):
        """console3"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.do_show("User")
            self.assertEqual(fake_output.getvalue().strip(), "** instance id missing **")

    def test_do_show_nonexistent(self):
        """console3"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.do_show(f"BaseModel 12345")
            self.assertEqual(fake_output.getvalue().strip(), "** no instance found **")

    def test_do_destroy_no_class(self):
        """console3"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.do_destroy("")
            self.assertEqual(fake_output.getvalue().strip(), "** class name missing **")

    def test_do_destroy_no_instance_id(self):
        """console3"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.do_destroy("User")
            self.assertEqual(fake_output.getvalue().strip(), "** instance id missing **")

    def test_do_destroy_nonexistent(self):
        """console3"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.do_destroy(f"BaseModel 12345")
            self.assertEqual(fake_output.getvalue().strip(), "** no instance found **")

    def test_do_count_valid_class(self):
        """consol3e"""
        BaseModel()
        BaseModel()
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.do_count("BaseModel")
            self.assertEqual(fake_output.getvalue().strip(), "2")

    def test_do_count_invalid_class(self):
        """console3"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.do_count("MyModel")
            self.assertEqual(fake_output.getvalue().strip(), "** class doesn't exist **")

    def test_do_update_no_class(self):
        """console3"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.do_update("")
            self.assertEqual(fake_output.getvalue().strip(), "** class name missing **")

    def test_do_update_no_instance_id(self):
        """console3"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.do_update("BaseModel")
            self.assertEqual(fake_output.getvalue().strip(), "** instance id missing **")

    def test_do_update_no_attribute_name(self):
        """console3"""
        obj = BaseModel()
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.do_update(f"BaseModel {obj.id}")
    self.assertEqual(fake_output.getvalue().strip(), "** attribute name missing **")

    def test_do_update_no_value(self):
        """console"""
        obj = BaseModel()
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.console.do_update(f"BaseModel {obj.id} name")
self.assertEqual(fake_output.getvalue().strip(), "** value missing **")


if __name__ == '__main__':
    unittest.main()
