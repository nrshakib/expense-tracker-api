from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from expenses.models import Expense
from expenses.serializers import ExpenseSerializer

# Create your views here.
class ExpenseGetView(APIView):
    def get(self, request):
        data = Expense.objects.all()
        serializer = ExpenseSerializer(data, many= True)
    
        return Response(
            {
                "message": 'Data Retrieved Successfully',
                "data": serializer.data,
            },
            status = status.HTTP_200_OK
        )
class ExpenseCreateView(APIView):
    def post(self, request):
        data = request.data
        serializer = ExpenseSerializer(data = data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Expense created Successfully",
                "data": serializer.data
            },
                status=status.HTTP_201_CREATED,
            )
