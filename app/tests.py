from django.test import TestCase
from .models import Book


class BookTest(TestCase):
    """ Test module for Book model """

    def setUp(self):
        Book.objects.create(
            title='Rich dad Poor dad',
            author="Robert",
            price=299,
            quantity_in_stock=100,
            genre="Self Help",
            isbn="978-0-596-52068-2"
        )

    def test_book(self):
        book = Book.objects.get(title='Rich dad Poor dad')
        self.assertEqual(
            book.get_title(),
            "Rich dad Poor dad"
        )
