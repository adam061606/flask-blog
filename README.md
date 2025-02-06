# Simple Blog Project

This is a simple blog application built using Python Flask, SQLite as the backend database, and Bootstrap for styling.

## Project Structure

```
simple-blog
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   └── templates
│       ├── base.html
│       ├── index.html
│       ├── login.html
│       └── register.html
├── instance
│   └── config.py
├── venv
├── .flaskenv
├── config.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd simple-blog
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Set up the database URI in `instance/config.py`:
   ```python
   SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
   ```

2. Create the database:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

## Running the Application

To run the application, use the following command:
```
flask run
```

Visit `http://127.0.0.1:5000` in your web browser to access the blog.

## Features

- User registration and authentication
- Create, read, update, and delete blog posts
- Responsive design using Bootstrap

## License

This project is licensed under the MIT License.