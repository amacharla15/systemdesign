Notification System

A simple Python notification system that supports Email, SMS, and Push notification channels using a shared send interface.

Features:
- Email notification support
- SMS notification support
- Push notification support
- NotificationService class that can send messages through any notification object
- Avoids hardcoded if/else chains by using polymorphic behavior

Core Design:
Each notification type implements a send(message) method. NotificationService stores a notification object and calls its send method without checking whether it is email, SMS, or push.

Files:
- main.py: contains notification classes and demo usage

How to Run:
python main.py