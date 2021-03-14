from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index,name="index"),
    path('insert',views.insert,name="insert"),
    path('delete/<int:id>',views.delete,name="delete"),
    # path('update',views.update,name="update")
    path('edit/<int:id>',views.edit,name="edit")
]
