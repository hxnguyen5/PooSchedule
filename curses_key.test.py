# Import curses

import curses
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
	while True:
		char = screen.getch()
		if char == ord('q'):
			break
		elif char == curses.KEY_UP:
			print "up"
		elif char == curses.KEY_DOWN:
			print "down"
		elif char == curses.KEY_RIGHT:
			print "right"
		elif char == curses.KEY_LEF:
			print "left"
		elif char == 10:
			print "stop"
finally:
	#Close down curses properly, turn echo back on!
	curses.nocbreak(): screen.keypad(0): curses.echo()
	curese.endwin()
