from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from blog.views import home_page, article_page
from blog.models import Article
from datetime import datetime, timezone


class ArticlePageTest(TestCase):

    def test_article_page_displays_correct_article(self):
        Article.objects.create(
            title='title 1',
            full_text='full text 1',
            summary='summary 1',
            category='category 1',
            pubdate=datetime.now(timezone.utc),
            slug='slug-1',
        )

        request = HttpRequest()
        response = article_page(request, 'slug-1')
        html = response.content.decode('utf8')

        self.assertIn('title 1', html)
        self.assertNotIn('summary 1', html)
        self.assertIn('full text 1', html)


class HomePagetest(TestCase):

    def test_home_page_displays_articles(self):
        Article.objects.create(
            title='title 1',
            full_text='full text 1',
            summary='summary 1',
            category='category 1',
            pubdate=datetime.now(timezone.utc),
            slug='slug-1',
        )
        Article.objects.create(
            title='title 2',
            full_text='full text 2',
            summary='summary 2',
            category='category 2',
            pubdate=datetime.now(timezone.utc),
            slug='slug-2',
        )

        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        self.assertIn('title 1', html)
        self.assertIn('/blog/slug-1', html)
        self.assertIn('summary 1', html)
        self.assertNotIn('full text 1', html)

        self.assertIn('title 2', html)
        self.assertIn('/blog/slug-2', html)
        self.assertIn('summary 2', html)
        self.assertNotIn('full text 2', html)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Site NeDorazymenue</title>', html)
        self.assertIn('<h1>NeDorazymenue</h1>', html)
        self.assertTrue(html.endswith('</html>'))


class ArticleModelTest(TestCase):

    def test_article_model_save_and_retrieve(self):
        # создай статью 1
        article1 = Article(
            title='title 1',
            full_text='full text 1',
            summary='summary 1',
            category='category 1',
            pubdate=datetime.now(timezone.utc),
            slug='slug-1',
        )
        # сохрани статью 1 в базе
        article1.save()
        # создай статью 2
        article2 = Article(
            title='title 2',
            full_text='full text 2',
            summary='summary 2',
            category='category 2',
            pubdate=datetime.now(timezone.utc),
            slug='slug-2'
        )
        # сохрани статью 2 в базе
        article2.save()        
        # загрузи из базы все статьи
        articles = Article.objects.all()
        # проверь: статьи должно быть 2 
        self.assertEqual(len(articles), 2) 
        # проверь 1 загруженная статья == статья 1
        self.assertEqual(
            articles[0].title,
            article1.title
            )
        # проверь: 2 загруженная из базы статья == статья 2
        self.assertEqual(
            articles[1].title,
            article2.title
            )
