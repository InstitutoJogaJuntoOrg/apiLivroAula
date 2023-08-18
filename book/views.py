from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Author, Gender, Books
from .serializers import AuthorSerializer, GenderSerializer, BooksSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class GenderViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer

class BooksViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
