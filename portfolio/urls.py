from django.urls import path
from .import views


urlpatterns = [
    path('', views.portfolio_page, name='portfolio'),
    path('message/', views.messages),

    path('details/<int:portfolio_id>', views.portfolio_details, name='portfolio-details')
]
