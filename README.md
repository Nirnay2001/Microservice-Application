# DevOps Practice Microservice

A small web service for practicing the application lifecycle: install dependencies, run tests, build a container image, and run the container. It includes a responsive browser dashboard and two JSON API endpoints.

## Architecture

```text
 Browser
    | GET /
    v
 Flask app --------------------> HTML dashboard (templates/index.html)
    |                                  |
    | GET /health                      | fetch()
    | GET /api/v1/message <------------+
    v
 JSON API responses
```

- **Application:** `app.py` creates the Flask app, serves the dashboard, and defines the JSON API.
- **Frontend:** `templates/index.html` contains the responsive dashboard, styles, and browser-side code. It calls the health and message endpoints using `fetch`.
- **Dependencies:** `requirements.txt` pins Flask.
- **Container image:** `Dockerfile` installs Flask, copies the app and dashboard template, and runs the service on port `5000`.
- **Build context:** `.dockerignore` excludes local caches and virtual environments.
- **Tests:** `tests/test_app.py` checks the dashboard and API routes using Flask's test client.
- **Runtime flow:** the browser loads the dashboard from `/`; its health indicator calls `/health`, and the message button calls `/api/v1/message`. The service is stateless and does not require a database.

## Routes

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/` | Browser dashboard |
| GET | `/health` | Basic health response |
| GET | `/api/v1/message` | Example API message |

## Run locally

Requires Python 3.12 or newer.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

The service listens on `http://localhost:5000`. Set the `PORT` environment variable to use a different port.

Open the dashboard at `http://localhost:5000`. You can also try the JSON API routes in PowerShell:

```powershell
Invoke-RestMethod http://localhost:5000/health
Invoke-RestMethod http://localhost:5000/api/v1/message
```

## Run tests

With the dependencies installed:

```powershell
python -m unittest discover -s tests -v
```

## Build and run with Docker

From the project directory:

```powershell
docker build -t devops-practice-service .
docker run --rm -p 5000:5000 devops-practice-service
```

Then call the routes at `http://localhost:5000`. To map a different host port, for example `8080`, run `docker run --rm -p 8080:5000 devops-practice-service` and use `http://localhost:8080`.
