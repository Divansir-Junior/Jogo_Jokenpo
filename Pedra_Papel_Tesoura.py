import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ["Pedra", "Papel", "Tesoura"]
        self.player_score = 0
        self.computer_score = 0

    def play(self):
        print("Bem-vindo ao Pedra, Papel e Tesoura!")
        print("Vamos começar o jogo.")
        print()

        while True:
            player_choice = self.get_player_choice()
            computer_choice = self.get_computer_choice()

            print("Você escolheu:", player_choice)
            print("O computador escolheu:", computer_choice)
            print()

            winner = self.determine_winner(player_choice, computer_choice)

            if winner == "Player":
                self.player_score += 1
                print("Você venceu esta rodada!")
            elif winner == "Computer":
                self.computer_score += 1
                print("O computador venceu esta rodada!")
            else:
                print("Empate!")

            print("Placar:")
            print("Você:", self.player_score)
            print("Computador:", self.computer_score)
            print()

            play_again = input("Deseja jogar novamente? (s/n): ")
            if play_again.lower() != "s":
                break

        print("Obrigado por jogar!")

    def get_player_choice(self):
        while True:
            choice = input("Escolha sua jogada (Pedra, Papel ou Tesoura): ").capitalize()
            if choice in self.choices:
                return choice
            else:
                print("Escolha inválida. Por favor, tente novamente.")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return None

        if (player_choice == "Pedra" and computer_choice == "Tesoura") or \
                (player_choice == "Papel" and computer_choice == "Pedra") or \
                (player_choice == "Tesoura" and computer_choice == "Papel"):
            return "Player"
        else:
            return "Computer"

game = RockPaperScissors()
game.play()
