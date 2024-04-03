from django.contrib import admin
from .models import Category,Book,Payment
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","category_name")

    


class BookAdmin(admin.ModelAdmin):
    list_display =("id","book_name","price","size","description","image","category")


class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id","card_no","cvv","expiry","balance")

admin.site.register(Category,CategoryAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Payment,PaymentAdmin)