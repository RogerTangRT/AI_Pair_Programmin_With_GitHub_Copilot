from rest_framework.viewsets import ModelViewSet
from .serializers import ExpenseSerializer
from .models import Expense


class ExpenseViewSet(ModelViewSet):
    """
    A viewset for viewing and editing expense instances.
    """
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
