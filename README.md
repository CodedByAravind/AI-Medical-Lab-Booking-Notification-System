# AI Medical Lab Booking & Notification System

## Overview

This project is a simple AI-driven workflow system designed for medical labs to automate test bookings, data capture, and notifications.

It demonstrates how real-world business processes can be streamlined using automation and intelligent input handling.

### Features

* Chat-based interaction (WhatsApp-style UI)
* Lab test booking system
* Smart input parsing (handles flexible formats)
* Data storage using CSV
* Automated reminders (simulated using background threads)
* Automated report updates (simulated)
* Guided input with examples and validation

## Workflow Architecture

User (Chat Interface) ↓ Flask Backend ↓ Processing Logic (Rule-based AI) ↓ Database (CSV file) ↓ Automated Notifications (Threading) ↓ Response to User

## Tech Stack

* Python
* Flask
* HTML, CSS, JavaScript
* CSV (for data storage)
* Threading (for automation simulation)

## Logic

The system uses a rule-based approach to:

* Understand user intent (booking, queries, reports)
* Extract structured data from natural input
* Handle flexible formats like:
James, Blood Test, 23-12-2026
23-12-2026, urine, James

## Booking Flow

1.User requests booking
2.System prompts for details
3.User enters: Name, Test, Date
4.System:
- Validates input
- Stores data in leads.csv
- Confirms booking

## Automation

### Reminder
Triggered automatically after booking
Simulated using threading (5-second delay)
### Report Update
Automatically triggered after booking
Simulated after 8 seconds

In production, this can be integrated with WhatsApp/SMS APIs (e.g., Twilio)

## How to Run

Install dependencies
```
pip install flask
```
Run the app
```
python app.py
```
Open in browser:
```
http://127.0.0.1:5000
```

## Project Structure

project-folder/ 

│── app.py 

│── index.html 

│── leads.csv 

│── README.md


## Demo

The system demonstrates:

* Real-time chat interaction
* Booking workflow
* Data storage
* Automated reminders & report updates


## Future Improvements
* WhatsApp integration (Twilio API)
* Database (MySQL / MongoDB)
* User authentication
* Admin dashboard for lab management
* Real-time notification system

