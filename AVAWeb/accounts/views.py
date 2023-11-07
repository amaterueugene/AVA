from django.shortcuts import render
from django.views.generic import ListView

from .views import *
from .models import Account


class AllAccountsView(ListView):
    model = Account
    context_object_name = 'accounts'
    template_name = 'accounts/accounts.html'
    # сделать fetch для конкретного юзера через context_data