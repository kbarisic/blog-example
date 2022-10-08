# Blog example powered by FastAPI Python framework

- [Installation](#installation)
- [Getting started](#getting-started)

## Installation

1. Install project dependencies
   ```sh
   pip3 install -r requirements.txt
   ```

## Getting started

1.  Run uvicorn server:
      ```sh
      uvicorn blog.main:app --reload
      ```
2. Go to link in the browser: http://127.0.0.1:8000/docs
3. Use admin credentials to access web api service:
    ```txt
    username: admin@blog.com
    password: admin
    ```