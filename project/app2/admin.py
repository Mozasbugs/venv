from pydoc import doc
from django.contrib import admin
from .models import Doc
from .models import Patient
# Register your models here.

admin.site.register(Doc)
admin.site.register(Patient)

