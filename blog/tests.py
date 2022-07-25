from django.test import TestCase
from .models import Post

# Create your tests here.
class ModelTesting(TestCase):

    def setUp(self):
        #here we need create a new instance of model
        self.blog = Post.objects.create(title = 'django', author='dan', slug='dj')


    def test_post_model(self):

        d = self.blog
        self.assertTrue(d.title == 'django')
        self.assertTrue(d.slug == 'dj')
        self.assertTrue(d.author == 'dan')
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d.author), 'dan')
        self.assertEqual(str(d), 'django')
        
