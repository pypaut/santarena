from lib.Game import Game

def main():
    game = Game()

    while True:
        game.Event()
        game.Update()
        game.Draw()


if __name__ == "__main__":
    main()
