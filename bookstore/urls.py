from django.urls import path
from . import views

urlpatterns = [
    path("api/books",views.allbooks,name="Allbooks"),
    path("api/books/<int:book_id>",views.book,name="Book"),
]
