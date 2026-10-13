# Packages: Pygame

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

Create a window with a rectangle that moves left and right while arrow keys are held. Use pygame.key.get_pressed() inside the frame loop and a small fixed movement step. Keep the entire rectangle inside the horizontal window edges. Process close events, redraw each frame, limit the loop to 60 frames per second, and call pygame.quit() after the loop. No image or sound files are required.

## Run your work

Use a local desktop environment with a graphical display. A headless terminal cannot show the game window.

Run `.venv/Scripts/python.exe main.py` in Windows PowerShell or `.venv/bin/python main.py` on macOS/Linux.

## Check your work

- Holding either arrow key moves the rectangle in the expected direction.
- The rectangle cannot leave either horizontal edge.
- Closing the window ends the program.

Keep your edited files and record a prediction, an observed result, installed versions, and a question in notes.md.

## Reference

[Pygame documentation](https://www.pygame.org/docs/)
