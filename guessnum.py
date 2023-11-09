from random import randint
from stdlib import *

def initnum(difficulty: int):
	global ansnum
	if difficulty == 1:
		ansnum = randint(1, 100)
	elif difficulty == 2:
		ansnum = randint(1, 250)
	elif difficulty == 3:
		ansnum = randint(1, 500)
	else:
		ansnum = randint(1, difficulty)


def askuserinit():
	global difficulty
	difficulty = keepasks(f"{ascii.color.cyan}Difficulty({ascii.color.purple}E{ascii.color.yellow}[{ascii.color.green}asy{ascii.color.yellow}]{ascii.color.reset}, {ascii.color.purple}N{ascii.color.yellow}[{ascii.color.green}ormal{ascii.color.yellow}]{ascii.color.reset}, {ascii.color.purple}H{ascii.color.yellow}[{ascii.color.green}ard{ascii.color.yellow}]/{ascii.color.green}1{ascii.color.reset}, {ascii.color.green}2{ascii.color.reset}, {ascii.color.green}3{ascii.color.reset}/{ascii.color.green}custom{ascii.color.yellow}({ascii.color.purple}n{ascii.color.yellow}{{{ascii.color.cyan}100{ascii.color.yellow}}}{ascii.color.yellow}){ascii.color.blue}){ascii.color.reset}: {ascii.color.red}")
	difficulty = difficulty.lower()
	if difficulty == "e" or difficulty == "easy":
		difficulty = 1
	elif difficulty == "n" or difficulty == "normal":
		difficulty = 2
	elif difficulty == "h" or difficulty == "hard":
		difficulty = 3
	elif difficulty.startswith("n"):
		try:
			difficulty = difficulty.replace("n", "")
			difficulty = int(difficulty)
		except ValueError:
			printerror("Please input a valid difficulty number.")
			askuserinit()
	else:
		try:
			difficulty = int(difficulty)
		except ValueError:
			printerror("Please input a valid difficulty.")
			askuserinit()
		if difficulty not in [1, 2, 3]:
			printerror("Please input a valid difficulty number(1 for easy, 2 for noraml, 3 for hard or n{num} for custom.")
			askuserinit()

def winending():
	printinfo("Congratulations, You Win!")
	exit(0)

def loseending():
	printwarning("You lose!")
	printerror("RuntimeError: CRASHING Computer........")
	raise RuntimeError("You lose!")

def userdet():
	guestries = 0
	while True:
		currentGuest = keepasks(f"{ascii.color.yellow}Please enter your guess number {ascii.color.green}> {ascii.color.lgreen}")
		try:
			currentGuest = int(currentGuest)
			guestries += 1
		except ValueError:
			printerror("Please input a valid guest number!")
			continue
		if currentGuest > ansnum:
			if currentGuest < ansnum:
				printwarning("Number too big.")
			elif currentGuest+30 < ansnum:
				printwarning("Number very big.")
			elif currentGuest+15 < ansnum:
				printwarning("quiet Big, but close enough")
			else:
				printwarning("little big, but very close")
		elif currentGuest < ansnum:
			if currentGuest+50 < ansnum:
				printwarning("Number too small.")
			elif currentGuest+35 < ansnum:
				printwarning("Number very small.")
			elif currentGuest+15 < ansnum:
				printwarning("quiet small, but close enough")
			else:
				printwarning("little small, but very close")
		elif currentGuest == ansnum:
			winending()
		elif guestries == 10:
			printwarning("How are you still not getting there? Come On bro!")
		elif guestries == 15:
			printwarning("Bro come on, I beliven you!")
		elif guestries == 17:
			printwarning("Ok bro, 3 more chances...")
		elif guestries >= 20:
			loseending()


def main():
	askuserinit()
	initnum(difficulty)
	userdet()

if __name__ == "__main__":
	main()