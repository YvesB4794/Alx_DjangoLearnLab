from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Book, Bookshelf

# CustomUser creation form
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_photo')

# CustomUser change form
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_photo', 'is_active', 'is_staff', 'is_superuser')

# CustomUser admin class
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

# Register CustomUser with its admin
admin.site.register(CustomUser, CustomUserAdmin)


# Register other models as usual
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'added_by')
    list_filter = ('author', 'added_by')
    search_fields = ('title', 'author')

@admin.register(Bookshelf)
class BookshelfAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner')
    list_filter = ('owner',)
    search_fields = ('name',)
