from django.contrib.auth.views import LogoutView
from django.urls import path

from django_salesforce_oauth.views import oauth, oauth_callback

urlpatterns = [
    path("", oauth, {"domain": "login"}, name="oauth"),
    path("sandbox/", oauth, {"domain": "test"}, name="oauth-sandbox"),
    path("callback/", oauth_callback, {"domain": "login"}, name="oauth-callback"),
    path(
        "callback/sandbox/",
        oauth_callback,
        {"domain": "test"},
        name="oauth-callback-sandbox",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
]
