# FlightBooking
Akashayanam is a Python-based flight booking system designed for domestic air travel in India. The application allows users to register and log in, search for flights, select travel options, calculate ticket prices, apply discounts, and complete a booking. The current version uses Indian domestic destinations, Indian Rupees (INR), and India-based payment options as sample data.

# Features
# User Registration & Login
-Checks whether a user already has a registered account.
-Allows new users to create an account.
-Generates an OTP using Python's random module.
-Sends an OTP to the user's email address for verification.
-Flight Booking

Users can select from three travel options:
-One-way
-Two-way
-Multicity

For each journey, users can enter:
-Departure location
-Destination
-Travel date
-Preferred time slot
For multicity travel, the user can specify the number of destinations, and the system collects the required journey details using a loop.

# Airline Selection & Pricing
Users can select their preferred airline before proceeding to billing.
The system calculates ticket prices according to the traveller's age and group size:
-Travellers under 2 years old receive half-price tickets.
-Travellers over 60 years old receive half-price tickets.
-Groups of 5 or more travellers receive a 10% discount.

# Payment
The system provides several payment options:
-UPI
-Credit Card
-Debit Card
-Net Banking
It also includes digital payment options:
-Paytm
-PhonePe
-Google Pay
-BharatPe
-Amazon Pay
PIN verification is required for phone-based payment options within the application.

# Booking Confirmation
After successful payment, the system sends a confirmation email containing the booking information and ticket details.
