if which apt 2>&1 > /dev/null; then
    python3 main.py
elif which pacman 2>&1 > /dev/null; then
    python main.py
fi
