# 🚀 FastAPI Backend Project

A lightweight and high-performance backend built using **FastAPI**, designed for modern web applications. FastAPI leverages Python type hints and async features to deliver robust APIs with minimal overhead.

## 🧰 Features

- 🔐 JWT-based authentication
- 🧑‍💻 User registration & login system
- 📬 Email/password authentication
- 📄 Pydantic models for validation
- 💾 SQLAlchemy ORM
- 🔄 RESTful routes (CRUD-ready)
- ⚡ Lightning-fast API response times

## 📦 Tech Stack

- **Python 3.10+**
- **FastAPI**
- **Uvicorn** (ASGI server)
- **Pydantic**
- **SQLAlchemy**
- **Passlib + Bcrypt** for password hashing
- **Python-Jose** for JWT handling

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

🧪 Testing
Coming soon: Pytest support for endpoint and model testing!
