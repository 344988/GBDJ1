from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def home_view(request):
    logger.info("Главная страница посещена")
    return render(request, 'home.html')

def about_view(request):
    logger.info("Страница 'О себе' посещена")
    return render(request, 'about.html')
