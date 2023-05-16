from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register_view, name="register"),
    path("logout", views.logout_view, name="logout"),

    # API routes
    path("transactions", views.transactions, name="transactions"),
    path("users", views.users, name="users"),
    path("transactions/thismonth", views.thismonth_transactions, name="thismonth-transactions")
]