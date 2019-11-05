from lib.game import Game

def main():
    game = Game()
    game.Start()

    while True:
        game.Event()
        game.Update()
        game.Draw()


if __name__ == "__main__":
    main()
