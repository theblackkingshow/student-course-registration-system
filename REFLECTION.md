# Reflection

## What was the hardest part of this project?

The hardest part was making the program save and load data correctly. The system works with Python objects, but files store text. I fixed this by converting objects into dictionaries before saving them.

## Which classes did you create and why?

I created a `Person` class to store common personal information like name, email, and phone number.

I created a `Student` class to represent each student. It inherits from `Person` and adds a student ID.

I created a `Course` class to represent each course. It stores the course ID, course name, trainer name, and capacity.

I created a `SchoolSystem` class to manage the main actions of the project, such as adding students, adding courses, registering students, and viewing records.

## How does your registration logic prevent duplicate registrations?

Before registering a student, the system checks the existing registrations. If the same student ID is already registered for the same course ID, the program stops the process and shows a message.

## How does your system check if a course is full?

The system counts how many students are already registered for a course using `count_students_in_course()`. It compares that number with the course capacity. If the number of registered students is equal to or greater than the capacity, registration is not allowed.

## What bugs did you face and how did you fix them?

One issue was having too much code in `main.py`. I fixed it by splitting the project into multiple files inside the `app/` folder.

Another issue was changing the storage files from `.json` files to `.txt` files. I fixed it by updating the file paths in `storage.py`.

I also had duplicate copied files at one point. I removed the unnecessary copies to keep the project clean.

## Which part of the code would you improve if you had more time?

If I had more time, I would improve input validation. For example, I would check email format more carefully and make sure phone numbers contain only valid characters. I would also add tests for the main features.
