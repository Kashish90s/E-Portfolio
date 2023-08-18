from django.contrib import admin
from interface.models import AboutMe, Experience, Education,SocialLink, Skill,Projects

# Register your models here.
admin.site.register(AboutMe),
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(SocialLink)
admin.site.register(Projects)