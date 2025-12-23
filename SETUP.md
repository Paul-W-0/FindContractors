# FindContractors - Setup Guide

## Prerequisites
- Python 3.12+ installed
- pip installed

## Setup Instructions

### 1. Create and Activate Virtual Environment

**On Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at: http://127.0.0.1:8000/

### 6. Deactivate Virtual Environment

When you're done working:
```bash
deactivate
```

## Development

- The virtual environment is stored in the `venv/` directory (excluded from git)
- All Python dependencies are listed in `requirements.txt`
- Database: SQLite (db.sqlite3)
- Django version: 3.2.9

## Useful Commands

- `python manage.py check` - Check for project issues
- `python manage.py showmigrations` - Show migration status
- `python manage.py test` - Run tests
- `python manage.py shell` - Open Django shell

## Notes

- This project uses Django 3.2.9
- The database is SQLite and is included in the repository for development purposes
- Remember to activate the virtual environment before working on the project
- See README.md for more information about the project
