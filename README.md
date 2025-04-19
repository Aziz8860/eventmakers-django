# EventMakers Django

## Project Description

**EventMakers** is a Django-based web application designed for efficient event management and participant registration. The app provides a modern, responsive interface for creating, editing, and viewing events, as well as registering participants with unique email validation for each event.

### Key Features

- **Event Management**: Create, edit, and view events with details such as name, description, date, category, and image
- **Asynchronous Processing**: Event creation and editing are handled asynchronously using Huey task queue, improving user experience and application scalability
- **Participant Registration**: Users can register for events with their name and email address
- **Email Validation**: The system enforces unique participant emails per event to prevent duplicate registrations, while allowing the same email to register for different events
- **User Authentication**: Complete registration and login system with customizable password validation
- **Enhanced Admin Interface**: Customized Django admin panel for efficient management of events and participants
- **Responsive Design**: Modern UI built with Tailwind CSS for a seamless experience across devices

## Technology Stack

- **Backend**: Django
- **Database**: PostgreSQL
- **Task Queue**: Huey with Redis
- **Frontend**: HTML, Tailwind CSS
- **Authentication**: Django built-in auth system

## Installation and Setup

### Prerequisites

- Python 3.8+
- PostgreSQL
- Redis Server

### Setting Up the Environment

1. Clone the repository and create a virtual environment:

```bash
# Create and activate virtual environment
python -m venv .venv

# On Windows
.\.venv\Scripts\activate

# On Linux/macOS
source .venv/bin/activate
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Set up Redis for Huey task queue
4. Set up PostgreSQL database
5. Run migrations and start the development server
6. Start the Huey worker in a separate terminal

### Project Structure
The application follows Django's MVT (Model-View-Template) architecture with additional components for asynchronous processing:

- models.py: Defines Event and Participant data models
- views.py: Contains class-based views for handling HTTP requests
- methods.py: Contains business logic for event operations
- tasks.py: Defines asynchronous tasks using Huey
- templates/: HTML templates with Tailwind CSS styling
- admin.py: Customized admin interface configuration

### Development Notes
When creating a new Django app:

- Start from view implementation
- Create templates in a templates folder within the app
- Set up URL patterns in urls.py
- Register the app's URLs in core urls.py
- Define models in models.py
- Register models in admin.py

### License
This project is licensed under the MIT License - see the LICENSE file for details.