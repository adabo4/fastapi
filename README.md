# 🚀 FastAPI Backend Project

This is a learning project where I'm building a backend with **FastAPI** in Python. The idea is to get hands-on with common backend features like:

- Setting up routes
- Creating and verifying JWT tokens for authentication
- Connecting to a PostgreSQL database
- Performing basic CRUD operations

I'm using this project to better understand how a modern backend is structured and how all these pieces work together.

## 🧰 Features

- ✅ User registration and login
- ✅ JWT-based authorization
- ✅ Protected routes
- ✅ PostgreSQL connection with SQLAlchemy
- ✅ Basic CRUD operations (create/read/update/delete)

## 📦 Tech Stack

- **FastAPI** – Python framework for building APIs
- **Uvicorn** – ASGI server to run FastAPI
- **PostgreSQL** – database for storing data
- **SQLAlchemy** – ORM for interacting with the database
- **Pydantic** – for request/response validation
- **python-jose** – for JWT handling
- **passlib** – for password hashing
- **python-dotenv** – for loading environment variables

## 🚀 Getting Started

### 🔧 Installation

1. Clone the repository:

```bash
git clone https://github.com/adabo4/fastapi.git
cd your-fastapi-repo
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
uvicorn app.main:app --reload
```

Visit 👉 http://127.0.0.1:8000/docs for the Swagger API docs.

✅ Environment Setup
Create a .env file with the following:

```bash
SECRET_KEY=your-secret-key
DATABASE_URL=db://user:password@host/dbname
```

## 🧠 What I'm Practicing

- Structuring a backend with routers and models
- Validating input/output using Pydantic
- Securing endpoints with JWT authentication
- Interacting with a PostgreSQL database using SQLAlchemy
- Hashing passwords and managing user auth

🧪 Testing
Coming soon: Pytest support for endpoint and model testing!
