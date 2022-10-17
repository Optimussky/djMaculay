from django.contrib import admin
from .models import Resume, Post


class PostAdmin(admin.ModelAdmin):
    # https://docs.djangoproject.com/en/4.1/ref/contrib/admin/
    list_display = ('title','author','date',)

    # https://juhanajauhiainen.com/posts/customize-django-admin-with-list-display-property
    def chanchito(self, obj: Post)-> str:
        return f"{obj.author.upper()}"

# Register your models here.
admin.site.register(Resume)
admin.site.register(Post,PostAdmin)