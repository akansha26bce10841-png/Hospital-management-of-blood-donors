HOSPITAL BLOOD DONOR MANAGEMENT SYSTEM


1. Overview

The Hospital Blood Donor Management System is a menu-driven Python application designed to organize and manage blood donor information. It provides a simple way to add, view, search, update, and delete donor records, along with generating a blood-group-wise donor report.

2. Objectives

The project aims to apply core Python concepts to a practical healthcare-related problem, including lists, strings, functions, loops, conditional statements, user input/output, and list methods.

3. Problem Statement

Hospitals may need to quickly identify suitable blood donors. This project provides a simple system for storing donor details and searching for donors based on their blood group.

4. Features and Scope

- Add new donor records
- View all registered donors
- Search donors by blood group
- Update donor details
- Delete donor records
- Generate blood-group-wise reports

The current version is a console-based application using temporary list storage.

5. System Design

5.1 Architecture

The project follows a function-based architecture. The main menu controls different operations:

"Main Menu → Add → View → Search → Update → Delete → Report"

5.2 Algorithms and Logic

The program stores donor records inside a list. Each operation is implemented through a separate function. Conditional statements identify the selected menu option, while loops process donor records for searching, updating, deleting, and generating reports.

6. Implementation Details

Programming Language: Python 3
Interface: Command Line
Data Structure: List
External Libraries: None

7. How to Run

Save the program as:

blood_donor_management.py

Run the following command:

python blood_donor_management.py

8. Testing and Validation

The system was tested for donor registration, viewing, searching, updating, deletion, and blood-group reporting. Each operation produced the expected output for valid inputs.

9. Results and Observations

The application successfully manages donor records through a simple menu-driven interface. It provides quick blood-group-based searching and maintains accurate donor information during program execution.

10. Conclusion and Future Work

The project demonstrates the practical application of fundamental Python programming concepts to a real-world record-management problem. Future improvements can include MySQL database connectivity, Tkinter GUI, authentication, donor eligibility checking, and blood inventory management.

11. References

- Python Official Documentation
- Python Course Materials
- VITyarthi Build Your Own Project Guidelines

12. Academic Integrity

This project is developed as an academic Build Your Own Project submission for the Python course and follows the applicable academic guidelines.