#from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Stock
from .serializers import StockSerializer
from rest_framework import status
# Create your views here.


class StockList(APIView):


     def get(self, resquest):
         stocks = Stock.objects.all()
         serializer = StockSerializer(stocks,  many=True)
         return Response(serializer.data)
         


#   def post(self) :
#          pass   
