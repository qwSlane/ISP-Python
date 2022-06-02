from django.contrib.auth.models import User
from django.test import TestCase
from spytnik.models import Post, PostDescription, Genre, Vote
from django.urls import reverse


class PostListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_authors = 13
        auth = User.objects.create_user(username='qwa', password='123')
        auth.save()
        for author_num in range(number_of_authors):
            Post.objects.create(author=auth, title='title %s' % author_num, image='null',
                                text='title %s' % author_num, slug=author_num)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('info')
        self.assertEqual(resp.status_code, 404)


class HomeListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_authors = 13
        auth = User.objects.create_user(username='qwa', password='123')
        genres = [Genre.objects.create(name="tt",slug="tTT"), Genre.objects.create(name="qw",slug="wq")]
        auth.save()
        for author_num in range(number_of_authors):
            post = Post.objects.create(author=auth, title='title %s' % author_num, image='null', text='title %s' % author_num, slug=author_num)
            post.save()
            post.genre.set(genres)

    def test_post(self):
        resp = self.client.post(reverse('home'), {'username': 'userT', 'password': 'pass'})
        print(resp)
        self.assertEqual(resp.status_code, 400)

    def test_post_2(self):
        resp = self.client.post(reverse('home'), {'username': 'qwa', 'password': '123'})
        print(resp)
        self.assertEqual(resp.status_code, 201)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, "spytnik/index.html")

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
