from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from expenses.models import Expense
from expenses.serializers import ExpenseSerializer

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

class ExpenseDetailView(APIView):
    def get(self, request, id):
        expense = get_object_or_404(Expense, id = id)
        serializer = ExpenseSerializer(expense)

        return Response({
            "message": 'Expense retrieved successfully',
            "data": serializer.data
        },
        status= status.HTTP_200_OK
    )

    def patch(self, request, id):
        expense = get_object_or_404(Expense, id = id)
        serializer = ExpenseSerializer(expense, data = request.data, partial = True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message": "Expense updated successfully",
            "data": serializer.data
        },
        status=status.HTTP_200_OK
    )

    def put(self, request, id):
        expense = get_object_or_404(Expense, id = id)
        serializer = ExpenseSerializer(expense, data = request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message": "Expense updated successfully",
            "data": serializer.data
        },
        status= status.HTTP_200_OK
    )

    def delete(self, request, id):
        expense = get_object_or_404(Expense, id = id)
        expense.delete()

        return Response({
            "message": "Expense deleted successfully"},
            status= status.HTTP_200_OK )