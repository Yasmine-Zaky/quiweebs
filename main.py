from GAME2 import Game
g = Game()

while g.running:
	g.currently_in_menu.display_menu()
	g.game_loop()