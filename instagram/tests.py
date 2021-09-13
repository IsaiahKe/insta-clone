from django.test import TestCase
from . models import User

# Create your tests here.
class Test_user(TestCase):
    def setUp(self):
        self.user=User(username='isaiahmorara',email='isaiahmorara9@gmail.com',password='isaiahmorara')
        
    
    def test_instance(self):
         self.assertIsInstance(self.user,User)
         
    def test_save(self):
        self.user.save_user()
        query=User.objects.all()
        self.assertTrue(len(query)>0)
    
        
        