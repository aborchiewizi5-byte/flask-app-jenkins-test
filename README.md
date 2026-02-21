# Jenkins Demo App

A simple Flask API used to practise Jenkins CI/CD pipelines.

## Endpoints

| Method | Route        | Description          |
|--------|-------------|----------------------|
| GET    | `/`         | Hello message        |
| GET    | `/health`   | Health check         |
| GET    | `/add/a/b`  | Add two numbers      |

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

## Run Tests

```bash
pytest tests/ -v
```

## Docker

```bash
docker build -t jenkins-demo-app .
docker run -p 5000:5000 jenkins-demo-app
```

## Jenkins Pipeline Stages

1. **Checkout** – pulls the code from SCM
2. **Install Dependencies** – sets up a virtualenv and installs packages
3. **Run Tests** – runs pytest with coverage
4. **Build Docker Image** – builds the container image
5. **Deploy (Local)** – stops any old container and starts the new one
