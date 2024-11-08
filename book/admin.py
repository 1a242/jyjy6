from django.contrib import admin
from .models import Book, Review1

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title','description')
    search_fields = ['title','description']
    list_editable = ('title','description',)                #修改字段

admin.site.register(Book,BookAdmin)
admin.site.register(Review1)