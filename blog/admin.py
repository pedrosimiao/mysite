from django.contrib import admin

# Register your models here.
# It actually searches for the models in the __init__.py file
# So make sure that you have imported every model in it.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)