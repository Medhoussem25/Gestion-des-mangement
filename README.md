# Employee Management System V 1.0

This project is a desktop application for managing employees, developed using Python's Tkinter library for the graphical user interface, SQLite for the database, and PIL for handling images. The application includes functionalities for login, CRUD (Create, Read, Update, Delete) operations, and a dashboard for visualizing employee data.

## Features

### 1. Login System
- Secure login interface.
- Password visibility toggle.
- Displays error messages for incorrect username or password.

### 2. Employee Management
- Add, update, delete, and view employee records.
- Validates input fields for correctness (e.g., email format, age, phone number).
- Prevents duplicate entries based on email.

### 3. Dashboard
- Interactive dashboard for visualizing employee statistics (future enhancement).

### 4. Developer Info
- Displays developer information with contact details.

## Installation

### Prerequisites
- Python 3.x
- Required libraries:
  - Tkinter
  - SQLite3 (built-in with Python)
  - PIL (Pillow)
  - Matplotlib

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/employee-management.git
   ```
2. Navigate to the project directory:
   ```bash
   cd employee-management
   ```
3. Install required dependencies:
   ```bash
   pip install pillow matplotlib
   ```
4. Ensure the following images are in the project directory:
   - `recruitment.png`: Icon for the application.
   - `manager.png`: Display image for the login screen.

5. Run the application:
   ```bash
   python main.py
   ```

## Usage

### Login
1. Launch the application.
2. Enter the username and password. Default credentials:
   - Username: `admin`
   - Password: `123`

### Employee Management
1. After login, the main employee management window opens.
2. Use the form on the left to add employee details:
   - Name
   - Job
   - Gender
   - Age
   - Email
   - Phone number
   - Address
3. Use the buttons below the form for actions:
   - **Add**: Adds a new employee to the database.
   - **Delete**: Removes the selected employee from the database.
   - **Update**: Updates details of the selected employee.
   - **Clear**: Clears the input fields.
   - **Dashboard**: Opens the dashboard (future enhancement).
   - **Logout**: Logs out and returns to the login screen.

### Developer Info
Click the "Infos Développeur" button on the login screen to view developer contact information.

## Database
- The application uses an SQLite database (`employees.db`).
- The `employees` table structure:
  ```sql
  CREATE TABLE employees (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      job TEXT,
      gender TEXT,
      age INTEGER,
      email TEXT UNIQUE,
      phone TEXT,
      address TEXT
  );
  ```

## File Structure
```
employee-management/
├── main.py          # Main application file
├── employees.db     # SQLite database file (auto-created)
├── recruitment.png  # Application icon
├── manager.png      # Login screen image
└── README.md        # Project documentation
```

## Future Enhancements
- Implement an interactive dashboard using Matplotlib for employee data visualization.
- Add role-based authentication.
- Include export and import functionality for employee data.

## Developer Contact
- **Name:** Houssem Bouagal
- **Email:** mouhamedhoussem813@gmail.com
- **Version:** 1.0

