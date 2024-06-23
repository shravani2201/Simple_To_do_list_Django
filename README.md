# TO-DO List Webapp

A simple web application to manage your tasks. This project includes user authentication, task creation, completion, and deletion functionalities. It is built using Django.

## Features

- User Registration
- User Login
- Task Creation
- Task Completion
- Task Deletion
- Different views and functionalities for Admin and Guest users

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.11.5
- Django 4.2.6
- Virtualenv (optional but recommended)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/todo-list-webapp.git
    cd todo-list-webapp
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages.**

4. **Install and set-up the OPA executable file from the github releases from the official website.**


5. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

8. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:8000/
    ```

## Project Structure

- `homepage/`: Contains the main application files.
  - `templates/homepage/`: HTML templates for the application.
  - `static/homepage/`: Static files (CSS, JS, images).
- `todo_list/`: Main project folder with settings and configuration.
- `manage.py`: Command-line utility for administrative tasks.

## Usage

1. **Homepage:**
   - Welcome message and links to Login and Register.

2. **Register:**
   - Create a new user account with a role selection (Guest/Admin).

3. **Login:**
   - Authenticate with username and password.

4. **To-Do List:**
   - View, create, complete, and delete tasks.

## Demo Video

https://github.com/shravani2201/Simple_To_do_list_Django/assets/119721385/a838260e-adba-4acb-8509-c53d63cf0c2b


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please reach out to [tvshravani22@gmail.com](mailto:tvshravani22@gmail.com).
