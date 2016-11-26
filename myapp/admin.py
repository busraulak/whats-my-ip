from django.contrib import admin
<<<<<<< HEAD
from myapp.models import (Book, Author)


class BookAdmin(admin.ModelAdmin):
    pass
    list_display = ('title', 'lc_classification')

class AuthorAdmin(admin.ModelAdmin):
    pass
    list_display = ('name', 'surname', 'date_of_birth')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
# Register your models here
=======

# Register your models here.
>>>>>>> 47e9abd8d7de15ddd040ba0b45410a37684185af
