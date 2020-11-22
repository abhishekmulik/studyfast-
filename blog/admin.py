from django.contrib import admin

# Register your models here.
from blog.models import Post,Comment,Category,SubjectList
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(SubjectList)
admin.site.register(Category)
# admin.site.register(Category)

