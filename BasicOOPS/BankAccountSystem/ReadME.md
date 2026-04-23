# Bank Account System

A Python-based banking system that models customers, accounts, and transaction tracking using object-oriented design.

## Features

- Support for multiple accounts per customer
- Deposit funds into an account
- Withdraw funds with balance validation
- Transfer funds between accounts
- Track transaction history for each account
- Print account summary with current balance and past transactions

## Project Structure

### Customer
Stores customer details and maintains the list of accounts owned by the customer.

### Account
Handles core banking operations including:

- deposit
- withdraw
- transfer
- account summary

Each account maintains its own balance and transaction history.

### Transaction
Represents transaction records stored in an account’s history.

## Example Workflow

The current implementation demonstrates the following flow:

1. Create a customer
2. Create checking and savings accounts
3. Link both accounts to the customer
4. Deposit money into checking
5. Withdraw money from savings
6. Transfer money from checking to savings
7. Print account summaries

## Technologies Used

- Python

## How to Run

```bash
python filename.py