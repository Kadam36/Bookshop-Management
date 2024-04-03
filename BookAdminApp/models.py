from django.db import models

# Create your models here.
class Category(models.Model):
        category_name = models.CharField(max_length=20)
     
        def __str__(self):
          return self.category_name 
        class Meta():
            db_table = "Category"

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    price = models.FloatField(default=200)
    description = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    image =  models.ImageField(upload_to="image",default="abc.jpg")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


    
    class Meta():
        db_table = "Book" 


        


class Payment(models.Model):
    card_no = models.CharField(max_length=20)
    cvv =  models.CharField(max_length=4)
    expiry =  models.CharField(max_length=10)
    balance = models.FloatField(default=10000)

    class Meta:
        db_table = "Payment"


        


