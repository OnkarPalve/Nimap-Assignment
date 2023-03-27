from django.contrib import admin
from api.models import Client,Project
# Register your models here..

class ClientAdmin(admin.ModelAdmin):
    list_display=('client_name','created_at','created_by')
    search_fields=('client_name',)   
    
class ProjectAdmin(admin.ModelAdmin):
    list_display=('project_name','created_at','created_by')
    list_filter=('project_name',)

admin.site.register(Client,ClientAdmin)
admin.site.register(Project,ProjectAdmin)