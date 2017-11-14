from django.test import TestCase
from .models import Editor,Article,tags

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.editor= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

    

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.editor,Editor))