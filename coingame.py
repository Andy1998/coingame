import random
import library

f = open("score.txt", "r+")
highscore = int(f.read())
print "Coin Guessing Game.  All time high score:", highscore, "correct"
live = 1
score = 0
side = ["head","tail"]

while live == 1:
	sidenum = random.randint(0,1)
	guess = library.side_input("Predict head or tail> ")
	print "It is", side[sidenum]
	if guess == side[sidenum]:
		score = score + 1
		print "Your score is", score
	else:
		live = 0
		print "Game over"
		if score > highscore:
			f.seek(0)
			f.truncate()
			f.write(str(score))
			highscore = score
print "Your Score:", score, " All time highscore:", highscore