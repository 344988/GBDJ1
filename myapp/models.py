from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='product_photos/', default='path/to/default/image.jpg')

    @classmethod
    def create(cls, name, description, price, quantity):
        if cls.objects.filter(name=name).exists():
            raise ValueError("A product with this name already exists")
        return cls.objects.create(
            name=name,
            description=description,
            price=price,
            quantity=quantity
        )

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, customer, products, total_amount=None):
        order = cls(customer=customer)
        order.save()

        for product in products:
            order.products.add(product)

        if total_amount is not None:
            order.total_amount = total_amount
        else:
            # Automatic calculation of the total amount
            order.total_amount = sum(p.price for p in products)

        order.save()
        return order

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"


class Article(models.Model):

    title = models.CharField(max_length=200)
    text = models.TextField()
    # Дополнительные поля, например, дата публикации, автор и т.д.

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_modified(self):
        return self.created_at != self.updated_at

    def __str__(self):
        return f"Comment by {self.author} on {self.article}"