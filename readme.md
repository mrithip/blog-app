# Django Blog Project

A simple blog application built with Django. This project features blog post management, categories, an about page, and a contact form. It uses SQLite as the database and Bootstrap for styling.

## Features

- List and paginate blog posts
- View post details with related posts
- Categorize posts
- About page
- Contact form (logs submissions)
- Admin interface for managing posts, categories, and about info

## Project Structure

```
myapp/
    settings.py
    urls.py
    ...
blog/
    models.py
    views.py
    urls.py
    forms.py
    admin.py
    templates/
    static/
    management/
        commands/
db.sqlite3
manage.py
```

## Setup Instructions

1. **Clone the repository**

    ```sh
    git clone <your-repo-url>
    cd <project-directory>
    ```

2. **Create and activate a virtual environment**

    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install dependencies**

    ```sh
    pip install django
    ```

4. **Apply migrations**

    ```sh
    python manage.py migrate
    ```

5. **Populate initial data (optional)**

    ```sh
    python manage.py populate_category
    python manage.py populate_posts
    ```

6. **Create a superuser for admin access**

    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server**

    ```sh
    python manage.py runserver
    ```

8. **Access the app**

    - Blog: [http://localhost:8000/](http://localhost:8000/)
    - Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Custom Commands

- `populate_category`: Populates the database with sample categories.
- `populate_posts`: Populates the database with sample blog posts.

## License

This project is licensed under the MIT License.

---

**Made with Django**