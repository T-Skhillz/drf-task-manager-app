from django.contrib import admin
from .models import Task

class TaskModelAdmin(admin.ModelAdmin):
    list_display = ("user","title", "completed", "created_at")
    list_filter = ["completed", "created_at"]
    search_fields = ["title", "completed"]

admin.site.register(Task, TaskModelAdmin)
