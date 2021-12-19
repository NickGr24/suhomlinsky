from django.contrib import admin

from .models import Post, PostImage

class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', ),}
    inlines = [PostImageAdmin]

 
@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass