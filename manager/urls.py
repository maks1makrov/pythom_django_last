
from django.urls import path


from manager import views
from manager.views import hello

urlpatterns = [
    path('hello/<int:digit>', hello),
    path('hello/<str:name>', hello),
    path('hello/', hello),
    path('', views.MyBook.as_view(), name='mybook'),
]
