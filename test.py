from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from book.models import Books, Gender, Author


# class BookTests(APITestCase):
#     def test_create_book(self):
#         url = reverse('books')
#         data = {'title': 'My Book', 'author': 1, 'gender': 1}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Books.objects.count(), 1)
#         self.assertEqual(Books.objects.get().title, 'My Book')
    


class GenderTests(APITestCase):
    def test_create_gender(self):
        url = reverse('genders-list')
        data = {'name': 'Suspense'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Gender.objects.count(), 1)
        self.assertEqual(Gender.objects.get().name, 'Suspense')
        
# class AuthorTests(APITestCase):
#     def test_create_author(self):
#         url = reverse('authors')
#         data = {'name': 'Matheus Geambastiane'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Author.objects.count(), 1)
#         self.assertEqual(Author.objects.get().name, 'Matheus Geambastiane')
    
