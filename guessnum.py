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

def winending():
	printinfo("Congratulations, you win!")
	exit(0)

def loseending():
	printwarning("You lose!")
	printerror("RuntimeError: CRASHING Computer........")
	raise RuntimeError("You lose!")

def userdet():
	guestries = 0
	while True:
		currentGuest = keepasks("Guest number: ")
		try:
			currentGuest = int(currentGuest)
			guestries += 1
		except ValueError:
			printerror("Please input a valid guest number.")
			continue
		if currentGuest > ansnum:
			if currentGuest < ansnum:
				printwarning("Too big.")
			elif currentGuest+30 < ansnum:
				printwarning("very big.")
			elif currentGuest+15 < ansnum:
				printwarning("big, but close enough")
			else:
				printwarning("big, but very close")
		elif currentGuest < ansnum:
			if currentGuest+50 < ansnum:
				printwarning("Too small.")
			elif currentGuest+35 < ansnum:
				printwarning("very small.")
			elif currentGuest+15 < ansnum:
				printwarning("small, but close enough")
			else:
				printwarning("small, but very close")
		elif currentGuest == ansnum:
			winending()
		if guestries == 5:
			printwarning("You tried a few times, come on")
		elif guestries == 10:
			printwarning("You tried these much?? Come On bro")
		elif guestries == 20:
			printwarning("Bro come on, i beliven you")
		elif guestries == 23:
			printwarning("Ok bro, 2 more chances...")
		elif guestries >= 25:
			loseending()


def main():
	askuserinit()
	initnum(difficulty)
	userdet()

if __name__ == "__main__":
	main()