from django.contrib import admin

from .models import Jogo, Categoria

admin.site.register([Jogo, Categoria])

