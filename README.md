# Student Course Registration System

## What the Project Does

This is a terminal-based Python application for managing student course registration. It allows a user to add students, add courses, register students for courses, view saved records, and search student information.

The project stores data in text files inside the `data/` folder. The data is written in JSON format so it can be loaded again when the program starts.

## How to Run the Project

1. Make sure Python 3 is installed.
2. Open the project folder in the terminal.
3. Run the command:

```bash
python3 main.py
```

4. Choose an option from the menu by entering its number.

## Features Implemented

- Add a new student
- View all students
- Search for a student by ID or name
- Add a new course
- View all courses
- Register a student for a course
- View students registered in a course
- View courses registered by a student
- Save data to `.txt` files
- Load data from `.txt` files
- Prevent duplicate student IDs
- Prevent duplicate course IDs
- Prevent duplicate course registrations
- Prevent registration when a course is full

## Classes Used

- `Person`: A base class that stores shared personal details such as name, email, and phone number.
- `Student`: A child class of `Person` that adds a student ID and methods for saving, loading, and displaying student information.
- `Course`: A class that stores course details such as course ID, course name, trainer name, and capacity.
- `SchoolSystem`: The main system class that manages students, courses, registrations, and user actions.

## Project Structure

```text
main.py
app/
  __init__.py
  menu.py
  models.py
  school_system.py
  storage.py
data/
  students.txt
  courses.txt
  registrations.txt
screenshots/
```

## Challenges Faced

One challenge was organizing the project so that everything was not inside `main.py`. This was fixed by separating the code into different modules for models, storage, menu logic, and system logic.

Another challenge was saving Python objects to a file. This was solved by converting `Student` and `Course` objects into dictionaries before saving them, then converting the dictionaries back into objects when loading data.

## Screenshots

The `screenshots/` folder contains terminal screenshots showing the application running.

- `01_add_student.png`
- `02_add_course.png`

#