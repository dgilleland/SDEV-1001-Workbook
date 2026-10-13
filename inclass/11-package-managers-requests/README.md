# Package Managers: Fundamentals with Requests

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

1. Follow the package setup. Inspect the installed library using python -m pip show requests, then list the environment's packages with python -m pip list.
2. Import requests. Make a GET request to the supplied URL with timeout=10 so an unresponsive service cannot block forever.
3. Use raise_for_status() to check for an HTTP error. Decode the JSON response and display its url value.
4. Catch requests.exceptions.RequestException and display a short message. Try the supplied error URL as well.
5. Use python -m pip freeze to inspect exact installed versions. Record the requests version in notes.md and explain the roles of pip, the environment, and requirements.txt.

## Run your work

This activity needs internet access. The public practice service may be unavailable; record a connection failure and retry later. A service outage is not necessarily a coding error.

Run `.venv/Scripts/python.exe main.py` in Windows PowerShell or `.venv/bin/python main.py` on macOS/Linux.

## Check your work

- A successful request displays the requested URL.
- The supplied HTTP-error URL produces a useful message rather than an uncaught exception.

Keep your edited files and record a prediction, an observed result, installed versions, and a question in notes.md.

## Reference

[Requests quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/) and [Python package installation](https://packaging.python.org/en/latest/tutorials/installing-packages/)
