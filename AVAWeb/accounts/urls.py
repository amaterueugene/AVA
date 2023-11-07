from django.urls import path

from .views import AllAccountsView

urlpatterns = [
    path('', AllAccountsView.as_view(), name="all_accounts"),
]
