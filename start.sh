if which apt; then
    python3 main.py
elif which pacman; then
    python main.py
fi