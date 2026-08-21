# CareSlot - Service Booking & Appointment Management System

CareSlot is a Django-based web application designed to prevent double-booking conflicts for service businesses (e.g., salons, clinics, repair centers).

## Features
- Browse services and rates
- Real-time time slot booking with double-booking prevention logic
- User booking status tracking (Pending, Confirmed, Cancelled)
- Admin management for services and appointments

## Design Methodology
This project uses **Specification-Driven Design**. All structural decisions, database entities, and workflows were documented in `SPEC.md` prior to execution.

## How to Run Locally

### Option 1: Standard Python Setup
1. Clone the repository:
   ```bash
   git clone <GITHUB_REPO_URL>
   cd Project01

## Future Improvements (Reflection)
Given more time, the following enhancements would be made:
- **User Authentication & Roles:** Implement distinct role-based access control and customized dashboards for Customers and Admins.
- **Automated Email/SMS Notifications:** Integration to send real-time appointment confirmations and reminder alerts.
- **RESTful API Services:** Expose endpoints using Django REST Framework (DRF) to enable mobile app integrations.
- **Online Payment Gateway:** Integrate payment gateways to process upfront booking deposits.