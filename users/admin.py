from django.contrib import admin
from .models import Person

# Register your models here.
class userAdmin(admin.ModelAdmin):
    model = Person
    list_display = ('nombre', 'correo', 'telefono', 'direccion')
    search_fields = ['username', 'email']

admin.site.register(Person, userAdmin)