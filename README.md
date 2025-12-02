---

# Backend API of Social Media App using FastAPI

This is the backend API of a social media application created using **FastAPI**.
The project includes user authentication, post management, and a voting/like system.

---

## 🚀 Routes Overview

### **1) Post Route**

Responsible for:

* Creating posts
* Deleting posts
* Updating posts
* Retrieving posts

### **2) Users Route**

Handles:

* Creating users
* Fetching users by ID

### **3) Auth Route**

* Login system & token generation

### **4) Vote Route**

* Voting / Like functionality
  *(Currently supports upvote & remove vote — no downvote logic yet)*

---

## 🛠 How to Run Locally

### **Step 1 — Clone the Repository**

```bash
git clone https://github.com/Sanjeev-Thiyagarajan/fastapi-course.git
```

### **Step 2 — Change Directory**

```bash
cd fastapi-course
```

### **Step 3 — Install Dependencies using `uv` (instead of pip)**

```bash
uv venv
source .venv/bin/activate  # for macOS / Linux
# OR
.venv\Scripts\activate     # for Windows

uv pip install fastapi[all]
uv pip install -r requirements.txt
```

### **Step 4 — Run the Application**

```bash
uvicorn main:app --reload
```

### **Step 5 — Open API Documentation**

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 🗄 Database Setup (PostgreSQL)

Create a PostgreSQL database, then add a `.env` file in your project root:

```
DATABASE_HOSTNAME = localhost
DATABASE_PORT = 5432
DATABASE_PASSWORD = <your_password>
DATABASE_NAME = <database_name>
DATABASE_USERNAME = <postgres_user>
SECRET_KEY = <your_generated_secret_key>
ALGORITHM = HS256
ACCESS_TOKEN_EXPIRE_MINUTES = 60
```

> **Note:** The `SECRET_KEY` example is a placeholder. Generate your own key from FastAPI documentation or using:

```bash
openssl rand -hex 32
```

---

## 📚 Learn FastAPI

For complete learning resources, refer to the FastAPI tutorials and official documentation.

---

### 🎉 You're ready to go!

Your FastAPI backend is now live and ready for testing.

---