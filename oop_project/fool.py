done = False

player1 = Player({})
player2 = Player()

while True:
    player1.play()
    player2.play()
    if player1.all_char_done() or player2.all_char_done():
        break
