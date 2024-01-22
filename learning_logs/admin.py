from django.contrib import admin

from learning_logs.models import Topic, Entry

admin.site.register(Topic)#tells Django to manage our model through the admin site
admin.site.register(Entry)

# Register your models here.
