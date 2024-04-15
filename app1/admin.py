from django.contrib import admin
from .models import Profile, Servies, Blog, Catigory, Skils, About, Project,Tool

admin.site.register(Tool)

@admin.register(Profile)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (  'id', 'full_name' ,)
    list_display_links = ('id', 'full_name',)
    search_fields = ( 'id', 'full_name' ,)
    list_filter = (  'id', 'full_name' ,)

@admin.register(Servies)
class ServiesAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'order', )
    list_editable = ('order',)
    search_fields = ('name', 'order',)
    list_filter =  ( 'name', 'order', )

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'punlished_at', 'author', )
    list_display_links = ( 'title', 'author',)
    list_filter = ( 'title', 'punlished_at', 'author',)
    search_fields = ('author', 'title', 'punlished_at', )


@admin.register(Catigory)
class CatigoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter  =( 'name',)

@admin.register(Skils)
class SkilsAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'percentage','order' ,)
    list_display_links = ( 'name',)
    search_fields = ( 'name', 'percentage','order',)
    list_editable = ( 'percentage','order',)
    list_filter = ( 'name', 'percentage','order' ,)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('amount', 'project_count', 'customer_count',)
    search_fields = ('amount', 'project_count', 'customer_count',)
    list_display_links = ('amount', 'project_count', 'customer_count',)
    list_filter = ('amount', 'project_count', 'customer_count',)
    # list_editable = ( 'project_count', 'customer_count',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','Catigory_id',)
    list_display_links = ('name','Catigory_id',)
    search_fields = ('name','Catigory_id',)
    list_filter = ('name','Catigory_id',)










