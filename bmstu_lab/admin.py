from django.contrib import admin
from .models import Groups
from .models import Students
from .models import Subscriptions
from .models import Timetable
from .models import Trainers
admin.site.register(Groups)
admin.site.register(Students)
admin.site.register(Subscriptions)
admin.site.register(Timetable)
admin.site.register(Trainers)
# Register your models here.

