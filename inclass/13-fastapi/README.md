# Packages: FastAPI

Let's explore a small project together using an installed package. This is ungraded practice with an unfinished starter.

## Package setup

Use the Python 3 installation selected by your instructor. Open a terminal in this topic folder and create a separate virtual environment here.

**Windows PowerShell:**

```powershell
py -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt
```

**macOS/Linux:**

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

These commands use the environment directly; activation is unnecessary. Select this environment's interpreter in your editor too. Where an activity says `python -m pip`, substitute `.venv/Scripts/python.exe -m pip` on Windows or `.venv/bin/python -m pip` on macOS/Linux.

requirements.txt lists direct dependencies without fixing versions. Your instructor may specify versions for class. Record your installed versions in notes.md. Keep requirements.txt in Git; the generated .venv folder is ignored.

## Explore together

1. A route connects a URL path to a function. Import FastAPI and create an application named app in main.py.
2. Define a GET route for /hello. Its function should return a dictionary containing message with the value Hello, workbook!. FastAPI turns the dictionary into a JSON response.
3. Start the server using the command below. Open /hello and /docs in your browser.
4. Change the message and refresh the browser. Try the endpoint in /docs, then stop the server with Ctrl+C.

## Run your work

The starter has no app yet, so the server cannot start until you create it. This is a local development activity.

After creating app, run one of these commands from this folder:

```powershell
# Windows PowerShell
.venv/Scripts/python.exe -m uvicorn main:app --reload --host 127.0.0.1
```

```sh
# macOS/Linux
.venv/bin/python -m uvicorn main:app --reload --host 127.0.0.1
```

Open [local API docs](http://127.0.0.1:8000/docs). Stop the server with Ctrl+C.

## Check your work

- GET /hello returns {"message": "Hello, workbook!"}.
- /docs lists the route and lets you try it.

Keep your edited files and record a prediction, an observed result, installed versions, and a question in notes.md.

## Reference

[FastAPI first steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
