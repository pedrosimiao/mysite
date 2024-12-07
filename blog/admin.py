from django.contrib import admin

# Register your models here.
# It actually searches for the models in the __init__.py file
# So make sure that you have imported every model in it.
from .models import Post
