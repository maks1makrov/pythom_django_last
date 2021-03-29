from django.contrib import admin

from manager.models import Book, Comment


class CommentAdmin(admin.StackedInline):
    model = Comment

class BookAdmin(admin.ModelAdmin):
    inlines = [CommentAdmin]


admin.site.register(Book, BookAdmin)
