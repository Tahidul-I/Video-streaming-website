from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from streaming.models import Item,comment
# Register your models here.
admin.site.register(Item)
admin.site.register(comment)