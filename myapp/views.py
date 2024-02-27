from django.shortcuts import render, redirect
import logging
from .models import Article, Customer
from django.utils import timezone
from datetime import timedelta
from .models import Order
from .forms import CommentForm
from .forms import ProductForm
from .models import Product

logger = logging.getLogger(__name__)

def home_view(request):
    logger.info("Главная страница посещена")
    return render(request, 'home.html')

def about_view(request):
    logger.info("Страница 'О себе' посещена")
    return render(request, 'about.html')

def article_view(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article_view', article_id=article_id)
    else:
        form = CommentForm()

    return render(request, 'article_template.html', {'article': article, 'form': form})

def customer_orders_view(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    return render(request, 'orders_template.html', {'customer': customer})

def ordered_products_view(request, customer_id, days):
    end_date = timezone.now()
    start_date = end_date - timedelta(days=days)
    orders = Order.objects.filter(customer_id=customer_id, order_date__range=(start_date, end_date))

    products = set()
    for order in orders:
        for product in order.products.all():
            products.add(product)

    return render(request, 'ordered_products_template.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('some-view-name')  # замените 'some-view-name' на имя вашего представления
    else:
        form = ProductForm()

    return render(request, 'your_app/add_product.html', {'form': form})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})