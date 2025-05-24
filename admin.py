
from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(section)
admin.site.register(sports)
admin.site.register(sportsImage)
admin.site.register(sportsvideo)
admin.site.register(sportadvice)
admin.site.register(sportsclub)
admin.site.register(feedadvice)
admin.site.register(feedImage)
admin.site.register(feed)
admin.site.register(physicalCenter)
admin.site.register(physicaladvice)
admin.site.register(physicalvideo)
admin.site.register(physicalImage)
admin.site.register(physicalTherapy)
