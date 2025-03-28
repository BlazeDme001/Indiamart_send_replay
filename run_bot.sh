#!/bin/bash

# Open a new terminal and run main_linux_1.py
gnome-terminal -- bash -c "python3 main_linux_1.py; exec bash" &

# Open a new terminal and run main_linux_2.py
gnome-terminal -- bash -c "python3 main_linux_2.py; exec bash" &

echo "Both scripts are started in new terminal windows."
