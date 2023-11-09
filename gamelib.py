def winending():
	printinfo("Congratulations, You Win!")
	exit(0)

def loseending():
	printwarning("You lose!")
	printerror("RuntimeError: CRASHING Computer........")
	raise RuntimeError("You lose!")