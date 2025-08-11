from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    model = Person
    list_display = ('username', 'email', 'telefono', 'direccion')
    search_fields = ['user__username', 'user__email']  # búsqueda en campos relacionados
    list_select_related = ('user',)  # optimiza consultas

    def username(self, obj):
        return obj.user.username
    username.admin_order_field = 'user__username'
    username.short_description = 'Username'

    def email(self, obj):
        return obj.user.email
    email.admin_order_field = 'user__email'
    email.short_description = 'Email'

admin.site.register(Person, PersonAdmin)
