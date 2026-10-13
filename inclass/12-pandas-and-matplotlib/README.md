# Packages: Pandas and Matplotlib (Tiny Introduction)

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

1. Import pandas and matplotlib.pyplot. Read data/activity.csv with pandas.read_csv() and inspect the table and column names.
2. Calculate the total of the minutes column.
3. Create a bar chart using the day and minutes columns. Give it a title and label both axes.
4. Save the figure as activity.png before calling show(). If a display window is unavailable, inspect the saved image. Keep this introduction to one table, one total, and one chart.

## Run your work

Run from this topic folder so the relative CSV path works. No network request is needed after installing the packages.

Run `.venv/Scripts/python.exe main.py` in Windows PowerShell or `.venv/bin/python main.py` on macOS/Linux.

## Check your work

- The total is 60 minutes.
- The chart has three bars with heights 15, 20, and 25 and labelled axes.

Keep your edited files and record a prediction, an observed result, installed versions, and a question in notes.md.

## Reference

[Pandas plotting introduction](https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html)
