# Packages: Pandas and Matplotlib (Tiny Introduction)

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

Load data/books.csv with pandas. Calculate total pages and use Matplotlib to create a bar chart comparing the three titles. Use the supplied data unchanged. Add a title and axis labels. Save as books.png before displaying the chart, or inspect the saved image if your environment cannot display a window.

## Run your work

Run from this topic folder so the relative CSV path works. No network request is needed after installing the packages.

Run `.venv/Scripts/python.exe main.py` in Windows PowerShell or `.venv/bin/python main.py` on macOS/Linux.

## Check your work

- The total is 450 pages.
- Three bars show 120, 180, and 150 pages, labelled by title.

Keep your edited files and record a prediction, an observed result, installed versions, and a question in notes.md.

## Reference

[Pandas plotting introduction](https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html)
