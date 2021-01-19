from django.urls import path
from .views import interest_rate, price_indice, all_stats, home, redirect_stats


urlpatterns = [
    path('', redirect_stats),
    path('stats/', home),
    path('stats/interest-rates', interest_rate),
    path('stats/price-indices', price_indice),
    path('stats/all', all_stats),
]