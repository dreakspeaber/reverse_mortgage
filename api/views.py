from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from api.serializers import ReverseMortgageSerializer
from mortgage import ReverseMortgageManager

# Create your views here.



class MarginAPI(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'margins': ReverseMortgageManager.MARGIN_LIST},status=status.HTTP_200_OK)


class PrincipalLimitPage(TemplateView):
    template_name = 'principal_limit_index.html' 


class PrincipalLimitAPI(APIView):
    def post(self, request):
        serializer = ReverseMortgageSerializer(data=request.data)
        print(request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        reverse_mortgage_manager = ReverseMortgageManager(**serializer.validated_data)
        if not reverse_mortgage_manager.is_valid():
            return Response(reverse_mortgage_manager.errors(), status = status.HTTP_400_BAD_REQUEST)
        return Response(reverse_mortgage_manager.get_principal_limit(), status = status.HTTP_200_OK)
    

