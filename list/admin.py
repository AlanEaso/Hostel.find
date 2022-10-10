from django.contrib import admin

from .models import List
from .models import Near_by
from .models import Near

admin.site.register(List)

admin.site.register(Near_by)

admin.site.register(Near)
