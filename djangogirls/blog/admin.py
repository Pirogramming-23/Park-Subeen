from django.contrib import admin
from .models import Post #  앞 장에서 정의했던 Post모델 가져오기

# Register your models here.

admin.site.register(Post)