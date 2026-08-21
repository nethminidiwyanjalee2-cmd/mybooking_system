# SPEC.md - CareSlot: Service Booking & Appointment Management System

## 1. Project Overview & Problem Statement
Small service-based businesses (e.g., hair salons, auto repair shops, private clinics) often face scheduling conflicts and double-booking issues when managing appointments manually. CareSlot is a full-stack web application designed to automate slot availability checks, streamline customer reservations, and provide administrators with a centralized dashboard to manage daily bookings.

## 2. Target Users & Personas
- **Customer:** Browses available services, checks real-time slot availability, books appointments, and views booking history.
- **Admin / Staff:** Manages available services (CRUD), reviews pending booking requests, updates booking statuses, and monitors daily schedules.

## 3. Functional Requirements

### Customer Features
- **Service Catalog:** View all listed services with details (title, description, price, duration).
- **Appointment Booking:** Select a service, date, and available time slot to submit a booking request.
- **Double Booking Prevention (Business Logic):** System checks existing database records to ensure the selected time slot and service are not already booked for the specified date.
- **My Bookings:** View a personal history of booked appointments along with their status (Pending, Confirmed, Cancelled).

### Admin Features
- **Service Management:** Add, edit, or delete services offered by the business.
- **Booking Management:** Review incoming booking requests and update status (Approve/Cancel).
- **Dashboard Overview:** View a structured list of daily appointments filtered by date or status.

## 4. System Architecture & Tech Stack
- **Framework:** Django (Python 3.x)
- **Database:** SQLite (Development) / PostgreSQL (Production ready)
- **Frontend:** Semantic HTML5, Custom CSS3 / Bootstrap
- **Containerization:** Docker & Docker Compose
- **Version Control:** Git & GitHub

## 5. Data Model (Database Schema)

### User Entity (Django Built-in User Model)
- `id`: Integer (PK)
- `username`: String
- `email`: String
- `first_name`: String
- `last_name`: String
- `is_staff`: Boolean

### Service Entity
- `id`: Integer (PK)
- `title`: String (e.g., "Haircut & Styling")
- `description`: Text
- `price`: Decimal
- `duration_minutes`: Integer (e.g., 30, 60)
- `created_at`: DateTime

### Booking Entity
- `id`: Integer (PK)
- `user`: ForeignKey (User)
- `service`: ForeignKey (Service)
- `booking_date`: Date
- `booking_time`: Time
- `status`: String (Choices: 'Pending', 'Confirmed', 'Cancelled')
- `created_at`: DateTime

## 6. Key User Flows

### Flow 1: Customer Booking Request
1. Customer selects a service from the Service Catalog.
2. Customer chooses a preferred date and time slot.
3. System validates slot availability (`booking_date` + `booking_time` + `service`).
4. If available, the system saves the record with status `Pending` and shows a success notification.
5. If unavailable, an error message is displayed requesting the user to pick a different slot.

### Flow 2: Admin Approval Workflow
1. Admin logs into the dashboard and reviews `Pending` requests.
2. Admin updates the status to `Confirmed` or `Cancelled`.
3. Database record updates and reflects on the customer's "My Bookings" page.

## 7. Development & Deployment Strategy
- **Version Control:** Incremental commits pushed to GitHub following feature branch strategy.
- **Containerization:** Environment containerized using Dockerfile to ensure reproducible execution across operating systems.