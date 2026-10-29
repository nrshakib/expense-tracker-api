from django.urls import path

from expenses import views


urlpatterns = [
    path('expenses/', views.ExpenseGetView.as_view(), name = 'get-expenses'),
    path('expenses/<int:id>/', views.ExpenseDetailView.as_view(), name = 'expense-detail'),
    path('expenses/create/', views.ExpenseCreateView.as_view(), name = 'expense-create'),
    path('expenses/edit/<int:id>/', views.ExpenseDetailView.as_view(), name = 'expense-edit'),
    path('expenses/update/<int:id>/', views.ExpenseDetailView.as_view(), name = 'expense-update'),
    path('expenses/delete/<int:id>/', views.ExpenseDetailView.as_view(), name = 'expense-delete'),
]