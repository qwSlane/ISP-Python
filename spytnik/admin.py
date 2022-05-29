from django.contrib import admin

from .models import Post, Genre, PostDescription, Pleb, Vote


class PostDescriptionInline(admin.StackedInline):
    model = PostDescription
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "published_date"]
    inlines = [PostDescriptionInline]


admin.site.register(PostDescription)
admin.site.register(Genre)
admin.site.register(Pleb)
admin.site.register(Vote)

