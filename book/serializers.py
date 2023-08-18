from rest_framework import serializers
from .models import Author, Gender, Books

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'

class BooksSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(write_only=True)
    gender_name = serializers.CharField(write_only=True)

    # import ipdb; ipdb.set_trace()
    class Meta:
        model = Books
        fields = ['title', 'author_name', 'gender_name', 'description', 'author', 'gender']

    def create(self, validated_data):
        author_name = validated_data.pop('author')
        gender_name = validated_data.pop('gender')

        author, _ = Author.objects.get_or_create(name=author_name)
        gender, _ = Gender.objects.get_or_create(title=gender_name)

        book = Books.objects.create(author=author, gender=gender, **validated_data)
        return book