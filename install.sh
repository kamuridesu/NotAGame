if which apt 2>&1 > /dev/null; then
	sudo apt update
	sudo apt install python python3 -y
	sudo apt install python3-pip -y
elif which pacman 2>&1 > /dev/null; then
	sudo pacman --noconfirm -Sy python python3-pip
fi
