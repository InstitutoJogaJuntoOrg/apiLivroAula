from django.contrib import admin
from .models import Author, Gender, Books

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'gender',)
    search_fields = ('title', 'author__name', 'gender__name',)
    list_filter = ('author', 'gender',)
    ordering = ('title',)
