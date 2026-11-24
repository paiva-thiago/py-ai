# Python AI and Desktop Automation Exercises

A collection of Python examples covering desktop automation with PyAutoGUI, window management on Windows, date/time basics, HTTP requests, and AI APIs including Google Gemini and DeepSeek.

## Project Structure

```text
py-ai/
|-- ai-and-apis/
|   |-- main.py          # Analyze an image with Google Gemini
|   |-- deepseek.py      # Send a chat prompt to DeepSeek
|   |-- joke.py          # Fetch and print a random dad joke
|   |-- spfc.jpg         # Example image used by main.py
|   |-- example.json     # Example JSON file
|   `-- gemini-reponse.txt
|-- pyautogui/
|   |-- intro/           # Keyboard, typing, and application examples
|   |-- position/        # Mouse movement and position detection
|   |-- color/           # Screen pixel color detection
|   |-- references/      # Image recognition and reference-image examples
|   |-- screenshots/     # Full-screen and region screenshots
|   `-- windows/         # Windows discovery and layout management
|-- pythonreview/
|   |-- review.py        # Basic Python variables, conditions, and loops
|   |-- managingdatetime.py
|   `-- randomsamples.py # Random integers, floats, choices, and shuffling
`-- .idea/               # IntelliJ/PyCharm project configuration
```

## Requirements

- Windows
- Python 3.10 or newer
- A desktop environment (some examples open and control applications)

Install the third-party packages used by the project:

```powershell
python -m pip install pyautogui pyperclip pygetwindow google-genai openai python-dotenv requests pillow opencv-python
```

Some scripts use Windows-specific applications and commands, such as Paint, Notepad, and `taskkill`, so they are intended to run on Windows.

## Gemini Image Analysis

`ai-and-apis/main.py` loads `GEMINI_API_KEY` from an environment file and asks Gemini to describe `spfc.jpg` and transcribe any text it finds.

Create `ai-and-apis/.env`:

```dotenv
GEMINI_API_KEY=your_api_key_here
```

Run it from the project directory:

```powershell
cd ai-and-apis
python main.py
```

Keep the `.env` file private and never commit API keys. The `.env` file in this folder is already excluded by `.gitignore`.

## DeepSeek Chat

`ai-and-apis/deepseek.py` sends a sample question to the DeepSeek chat API. Add your key to `ai-and-apis/.env`:

```dotenv
DEEPSEEK_API_KEY=your_api_key_here
```

Run it from the `ai-and-apis` directory:

```powershell
python deepseek.py
```

## Other Examples

### Random joke

```powershell
cd ai-and-apis
python joke.py
```

The script uses the ICanHazDadJoke public API.

### Python review

```powershell
python pythonreview/review.py
python pythonreview/managingdatetime.py
python pythonreview/randomsamples.py
```

`randomsamples.py` demonstrates Python's built-in `random` module, including `randint`, `random`, `choice`, and `shuffle`.

### PyAutoGUI examples

Run individual scripts from the project root or from their own folders:

```powershell
python pyautogui/position/auto.py
python pyautogui/color/colordetector.py
python pyautogui/intro/open_apps.py
python pyautogui/windows/windows.py
```

Examples include:

- Moving and clicking the mouse
- Typing text into active applications
- Tracking the mouse position
- Reading pixel colors
- Opening Paint and drawing a square
- Saving full-screen or region screenshots
- Finding a reference image on the screen
- Moving and resizing desktop windows
- Arranging open windows into columns

## Important Notes

- PyAutoGUI scripts can immediately move the mouse, type text, open applications, or close processes. Review a script before running it.
- Some screenshot and image-recognition scripts contain machine-specific absolute paths. Replace paths such as `C:\Users\Thiago Paiva\OneDrive - sharkcoders\20260915-python\` with a folder available on your computer.
- Reference-image scripts assume the image is in their expected relative location. `pyautogui/references/reference.png` is included for this purpose.
- Press `Ctrl+C` to stop scripts that use continuous loops.
- Window titles and layout behavior depend on the applications and screen resolution in use.
