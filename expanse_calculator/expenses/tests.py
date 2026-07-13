#imports from django_rest_framework tests
from rest_framework.test import APITestCase

from .models import Expense

class ExpenseModelTestCase(APITestCase):
   
    """
    Test case for the Expense model.
    """
    def setUp(self):
        """
        Set up test data for the Expense model.
        """
        self.expense = Expense.objects.create(
            name='Test Expense',
            amount=100.00,
            category='food'
        )

    def test_expense_creation(self):
        """
        Test that an expense is created successfully.
        """
        self.assertEqual(self.expense.name, 'Test Expense')
        self.assertEqual(self.expense.amount, 100.00)
        self.assertEqual(self.expense.category, 'food')

    def test_expense_str_representation(self):
        """
        Test the string representation of the expense.
        """
        self.assertEqual(str(self.expense), 'Test Expense - 100.0')
    """
    Create 3 expenses with different categories and test the model's functionality.
    """
    def test_multiple_expenses(self):   
        """
        Test creating multiple expenses with different categories.
        """
        expenses = Expense.objects.bulk_create([
            Expense(
                name='Expense 1',
                amount=50.00,
                category='transportation'
            ),
            Expense(
                name='Expense 2',
                amount=75.00,
                category='entertainment'
            ),
            Expense(
                name='Expense 3',
                amount=25.00,
                category='utilities'
            )
        ])
        self.assertEqual(expenses[0].category, 'transportation')
    def test_expensive_update(self):
        """
        Test updating an expense's amount.
        """
        self.expense.amount = 150.00
        self.expense.save()
        updated_expense = Expense.objects.get(id=self.expense.id)
        self.assertEqual(updated_expense.amount, 150.00)

    def test_expense_deletion(self):
        """
        Test deleting an expense.
        """
        self.expense.delete()
        with self.assertRaises(Expense.DoesNotExist):
            Expense.objects.get(id=self.expense.id)
