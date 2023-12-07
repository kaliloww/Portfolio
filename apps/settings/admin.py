from django.contrib import admin
from apps.settings.models import InfoUser,About, Skills, Work, Education
# Register your models here.
admin.site.register(InfoUser)
admin.site.register(About)
admin.site.register(Skills)
admin.site.register(Work)
admin.site.register(Education)
