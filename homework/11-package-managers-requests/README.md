# Package Managers: Fundamentals with Requests

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

Use the supplied echo service to send a query parameter named topic with the value python. Use the params argument rather than assembling the query string yourself. Display the echoed topic from the response's args dictionary. Set a timeout, check HTTP status, and handle request failures. Record the installed requests version in notes.md.

## Run your work

This activity needs internet access. The public practice service may be unavailable; record a connection failure and retry later. A service outage is not necessarily a coding error.

Run `.venv/Scripts/python.exe main.py` in Windows PowerShell or `.venv/bin/python main.py` on macOS/Linux.

## Check your work

- The response echoes python as the topic.
- The HTTP-error URL produces a useful message.

Keep your edited files and record a prediction, an observed result, installed versions, and a question in notes.md.

## Reference

[Requests quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/) and [Python package installation](https://packaging.python.org/en/latest/tutorials/installing-packages/)
