from unicodedata import category
import unittest
from app.models import User,Pitch,Comment,Upvote,Downvote

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(id='1',title='Test-title',pitch='test-post',category='test-category', pitch_id=1,user_id=1)
        self.new_user = User(id='1',username='Luar',email='luar@gmail.com',password='luar34',bio='I love music')
        self.new_comment = Comment(text='Awesome idea',pitch_id=1,user_id=1)
        self.new_upvote = Upvote(pitch_id=1,author='Luar',user_id=1)
        self.new_downvote = Downvote(pitch_id=1,author='Luar',user_id=1)
    
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))
        self.assertTrue(isinstance(self.new_user, User))
        self.assertTrue(isinstance(self.new_comment, Comment))
        self.assertTrue(isinstance(self.new_upvote, Upvote))
        self.assertTrue(isinstance(self.new_downvote, Downvote))


