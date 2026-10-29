from django.urls import path

from expenses import views


urlpatterns = [
    path('expenses/', views.ExpenseGetView.as_view(), name = 'get-expenses'),
    path('expenses/create/', views.ExpenseCreateView.as_view(), name = 'expense-create')
]