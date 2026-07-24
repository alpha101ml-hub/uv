# /// script
# requires-python = "==3.9.12"
# dependencies = []
# ///


import sys
# import rich
# from rich import print
# import requests
print(sys.version)

# in terminal run: uv (if install you will see commands that can be used in uv)

# in terminal run: clear (to clear the terminal)

# in terminal run: uv python list (to see the list of python versions installed in your system)

# in terminal run: uv python install 3.8

# in terminal run: uv python find 3.8

# in terminal run: uv python uninstall 3.8 (if you want to uninstall python version 3.8 or any version you want to uninstall)

# in terminal run: uv run main.py (to run the main.py file using uv)
# 3.14.4 | packaged by Anaconda, Inc. | (main, Apr 14 2026, 17:00:17) [MSC v.1942 64 bit (AMD64)]

# in terminal run: uv run --python 3.9.12 main.py (to run the main.py file using uv with python version 3.9.12)
# 3.9.12 (main, May  3 2022, 01:55:40) [MSC v.1929 64 bit (AMD64)]

# in terminal run: uv run --with rich --python 3.9 main.py
# it will run the main.py file using uv with python version 3.9 and rich module installed in that python version without installing rich module in your current python version.

# in terminal run: uv run --with rich --with requests --python 3.9 main.py
# it will run the main.py file using uv with python version 3.9 and rich and requests modules installed in that python version without installing rich and requests modules in your current python version.


# requires-python = ">=3.9"

# in terminal run: uv init --script main.py --python 3.9.12

# in terminal run: uv run main.py (to run the main.py file using uv with python version 3.9.12)

# in terminal run: uv add --script main.py "rich" (to add rich module in main.py script)

# in terminal run: uv add --script main.py "requests" (to add requests module in main.py script)