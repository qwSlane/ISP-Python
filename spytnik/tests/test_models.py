from django.contrib.auth.models import User
from django.test import TestCase
from spytnik.models import Post, PostDescription, Genre, Vote


class GenreModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(name="QWE", slug='qwe')

    def test_name_label(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        genre = Genre.objects.get(id=1)
        max_length = genre._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)

    def test_to_str(self):
        genre = Genre.objects.get(id=1)
        expected_object_name = genre.name
        self.assertEquals(expected_object_name, str(genre))


class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        auth = User.objects.create_user(username='qwa', password='123')
        genres = [Genre.objects.create(name="tt", slug="tTT"), Genre.objects.create(name="qw", slug="wq")]
        auth.save()
        post = Post.objects.create(author=auth, title='title', image='null',
                                       text='title', slug="testt")
        post.save()
        post.genre.set(genres)

    def test_name_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_name_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_to_str(self):
        post = Post.objects.get(id=1)
        expected_object_name = post.title
        self.assertEquals(expected_object_name, str(post))


class VoteModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        auth = User.objects.create_user(username='qwa', password='123')
        genres = [Genre.objects.create(name="tt", slug="tTT"), Genre.objects.create(name="qw", slug="wq")]
        post = Post.objects.create(author=auth, title='title', image='null',
                                   text='title', slug="testt")
        post.save()
        post.genre.set(genres)
        vote = Vote.objects.create(value=3, user=auth, post=post)
        vote.save()

    def test_name_label(self):
        vote = Vote.objects.get(id=1)
        field_label = vote._meta.get_field('value').verbose_name
        self.assertEqual(field_label, 'value')




