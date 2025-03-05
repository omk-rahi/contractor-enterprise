# Contractor Enterprise IT Solutions

Contractor Enterprise IT Solutions is a web-based platform designed to make the company's services and products easily accessible online.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/downloads/) (version 3.8 or higher)
- [Node.js](https://nodejs.org/en/download/) (version 14 or higher - Optional)
- [pnpm](https://pnpm.io/) (for managing frontend dependencies - Optional)

## Setup Instructions

### 1. Clone the repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/omk-rahi/contractor-enterprise.git
cd contractor-enterprise
```

### 2. Setup the Backend (Django)

#### 2.1 Create and Activate a Virtual Environment

It's recommended to use a virtual environment to manage dependencies for the backend. To create and activate a virtual environment, run the following commands:

```bash
    python -m venv venv
    source venv/Scripts/activate
```

#### 2.2 Install Backend Dependencies

Once the virtual environment is activated, install the Python dependencies for the Django project using the requirements.txt file:

```bash
    pip install -r requirements.txt
```

#### 2.3 Apply Migrations

Once the virtual environment is activated, install the Python dependencies for the Django project using the requirements.txt file:

```bash
    python manage.py migrate
```

#### 2.4 Run the Django Development Server

Once the virtual environment is activated, install the Python dependencies for the Django project using the requirements.txt file:

```bash
    python manage.py runserver
```
