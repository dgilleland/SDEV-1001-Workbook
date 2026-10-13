# Packages: Pygame

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

1. Import pygame, initialise it, create a window using the supplied dimensions, and create a Clock.
2. Build a loop controlled by a running variable. Process pygame.event.get() each frame and respond to pygame.QUIT.
3. Fill the background, draw a rectangle, update the display, and use the clock to limit the loop to 60 frames per second.
4. Call pygame.quit() after leaving the loop. Close the window and confirm that the program ends.

## Run your work

Use a local desktop environment with a graphical display. A headless terminal cannot show the game window.

Run `.venv/Scripts/python.exe main.py` in Windows PowerShell or `.venv/bin/python main.py` on macOS/Linux.

## Check your work

- The window shows one rectangle without trails from previous frames.
- The close button exits the loop and ends the program.

Keep your edited files and record a prediction, an observed result, installed versions, and a question in notes.md.

## Reference

[Pygame documentation](https://www.pygame.org/docs/)
