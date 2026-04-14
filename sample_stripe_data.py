import stripe
import time
import random
from credentials import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY

run_id = int(time.time())  # unique per run



# Create customers + payments
for i in range(10):
    customer = stripe.Customer.create(
        email=f"user{i}@test.com",
        metadata={"run_id": run_id}
    )
    print(f'Created customer {customer.id}')

    payment_method = random.choices(
    ["pm_card_visa", "pm_card_chargeDeclined"],
    weights=[0.7, 0.3]  # 70% success, 30% failure
    )[0]

    try:
        stripe.PaymentIntent.create(
            amount=random.randint(500, 10000),
            currency="usd",
            customer=customer.id,
            payment_method=payment_method,
            #payment_method_types=["card"],
            confirm=True, # this creates a charge immediately
            automatic_payment_methods={
                "enabled": True,
                "allow_redirects": "never"
            },
            metadata={"run_id": run_id}
        )
        print(f'Created payment intent for customer {customer.id}')
    
    except stripe.error.CardError as e:
        print(f"FAILED: {customer.id} - {e.user_message}")

