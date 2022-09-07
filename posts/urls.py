from django.urls import path
from.views import main_page, test_view, post_detail_view

urlpatterns = [
    path('', main_page),
    path('posts/', test_view),
    path('posts/<int:id>/', post_detail_view),
]