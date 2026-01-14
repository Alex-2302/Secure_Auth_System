# Setup & Execution Guide  
Secure Authentication System

---

## Purpose of This Document

This document describes the **safe and reproducible setup process** used to run the application for **security testing and analysis**.

The focus is on:
- Environment isolation
- Controlled dependency installation
- Local-only execution

This project is **not intended for production deployment**.

---

## 1. Environment Isolation (Virtual Environment)

A Python virtual environment is used to:

- Isolate project dependencies
- Prevent system-wide package pollution
- Ensure reproducible security testing results

### Create the virtual environment

python3 -m venv venv

Activate the virtual environment

source venv/bin/activate

###2. Dependency Installation

All required dependencies are explicitly defined in requirements.txt.

Only these dependencies should be installed to reduce:

- Supply-chain risk
- Dependency confusion
- Uncontrolled package usage
- pip install -r requirements.txt

###3. Application Execution

Run the application locally using Python:

python3 app.py


On successful startup, Flask displays:

Running on http://127.0.0.1:5000


This indicates the application is running correctly in a local environment.

###4. Application Access

The application is accessible only on localhost at:

http://127.0.0.1:5000/


No external network exposure is required or recommended.
