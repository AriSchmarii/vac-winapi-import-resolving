# "How does VAC3 use the WinApi if I can't see any imports in the .idata segment?????"
Every VAC3 module (on Windows) uses the much loved WinApi. To make it harder for a reverse engineer, they get all their imports by calling GetProcAddress and then store all function pointers in an array.
This array can be found by searching for ```8B 0D ? ? ? ? 68 ? ? ? ? 57``` in a VAC3 module.

"How can I get around this?", you may ask. Well, the solution is actually quite simple. As mentioned above, you the modules get the imports by calling GetProcAddress. By creating a log breakpoint with x32dbg on GetProcAddress you can create a list of all the current imports (you could also hook it). Make sure to do this before a VAC module loads (only performed once per module).
Luckily for us, VAC does this linearly and not randomly, so we get a perfectly structured list of their imports.

# How to use the script?
1. (In IDA) go to File -> Script file and load resolve_imports.py
2. find the array by scanning for ```8B 0D ? ? ? ? 68 ? ? ? ? 57```
3. press Y (shortcut for "Set item type")
4. enter vac_winapi* winapi (only the data type really matters here)

![](https://github.com/AriSchmarii/vac-winapi-import-resolving/blob/main/script_example.gif)
