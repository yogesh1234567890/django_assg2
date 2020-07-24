from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'username')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','username', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    # def _allow_edit(self, obj=None):
    #     if not obj:
    #         return True
    #     return not (obj.is_staff or obj.is_superuser)
    #
    # def has_change_permission(self, request, obj=None):
    #     return self._allow_edit(obj)
    #
    # def has_delete_permission(self, request, obj=None):
    #     return self._allow_edit(obj)
    #
    # def has_add_permission(self, request):
    #     return True
    #
    # def has_view_permission(self, request, obj=None):
    #     return True

    # def has_module_permission(self, request):
    #     return True

admin.site.register(get_user_model(), CustomUserAdmin)