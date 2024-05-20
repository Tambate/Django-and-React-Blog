from django.contrib import admin
from .models import category, blog

#tu dong add text tu truong title vao slug va them gach ngang
class blogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}

admin.site.register(category)
admin.site.register(blog, blogAdmin)
