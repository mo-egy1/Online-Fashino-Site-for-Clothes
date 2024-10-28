from django.db import models
from user.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Category (models.Model):
    name = models.CharField(max_length=225)
    
    def __str__(self) -> str:
        return self.name

class Model (models.Model) :
    name = models.CharField(max_length=225)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='pd_category')
    model = models.ForeignKey(Model,on_delete=models.CASCADE,related_name='pd_model')
    title = models.CharField(max_length=225)
    description = models.TextField()
    image = models.ImageField(upload_to='pd-imgs/')
    price = models.FloatField(default=0)
    stars = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    def __str__(self) : 
        return self.title
    
    def get_stars (self) :
        stars = [
            '<i class="fa-regular  fa-star text-lg text-yellow-400"></i>' 
            for i in range(5)
        ]

        for i in range(0,self.stars) :
            stars[i] = '<i class="fa-solid fa-star text-lg text-yellow-400"></i>'

        return ' '.join(stars)


class Cart (models.Model) : 
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_cart')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cart_pd')
    amount = models.PositiveIntegerField(default=1)

    @staticmethod
    def get_total_price(for_user) :
        cart = Cart.objects.filter(user=for_user)
        total = sum([ i.product.price * i.amount for i in cart])
        return total


    @property
    def get_price (self) : 
        return self.amount * self.product.price