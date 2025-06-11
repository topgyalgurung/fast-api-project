
# FastAPI Project

A lightweight and powerful web API built using [FastAPI](https://fastapi.tiangolo.com/tutorial/), a modern Python framework designed for speed, type safety, and simplicity.

## 🚀 Getting Started

Follow these steps to set up your FastAPI environment locally:

```bash
$ cd fastapi-project
$ python3 -m venv venv
$ source venv/bin/activate 
$ pip install "fastapi[standard]"
```
Run the Dev Server
```bash
fastapi dev main.py
```
Once the server is running, you can access:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc UI: http://127.0.0.1:8000/redoc

Benefits of Fast API:
- 🐍 It’s just plain Python
- ⚡ Built-in async support for high-performance APIs
✅ Built-in data validation with Pydantic
- 🧠 FastAPI is typed Python – helps catch bugs early and improves editor support
- 🧾 JSON-based error responses (vs HTML in Flask)
- 🔐 Authentication built in:
- HTTP Basic
- OAuth2 (JWT tokens)
- API Key support via headers
- 📊 Swagger UI and ReDoc built in:
- Great for frontend developers, stakeholder demos, and API documentation


For more details and learning resources, check out the official [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)