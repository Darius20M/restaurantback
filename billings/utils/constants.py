from model_utils import Choices

PAYMENT_MET = Choices(
    ('credit_card', 'Credit Card'),
    ('bank_transfer', 'Bank Transfer'),
    ('paypal', 'PayPal'),
    ('check', 'Check'),
    ('cash', 'Cash'),
    ('cryptocurrency', 'Cryptocurrency'),
    ('debit_card', 'Debit Card'),
    ('mobile_payment', 'Mobile Payment'),
    ('apple_pay', 'Apple Pay'),
    ('google_pay', 'Google Pay'),
    ('samsung_pay', 'Samsung Pay'),
    ('venmo', 'Venmo'),
)

STATUS_CHOICES = Choices (
    ('pending', 'Pending'),
    ('completed', 'Completed'),
    ('failed', 'Failed'),
)
