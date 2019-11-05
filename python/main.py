from lib.game import Game


def main():
    game = Game()
    game.start()

    while True:
        game.event()
        game.update()
        game.draw()


if __name__ == "__main__":
    main()
