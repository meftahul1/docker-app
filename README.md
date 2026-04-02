# My Docker App

A containerized Python web application built with Flask, testing, and continuous integration configured via GitHub Actions.

## What the Project Does
This project is a simple, containerized Python web application that serves a very focused purpose by providing two endpoints: 
- A home route (`/`) that returns a friendly greeting: `"Hello, Docker!"`
- A health check route (`/health`) that returns the operational status of the service: `{"status": "ok"}`

The entire application is packaged using Docker, ensuring that it can run consistently on any machine.

## Prerequisites
- Docker & Docker Compose
- (Optional) Python 3 & pip (if you want to run tests locally without Docker)

## How to Build and Run it Locally with Docker
Because this project includes both a `Dockerfile` and a `compose.yaml` (generated using `docker init`), you have two ways to run it locally. 

### Option 1: Using Docker Compose (Recommended)
This is the easiest way to start the application with a single command. It will build the image and start the container, mapping the container's port to your local machine.

```bash
docker compose up --build
```
The application will be accessible at [http://localhost:5000](http://localhost:5000).

### Option 2: Using standard Docker commands
To manually build the image:
```bash
docker build -t my-docker-app .
```
And to run the container, mapping your machine's port 5000 to the container's port 5000:
```bash
docker run -p 5000:5000 my-docker-app
```

## Running Tests
The project uses `pytest` to test the API routes.
If you have Python and `pytest` installed locally, you can run the test suite using:

```bash
pip install -r requirements.txt
```
upgrade pip by using 
```bash
python -m pip install --upgrade pip
```

```bash

pytest ./test_app.py
```

## GitHub Actions CI/CD Workflow
The project uses GitHub Actions for Continuous Integration. The workflow (defined in `.github/workflows/ci.yml`) is triggered automatically whenever code is pushed to the `main` branch, or when a Pull Request is opened against `main`. 

It performs two main jobs:
1. **Test Job**: It sets up various Python environments, installs the project's dependencies, and runs automated tests using `pytest` to make sure the application endpoints are functioning perfectly. The tests ensure that the root of the application returns a 200 status code and the string "Hello, Docker!", and that the health check endpoint returns a 200 status code and the JSON object `{"status": "ok"}`.

2. **Build Job**: If—and only if the tests pass, the pipeline proceeds to verify that the Docker image can be successfully built (`docker build`). This ensures that the code added never breaks the containerization or the deployability of the application. Just an FYI, the build job does not push the image to any registry, therefore no docker auth credentials were used within the jobs. 


