if which apt; then
	sudo apt update
	sudo apt install python python3
	sudo apt install python3-pip
elif which pacman; then
	sudo pacman -Sy python python3-pip
fi