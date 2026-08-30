# Wallet Payment System

A simple Python object-oriented wallet and payment system that models wallet balance management, multiple payment methods, payment processing, and transaction history.

## Overview

This project implements a basic wallet system where a user can store money, attach different payment methods, process payments, and maintain transaction records.

The design separates responsibilities across different classes so that wallet data, payment method rules, and payment processing flow are handled independently.

## Features

- Create a wallet with user details and wallet balance
- Add multiple payment methods to a wallet
- Support different payment method types such as UPI and Card
- Validate payment method availability before processing payment
- Deduct wallet balance safely
- Prevent invalid payments when balance is insufficient
- Maintain wallet transaction history
- List available payment methods
- View recent transaction details

## Main Classes

### Wallet

Represents a user's wallet.

Responsibilities:

- Store wallet owner information
- Store wallet balance
- Store available payment methods
- Store transaction history
- Add payment methods
- Check whether a transaction is possible
- Deduct balance safely
- Record transaction history

### PaymentMethod

Represents the common parent type for all payment methods.

Responsibilities:

- Define common behavior expected from payment methods
- Allow different payment methods to be used through the same interface

### UPIpaymentmethod

Represents a UPI-based payment method.

Responsibilities:

- Store UPI ID
- Store active/inactive status
- Validate whether the UPI method can be used for payment

### Cardpaymentmethod

Represents a card-based payment method.

Responsibilities:

- Store card details such as last four digits
- Store active/inactive status
- Store card limit
- Validate whether the card can be used for a payment amount

### PaymentService

Coordinates the payment flow.

Responsibilities:

- Validate payment amount
- Check whether the selected payment method can be used
- Ask the wallet to deduct balance
- Record successful or failed transactions
- Return payment result

## Object Relationships

### Composition

A wallet has payment methods.

```text
Wallet
  └── payment_methods
        ├── UPIpaymentmethod
        └── Cardpaymentmethod

The wallet owns the list of payment methods. Payment methods do not directly modify the wallet.

Inheritance

UPI and Card payment methods are specific types of payment methods.

PaymentMethod
   ├── UPIpaymentmethod
   └── Cardpaymentmethod

This allows the payment service to work with any payment method that follows the common payment method behavior.

Polymorphism

The payment service can call the same method on different payment method objects.

For example:

payment_method.can_pay(amount)

The actual behavior depends on whether the selected payment method is UPI or Card.

Payment Flow
Successful Payment
User selects a payment method.
PaymentService receives the wallet, payment method, and amount.
PaymentService validates the amount.
PaymentService asks the selected payment method if it can be used.
Wallet checks whether enough balance is available.
Wallet deducts the amount.
Wallet records the transaction.
PaymentService returns success.
Failed Payment

A payment can fail if:

Payment amount is invalid
Payment method is inactive
Card limit is insufficient
Wallet balance is insufficient

In failed cases, the wallet balance remains unchanged.

Design Notes
Wallet owns and protects its own balance.
Payment methods do not directly change wallet balance.
PaymentService coordinates the payment but does not directly modify wallet fields.
Each payment method handles its own validation rules.
Wallet records transaction history through its own method.
New payment methods can be added by creating another class that follows the PaymentMethod behavior.
Example Use Case
1. Create wallet for a user.
2. Add UPI and Card payment methods.
3. Select UPI for a payment.
4. PaymentService validates the method and amount.
5. Wallet deducts the balance.
6. Transaction is recorded.
Concepts Used
Classes and objects
Constructors
Instance variables
Encapsulation
Inheritance
Polymorphism
Composition
Method responsibilities
Basic validation
Transaction history management