# ProjectNest

ProjectNest is an intuitive project management tool designed to streamline your workflow and enhance collaboration. Built with Django for the backend and Tailwind CSS for the frontend, ProjectNest aims to provide a user-friendly and efficient platform for managing projects and tasks.

## Features

- **User Authentication:** Secure sign-up, log-in, and log-out functionality.
- **Project Management:** Create, edit, and delete projects with ease.
- **Task Management:** Add, update, and remove tasks within projects.
- **Responsive Design:** Optimized for both mobile and desktop views.
- **Custom User Model:** Utilizing Django’s AbstractBaseUser and PermissionsMixin for flexible user management.

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x or higher
- Tailwind CSS

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/projectnest.git
    ```
2. Navigate to the project directory:
    ```sh
    cd projectnest
    ```
3. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```
4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
5. Apply migrations:
    ```sh
    python manage.py migrate
    ```
6. Run the development server:
    ```sh
    python manage.py runserver
    ```

### Usage

- Access the application at `http://127.0.0.1:8000/`
- Sign up for a new account or log in with existing credentials.
- Create, edit, and manage your projects and tasks.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Django: [https://www.djangoproject.com/](https://www.djangoproject.com/)
- Tailwind CSS: [https://tailwindcss.com/](https://tailwindcss.com/)

---

Developed by Tileni

Feel free to reach out with any questions or feedback. Enjoy managing your projects with ProjectNest!
