from decimal import Decimal, InvalidOperation

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from expenses.models import Expense
from expenses.serializers import ExpenseSerializer

class ExpenseGetView(APIView):
    def get(self, request):
        expenses = Expense.objects.all()

        # get the search query params from the url
        date_params = request.query_params.get('date')
        search_params = request.query_params.get('search')
        min_amount = request.query_params.get('min_amount')

        # if date params exist, filter expenses based on query set, else no filtering
        if date_params:
            expenses = expenses.filter(date=date_params)

        # if search_params exist, filter the date filtered data using search params,
        # if date_params doesn't exist, filter main data using search_params, else no filtering
        if search_params:
            expenses = expenses.filter(purpose__icontains = search_params)

        
        if min_amount:
            try:
                # if min_amount exists, Convert the query parameter to Decimal.
                # InvalidOperation will be raised if the value is invalid.
                min_amount_decimal = Decimal(min_amount)

                # negative value validation
                if min_amount_decimal >= 0:
                    expenses = expenses.filter(amount__gte = min_amount_decimal)
                else:
                    return Response({
                                "message": "Amount must be a non-negative number",
                                "status_text": "error",
                                "data": None
                            },
                                status=status.HTTP_400_BAD_REQUEST
                        ) 

            except InvalidOperation:
                return Response({
                    "message": "Invalid amount",
                    "status_text": "error",
                    "data": None
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ExpenseSerializer(expenses, many= True)
    
        return Response(
            {
                "message": 'Data Retrieved Successfully',
                "status_text": "Success",
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