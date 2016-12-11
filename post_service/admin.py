from django.contrib import admin

# Register your models here.
from post_service.models import Post

admin.site.register(Post)