#from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from .models import CustomUser

#class CustomUserCreationForm(UserCreationForm):
#    class Meta(UserCreationForm.Meta):
#        model = CustomUser
#       fields = ('username', 'email', 'profile_photo')

#class CustomUserChangeForm(UserChangeForm):
#    class Meta(UserChangeForm.Meta):
#        model = CustomUser
#        fields = ('username', 'email', 'profile_photo', 'is_active', 'is_staff', 'is_superuser')

#class CustomUserAdmin(UserAdmin):
#   add_form = CustomUserCreationForm
#   form = CustomUserChangeForm
#   model = CustomUser

#   list_display = ('username', 'email', 'is_staff', 'is_active')
#   list_filter = ('is_staff', 'is_active', 'is_superuser')

#   fieldsets = (
#       (None, {'fields': ('username', 'email', 'password')}),
#       ('Personal info', {'fields': ('profile_photo', 'bio')}),
#       ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
#       ('Important dates', {'fields': ('last_login', 'date_joined')}),
#   )

#   add_fieldsets = (
#       (None, {
#           'classes': ('wide',),
#           'fields': ('username', 'email', 'profile_photo', 'password1', 'password2', 'is_staff', 'is_active')}
#       ),
#   )

#admin.site.register(CustomUser, CustomUserAdmin)


#from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
#from .models import CustomUser

#admin.site.register(CustomUser, UserAdmin)






# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_photo')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_photo', 'is_active', 'is_staff', 'is_superuser')

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser')

    fieldsets = UserAdmin.fieldsets + (
        ('Additional info', {'fields': ('date_of_birth', 'profile_photo', 'bio')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'date_of_birth', 'profile_photo', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)
