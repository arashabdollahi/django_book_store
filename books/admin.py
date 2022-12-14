from django.contrib import admin

from .models import Book, Comment

admin.site.register(Book)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'text', 'datetime_create',)

# admin.site.register(Comment, CommentAdmin)
