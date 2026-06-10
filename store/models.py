from django.db import models

class Collection(models.Model):
    title = models.CharField(max_length=255)

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    #assuming the max price gonna be 9999.99
    price = models.DecimalField(max_digits=4,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    #so v mae on_delete to PROTECT cause if v accidentally deleted a collection we dont want it to delete the whole product
    collection = models.ForeignKey(Collection,on_delete=models.PROTECT)

class Customer(models.model):
    #so y v did this is cause if v gonna change the default choice later v gonna be needing to modify in multipl places so creating a constant var helps
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"
    #v are creting this choices cause v planning on making a dropdown and the full ("bronze" "silver""gold") is for user readabiity
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, "bronze"),
        (MEMBERSHIP_SILVER, "silver"),
        (MEMBERSHIP_GOLD, "gold")
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE)

class Cart(models.Model):
    creted_at= models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

class Order(models.Model):
    PAYMENT_PENDING = "P"
    PAYMENT_FAILED = "F"
    PAYMENT_COMPLETED = "C" 

    PAYMENT_STATUS_CHOICE = [
        (PAYMENT_PENDING,"pending"),
        (PAYMENT_COMPLETED,"completed"),
        (PAYMENT_FAILED,"failed")
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1,choices=PAYMENT_STATUS_CHOICE,default=PAYMENT_PENDING)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product =  models.ForeignKey(Product,on_delete=models.PROTECT)  
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)

class Address(models.Model):
    street = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)
#    so v are creting a one to one connection btw customer and the address class(table)
#    OneTOOneField has some required parameters
#   1. TO type = which basically says "on which class(table) are u attaching this onetoOne connection" so we added "Customer" whis is the class(table) name
#   2. on_delete = what happens when we delete the parent class(customer)..so there are multiple things but we added "CASCADE" which deletes the child class when the parent is deleted
#   3. primary_key = we gonna make it the primary_key.
#      if not then djangop gonna crete an id field for each address and it gonna become an OneTOMany realationship
    

#   we dont have to create a reverse relation on the customer class django gonna create it for uss
