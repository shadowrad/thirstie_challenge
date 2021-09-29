from django.test import TestCase
from rest_framework.test import APIRequestFactory

from library.models import Library, Book, LibraryBook, UserLibrary


def create_users(quantity):
    for i in range(quantity):
        UserLibrary.objects.create(
            name=f'user {i}',
        )


def create_libraries(quantity):
    for i in range(quantity):
        Library.objects.create(
            name=f'lib{i}',
            city=f'city{i}',
            state='state_test',
            postal_code='postal_test'
        )


def create_books(quantity):
    for i in range(quantity):
        Book.objects.create(
            title=f'title{i}',
            author_name='testbook{i}',
            isbn_num=f'isbn_num_test{i}',
            genre='testbook',
            description='')


def relate_libraries_books():
    for book in Book.objects.all():
        for library in Library.objects.all():
            LibraryBook.objects.create(
                library=library,
                book=book
            )


# Create your tests here.
class ActivityTestCase(TestCase):
    def setUp(self):
        create_users(3)
        create_books(3)
        create_libraries(3)
        relate_libraries_books()

    def test_checkout_checkin(self):
        response = self.client.post('/LibraryActivity/', data={
            "activity_type": "RENT",
            "library_book": 1,
            "user": 1
        })
        self.assertIsNotNone(response.data['checked_out_at'])
        self.assertIsNone(response.data['checked_in_at'])

    def test_checkin(self):
        response = self.client.post('/LibraryActivity/', data={
            "activity_type": "RENT",
            "library_book": 1,
            "user": 1
        })
        response = self.client.patch(f'/LibraryActivity/{response.data["id"]}/', content_type='application/json', )
        self.assertIsNotNone(response.data['checked_out_at'])
        self.assertIsNotNone(response.data['checked_in_at'])

