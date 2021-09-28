from django.db import models

activities_types = (
    ('RENT', 'rent'),
    ('BUY', 'buy'),
    ('RETURN', 'return')
)


#  everything except name should by a reference.
class Library(models.Model):
    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    isbn_num = models.CharField(max_length=20, unique=True)
    genre = models.CharField(max_length=50)
    description = models.TextField()

    # only one book in each library
    class Meta:
        unique_together = ('title', 'author_name',)

    def __str__(self):
        return self.title


class UserLibrary(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class LibraryBook(models.Model):
    library = models.ForeignKey(Library, on_delete=models.DO_NOTHING, related_name='libraries_books')
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, related_name='libraries_books')
    last_library_activity = models.ForeignKey('LibraryActivity', on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f'{self.book} in {self.library}'

    # only one book in each library
    class Meta:
        unique_together = ('library', 'book',)


class LibraryActivity(models.Model):
    library_book = models.ForeignKey(LibraryBook, on_delete=models.DO_NOTHING, related_name='activities')
    activity_type = models.CharField(max_length=50, choices=activities_types)
    checked_out_at = models.DateTimeField(null=True,auto_now_add=True)
    checked_in_at = models.DateTimeField(null=True)
    user = models.ForeignKey(UserLibrary, on_delete=models.DO_NOTHING,  related_name='users')

    def __str__(self):
        return f'{self.activity_type} {self.library_book}'
