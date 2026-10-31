from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'date', 'purpose', 'amount']

    def validate_purpose(self, value):
        if value and len(value) < 3:
            raise serializers.ValidationError("Purpose must contain at least 3 characters.")
                    
        return value