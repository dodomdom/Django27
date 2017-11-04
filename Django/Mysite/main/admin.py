from django.contrib import admin

# Register your models here.

from .models import Post

class PostModelAdmin(admin.ModelAdmin):


	list_display = ["classify", "title", "updated", "timestamp"]
	list_display_links = ["updated"]
	list_editable = ["title"]
	list_filter = ["updated", "timestamp"]
	search_fields = ["title", "content"]

	class meta:
		model = Post
admin.site.register(Post, PostModelAdmin);