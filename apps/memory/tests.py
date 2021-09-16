from django.test import TestCase

from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
from .models import Memory

test_comment = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

class MemoryTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='usr_test', email='usr_test@gmail.com')

    def test_insertion_retrieval(self):
        usr = User.objects.get(username="usr_test", email="usr_test@gmail.com") 
        Memory.objects.create(
            name="Place_1_test",
            comment=test_comment,
            location=Point(99,1),
            author=usr,
        )
        Memory.objects.create(
            name="Place_2_test",
            comment=test_comment,
            location=Point(88,2),
            author=usr,
        )
        Memory.objects.create(
            name="Place_3_test",
            comment=test_comment,
            location=Point(77,3),
            author=usr,
        )
        list_mem = Memory.objects.filter(author=usr)
        self.assertEqual(len(list_mem), 3)