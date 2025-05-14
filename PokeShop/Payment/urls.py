from django.urls import path
from Payment.views import createPayment, getPaymentsByUser, updatePaymentStatus, deletePayment

urlpatterns = [
    path('payment/create/', createPayment, name="create-payment"),
    path('payment/<int:user_id>/', getPaymentsByUser, name="get-payments-by-user"),
    path('payment/update/<int:payment_id>/user/<int:user_id>/', updatePaymentStatus, name="update-payment-status"),
    path('payment/delete/<int:payment_id>/', deletePayment, name="delete-payment"),
]
