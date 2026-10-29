# Student Management System

A Python and MySQL-based application for managing student records, teacher information, attendance, examination marks, and student results.

## Project Overview

The Student Management System is designed to simplify common academic record-management tasks through a menu-driven Python application backed by a MySQL relational database.

The project demonstrates Python programming, SQL operations, database connectivity, modular code organization, input validation, logging, and automated testing.

## Features

### 1. Student Management

* Add student records.
* Display student records.
* Search for students by roll number.
* Update student information.
* Delete student records.

### 2. Teacher Management

* Manage teacher information.
* Store teacher names, subjects, and email addresses.

### 3. Attendance Management

* Record student attendance.
* View attendance history.
* Generate attendance summaries.

### 4. Marks Management

* Add examination marks.
* View marks by student.
* Update marks.
* Delete marks.

### 5. Student Results

* Calculate total marks.
* Calculate percentages.
* Assign grades.
* Determine pass or fail status according to the configured rules.

### 6. Application Reliability

* Validate user inputs.
* Handle database errors.
* Log important application events.
* Use automated tests for selected functions.

## Technologies Used

* **Python** — application logic
* **MySQL** — relational database
* **mysql-connector-python** — Python–MySQL connectivity
* **python-dotenv** — environment-variable configuration
* **unittest** — automated testing
* **Git and GitHub** — version control and project hosting

## Project Structure

```text
student_management_system/
├── main.py
├── database.py
├── logger_config.py
├── .env.example
├── .gitignore
├── models/
├── repositories/
├── services/
├── utils/
└── tests/
```

### Directory Responsibilities

* `models/` — represents application entities such as students, teachers, marks, and attendance.
* `repositories/` — organizes database operations.
* `services/` — contains application-level business logic.
* `utils/` — contains reusable validation and calculation functions.
* `tests/` — contains automated tests.

## Database

The application uses a MySQL database named `student_management`.

The database contains tables for:

* `students`
* `teachers`
* `attendance`
* `marks`

Foreign keys connect attendance and marks records to students. These relationships help maintain referential integrity.

## Prerequisites

Install the following before running the project:

* Python 3
* MySQL Server
* MySQL Workbench (optional)
* Git (optional)

## Installation

### 1. Clone the repository

After publishing the project on GitHub:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace the placeholder with your repository's actual URL.

### 2. Open the project directory

```bash
cd student_management_system
```

### 3. Create a virtual environment

On Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
python -m pip install mysql-connector-python python-dotenv
```

### 5. Configure environment variables

Create a local `.env` file using `.env.example` as a template.

Configure the following variables:

```env
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=student_management
```

Use your own MySQL credentials. Do not commit `.env` to GitHub.

### 6. Set up the database

Create the database in MySQL:

```sql
CREATE DATABASE student_management;
```

Create the tables using the schema required by your application.

**Note:** The SQL table definitions should be documented or provided separately if they are not created automatically by the application.

### 7. Run the application

```powershell
python main.py
```

## Running Tests

Run the complete automated test suite:

```powershell
python -m unittest discover -s tests -v
```

## Security Notes

* Keep database credentials in `.env`.
* Exclude `.env` from version control.
* Use parameterized SQL queries.
* Avoid logging passwords or sensitive student information.
* Use appropriate database permissions when deploying beyond a local development environment.

## Future Improvements

Potential enhancements include:

* A graphical user interface or web interface.
* Exporting reports to CSV or PDF.
* Improved attendance analytics.
* More comprehensive automated tests.
* Database migration and setup scripts.
* Role-based access control.
* Deployment and continuous integration.

## Learning Outcomes

This project provides practical experience with:

* Python functions, classes, and modules.
* Object-oriented programming.
* SQL CRUD operations.
* Relational database design.
* Error handling and logging.
* Automated testing.
* Environment-variable configuration.
* Version control workflows.

## Project Status

The core Student Management System features have been implemented and tested.

### Current Features
- Student record management
- Teacher record management
- Attendance management
- Marks management
- Result calculation
- MySQL database integration
- Input validation
- Logging
- Automated unit tests

### Technologies Used
- Python
- MySQL
- Git
- GitHub
- python-dotenv
- unittest

## Future Improvements
- Role-based login for teachers and administrators
- Student performance reports
- Attendance reports
- Improved user interface


## Author

**Your Name**

MSc Data Science Student

