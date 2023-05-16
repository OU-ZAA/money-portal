import json
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Transaction, User

# Create your views here.
def index(request):
    return render(request, "finance/index.html")


@csrf_exempt
@login_required
def transactions(request):
    if request.method == "POST":
        
        # Get the data
        data = json.loads(request.body)
        amount = data.get("amount")
        transactionType = data.get("transaction_type")
        memo = data.get("memo")

        # Create a new transaction and save it to db
        transaction = Transaction(
            amount=amount,
            transaction_type=transactionType,
            memo=memo,
            user=request.user
        )
        transaction.save()

        # Update the balance
        if transactionType == "deposit":
            user = User.objects.get(username=request.user.username)
            user.balance += float(amount)
            user.save()

        elif transactionType == "point of sale":
            user = User.objects.get(username=request.user.username)
            user.balance -= float(amount)
            user.save()

        return JsonResponse({"message": "New transaction created succeful"}, status=201)
    
    transactions = Transaction.objects.filter(user=request.user).order_by("-created_at")

    return JsonResponse([transaction.serialize() for transaction in transactions], safe=False)


def users(request):
    return JsonResponse(request.user.serialize(), safe=False)


def thismonth_transactions(request):
    # Get this month transactions
    thismonth = str(timezone.now().month)
    transactions = Transaction.objects.filter(user=request.user, created_at__month=thismonth)

    return JsonResponse([transaction.serialize() for transaction in transactions], safe=False)


def login_view(request):
    if request.method == "POST":

        # Attempting to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "finance/login.html", {
                "message": "Invalide username or password"
            })

    return render(request, "finance/login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirm_password = request.POST["confirm-password"]
        if password != confirm_password:
            return render(request, "finance/register.html", {
                "message": "Passwords must match"
            })
        
        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
        except IntegrityError:
            return render(request, "finance.html", {
                "message": "Username already taken"
            })
        
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    return render(request, 'finance/register.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))