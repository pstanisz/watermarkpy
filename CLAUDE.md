# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

watermarkpy is a small desktop tool for watermarking images. It is at an early stage: the entire app is `main.py`, and the watermarking itself (compositing the mark onto the image) is not implemented yet. So far the app only lets the user pick a watermark file and an image file and previews each one.

## Running

There is no `requirements.txt`, build step, linter config or test suite. Dependencies are Tkinter (ships with standard CPython) and OpenCV:

```
pip install opencv-python
python main.py
```

## Architecture

- `main.py` is a flat script: it builds a Tkinter window at module level, wires two buttons to `browse_wmark()` / `browse_image()`, and ends with `window.mainloop()`. Importing the module launches the GUI, so new logic you want to test or reuse belongs in functions or modules that don't run on import.
- The UI uses Tkinter and image I/O uses OpenCV (`cv2.imread` / `cv2.imshow`). The loaded images live only in function locals and are not stored anywhere, so a watermarking step will need shared state (for example module-level variables or a class) to hold both images.
- The two GUI toolkits run side by side: preview windows come from `cv2.imshow`, but nothing calls `cv2.waitKey`, and only Tkinter's `mainloop` drives events. OpenCV windows may therefore not repaint properly. Keep this in mind when changing how images are displayed (one option is to render them in Tkinter through Pillow `ImageTk`).
- `cv2.imread` returns `None` without raising when the user cancels the file dialog or picks an unreadable file. The current code does not handle that case.
