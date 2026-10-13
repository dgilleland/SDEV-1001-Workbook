# Optional Extra Topics

Use this folder only if time remains and your instructor selects an extension. These are ungraded starter ideas, not additional required course work.

## Small extension: automated checks

We've checked results by running programs. Let's record some expectations as tests using Python's built-in unittest module.

Complete is_positive(number), then write checks for a positive number, zero, and a negative number. Only numbers greater than zero should return True.

Open helpers.py and test_helpers.py. Replace the deliberate failing test placeholder with assertions that call the function. Complete at least one assertion before implementing the function; run it and observe the failure, then implement and rerun.

From this folder, run `py -m unittest -v` on Windows or `python3 -m unittest -v` on macOS/Linux. If your installation uses `python` for Python 3, use that instead. No packages need installing.

Your completed tests should pass. Briefly break the implementation to confirm a test catches the change, then restore it. Record what you learned in notes.md.

## Other possible directions

- Sets: remove duplicates from a list and compare the result with the original.
- JSON: save and reload a small dictionary using the standard library.
- Command-line arguments: adapt a previous program to accept one argument using argparse.

Choose one direction with your instructor before adding files. Keep the example small and describe how you checked it.
