from rest_framework import serializers
from library.models import LibraryBook, Library, Book, LibraryActivity, UserLibrary


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UserLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLibrary
        fields = '__all__'


class LibraryBookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LibraryBook
        fields = ['library', 'book']


class LibraryActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryActivity
        fields = '__all__'