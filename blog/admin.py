from django.contrib import admin
from .models import Post, Project

class PostInline(admin.TabularInline):
	model = Post
	extra = 3

class ProjectAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 	{'fields': ['project_field']}),
		# ('Date Information', {'fields': ['log_date'], 'classes':['collapse']}),
	]
	inlines = [PostInline]
	# list_filter = ['log_date']
	search_fields = ['project_field']
	list_display = ('project_field','total_hours')#, 'log_date')
	readonly_fields = ('total_hours',)
	def total_hours(self, obj):

		proj = Project.objects.get(id=obj.id)
		# print proj
		post=Post.objects.filter(project_field=proj)
		
		project_hours = 0
		if post:
			for v_post in post:
				project_hours += post[0].duration_time
			# print post[0].duration_time,'waaako'
			return project_hours
		else:
			return 0

	total_hours.allow_tags = True 
admin.site.register(Project, ProjectAdmin)


# Register your models here.
