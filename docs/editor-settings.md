# VS Code, EditorConfig, and Line Endings

When we save a file, our editor writes invisible characters to mark the end of each line. **LF** uses a line-feed character; **CRLF** uses a carriage return followed by a line feed. This workbook uses LF for ordinary text files and CRLF for Windows batch scripts.

## Which file does what?

| Configuration file | Used by | Purpose in this workbook |
| --- | --- | --- |
| [`.vscode/settings.json`](../.vscode/settings.json) | VS Code | Sets the default line endings for this workspace. |
| [`.editorconfig`](../.editorconfig) | Editors with EditorConfig support | Shares line-ending preferences across editors. |
| [`.gitattributes`](../.gitattributes) | Git | Normalizes text in the repository and controls checkout line endings. |

Git does not use `.editorconfig` to configure your editor. Each tool reads its own configuration.

## VS Code workspace settings

Open the **workbook root folder** in VS Code so its `.vscode/settings.json` applies. Opening only a topic subfolder does not load the root folder's VS Code settings.

Our settings are:

```json
{
    "files.eol": "\n",
    "[bat]": {
        "files.eol": "\r\n"
    }
}
```

`files.eol` sets the default for new files. The `[bat]` section overrides it for files using VS Code's Windows batch language mode, normally `.bat` and `.cmd` files. Existing files can retain their current endings.

To inspect these settings, open the Command Palette and choose **Preferences: Open Workspace Settings (JSON)**. Workspace settings belong to this project; user settings apply across projects. Language-specific settings can also affect the result. See [VS Code's settings documentation](https://code.visualstudio.com/docs/configure/settings).

## EditorConfig

EditorConfig is an editor-independent standard. Our file contains:

```ini
root = true

[*]
end_of_line = lf

[*.{bat,cmd}]
end_of_line = crlf
```

- `root = true` stops the search for additional EditorConfig files in parent folders.
- `[*]` applies the LF preference to files covered by this configuration.
- `[*.{bat,cmd}]` overrides that preference for batch scripts.

These rules specify line endings only; they do not set indentation or enable a code formatter. Other editors may support EditorConfig directly or require a plugin. See the [EditorConfig documentation](https://editorconfig.org/).

For VS Code, install [EditorConfig for VS Code](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig) (`EditorConfig.EditorConfig`) if you want it to read this file. The extension is optional for our line-ending defaults because `.vscode/settings.json` already supplies them.

## Why keep both editor configurations?

Yes, the line-ending preference is duplicated. The VS Code settings work without an extra extension, while EditorConfig provides the same preference for other compatible editors. Keep the two files consistent if you change that preference.

`.gitattributes` has a separate role: Git normalizes text when staging it and applies the checkout policy. It cannot force an editor to save a file with particular endings.

## Fixing a CRLF warning

If `git add` reports that CRLF will be replaced by LF, the working file has CRLF endings while the repository expects LF. The warning alone does not mean staging failed.

For a Python file, let's fix the working copy in VS Code:

1. Open the file and find **CRLF** in the status bar.
2. Click **CRLF** and choose **LF**.
3. Save the file, then stage it again.

You can inspect both versions from the workbook root:

```sh
git ls-files --eol -- fast-track/step-01.py
```

Replace the path with the file you are checking. For a staged Python file, `i/lf` means the index (staged copy) uses LF, and `w/lf` means the working copy does too. With `w/crlf`, the working file still needs conversion. Leave Windows batch scripts using their intended CRLF endings.

Once the editor and Git agree, ordinary saves and staging should no longer produce this conversion warning. A pasted or externally created file may still need a one-time conversion.
