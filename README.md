# UTY-DebugMenu
Sets your Undertale Yellow save to the debug menu, with optional LV changing.

## How does it work, technically?
The program works by finding your save file (`%LOCALAPPDATA%\Undertale_Yellow\Save.sav`), and changing the room value to `rm_mainmenu_debug`.
The LV changing is mostly the same, changing the LV value to the user input.

## Why is my computer saying its a virus?
Put simply, it's not a virus. Windows, and many other antivirus vendors will flag the program as it is made in python, packaged into an exe, and interacts with a file on your computer. It's a false positive. Don't believe me? You can build it yourself, detailed below.

## Building
First, make sure python is installed on your system, then download `pyinstaller` using the fillowing command

```> pip install pyinstaller```

Next, run the `build.bat` file. this will pack the python file into a windows executable, and set its icon.
