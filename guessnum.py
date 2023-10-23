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


def askuserinit():
	global difficulty
	difficulty = keepasks("Difficulty(E[asy], N[ormal], H[ard]/1, 2, 3): ")
	difficulty = difficulty.lower()
	if difficulty == "e" or difficulty == "easy":
		difficulty = 1
	elif difficulty == "n" or difficulty == "normal":
		difficulty = 2
	elif difficulty == "h" or difficulty == "hard":
		difficulty = 3
	else:
		try:
			difficulty = int(difficulty)
		except ValueError:
			printerror("Please input a valid difficulty.")
			raise ValueError("Invalid difficulty")

def userdet():
	while True:
		currentGuest = keepasks("Guest number: ")
		try:
			currentGuest = int(currentGuest)
		except ValueError:
			printerror("Please input a valid guest number.")
			continue
		if currentGuest > ansnum:
			printwarning("Too big.")
		elif currentGuest < ansnum:
			printwarning("Too small.")
		elif currentGuest == ansnum:
			printinfo("You got the one")



def main():
	askuserinit()
	initnum(difficulty)
	userdet()
	

if __name__ == "__main__":
	main()