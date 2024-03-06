from django.urls import path
from api.views import PrincipalLimitAPI, PrincipalLimitPage

urlpatterns = [
    path('', PrincipalLimitPage.as_view(), name='reverse-mortgage'),
    path('principal-limit', PrincipalLimitAPI.as_view(), name='reverse-mortgage'),
]


app_name = 'api'