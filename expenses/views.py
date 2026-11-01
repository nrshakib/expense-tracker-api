from datetime import datetime
from decimal import Decimal, InvalidOperation

from django.db.models import Avg, Count, Max, Min, Sum
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from expenses.models import Expense
from expenses.serializers import ExpenseSerializer

class ExpenseGetView(APIView):
    def get_filtered_expenses(self, request, expenses):

        # get the query params from the url
        date_params = request.query_params.get('date')
        search_params = request.query_params.get('search')
        min_amount = request.query_params.get('min_amount')

        # if date params exist, filter expenses based on query set, else no filtering
        if date_params:
            try:
                datetime.strptime(date_params, '%Y-%m-%d')
                expenses = expenses.filter(date=date_params)

            except ValueError:
                 raise ValidationError({
                     "date": "Invalid date format. Use YYYY-MM-DD."
                    })

        # if search_params exist, filter the date_filtered_data using search params,
        # if date_params doesn't exist, filter main data using search_params, else no filtering
        if search_params:
            expenses = expenses.filter(purpose__icontains = search_params)

        if min_amount:
            try:
                # if min_amount exists, Convert the query parameter to Decimal.
                min_amount_decimal = Decimal(min_amount)

            # InvalidOperation will be raised if the value is invalid.
            except InvalidOperation:
                raise ValidationError({
                    "message": "Validation failed",
                    "status_text": "Error",
                    "data": {
                        "min_amount": "Invalid amount"
                        }
                    })
        
            # negative value validation
            if min_amount_decimal < 0:
                raise ValidationError({
                    "min_amount": "Amount must be a non-negative number"
                })
            else:
                expenses = expenses.filter(amount__gte = min_amount_decimal)
  
        return expenses

    def get_ordered_expenses(self, request, expenses):
        ordering = request.query_params.get('ordering')
        allowed_fields = ['date', '-date', 'amount', '-amount', 'purpose', '-purpose']

        if ordering:
            if ordering in allowed_fields:
                expenses = expenses.order_by(ordering)
            else:
                raise ValidationError({
                    "ordering": "Invalid ordering value. Use date, -date, amount, -amount, purpose or -purpose."
                })

        return expenses
    
    def get(self, request):
        expenses = Expense.objects.all()

        expenses = self.get_filtered_expenses(request, expenses)
        expenses = self.get_ordered_expenses(request, expenses)

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
                "status_text": "Success",
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
            "status_text": "Success",
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
            "status_text": "Success",
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
            "status_text": "Success",
            "data": serializer.data
        },
        status= status.HTTP_200_OK
    )

    def delete(self, request, id):
        expense = get_object_or_404(Expense, id = id)
        expense.delete()

        return Response({
            "message": "Expense deleted successfully",
            "status_text": "Success",
            "data": None
            },
            status= status.HTTP_200_OK )

class ExpenseStatView(APIView):
    def get(self, request):
        statistics = Expense.objects.aggregate(
            total_expense = Sum('amount'),
            max_expense = Max('amount'),
            min_expense = Min('amount'),
            avg_expense = Avg('amount'),
            expense_count = Count('id')
        )

        return Response({
            'message': 'Statistics retrieved successfully',
            'status_text': 'Success',
            'data': statistics,
        },status= status.HTTP_200_OK
    )

class ExpenseDateReportView(APIView):
    def get(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if not start_date or not end_date:
            raise ValidationError({
                'message': 'Validation failed',
                'success_text': 'Error',
                'data': 'Both start_date and end_date are required.'
            })
        
        try:
            parsed_start_date = datetime.strptime(start_date, '%Y-%m-%d')
            parsed_end_date = datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            raise ValidationError({
                'message': 'Validation failed',
                'data': 'Please provide valid dates.'
            })
        
        if parsed_start_date > parsed_end_date:
            raise ValidationError({
                'message': 'Validation failed',
                'status_text': 'Error',
                'data': {
                    'date': 'Start date cannot be greater than end date.'
                    }
                })

        expenses = Expense.objects.filter(date__range = [start_date, end_date])
        stats = expenses.aggregate(
            total_expense = Sum('amount'),
            max_expense = Max('amount'),
            min_expense = Min('amount'),
            avg_expense = Avg('amount'),
            expense_count = Count('id'),
        )

        return Response({
            'message': 'Filtered data retrieved successfully',
                        'status_text': 'Success',
                        'data': stats
                    }, status = status.HTTP_200_OK
                )