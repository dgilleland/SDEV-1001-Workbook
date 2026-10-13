# Packages: FastAPI

Try this independent activity after the matching in-class introduction. This is ungraded practice with an unfinished starter.

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

## Your task

Create a local greeting API with a GET route at /greet/{name}. Use a path parameter and a function argument annotated as str. Return a dictionary with a message containing the name. Try the endpoint in /docs. Keep this in memory; databases, authentication, and deployment are outside this introduction. Stop the server when finished.

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

- GET /greet/Ada returns {"message": "Hello, Ada!"}.
- Changing the path name changes the returned greeting.

Keep your edited files and record a prediction, an observed result, installed versions, and a question in notes.md.

## Reference

[FastAPI first steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
