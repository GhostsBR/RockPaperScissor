import random
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Game:
    MAX_ROUNDS = 3
    MAX_CARDS = 3
    RANDOM_CARDS = True
    ONLY_ONE_ROUND = True
    Computer_Points = 0
    Round = 1

    def start_game(self, player):
        self.player = player
        print(f"{bcolors.OKGREEN}Jogo iniciado!{bcolors.ENDC}\n")
        player.play_card()

    def restart_game(self, player):
        self.Computer_Points = 0
        self.Round = 1
        self.player = player
        player.points = 0
        player.cards = []
        print(f"{bcolors.OKGREEN}Jogo iniciado!{bcolors.ENDC}\n")
        player.play_card(self)

    def play_round(self, card, player):
        computerCard = random.randint(0, 2)
        computerCardPicked = 'NONE'
        if computerCard == 0:
            computerCardPicked = 'Pedra'
        elif computerCard == 1:
            computerCardPicked = 'Papel'
        elif computerCard == 2:
            computerCardPicked = 'Tesoura'
        print(f"\n{bcolors.BOLD}{player.get_name(self).upper()}{bcolors.ENDC} {bcolors.HEADER}>{bcolors.ENDC}{bcolors.BOLD} {card}{bcolors.ENDC} {bcolors.HEADER}VS{bcolors.ENDC} {bcolors.BOLD}{computerCardPicked}{bcolors.ENDC} {bcolors.HEADER}<{bcolors.ENDC} {bcolors.BOLD}COMPUTADOR{bcolors.ENDC}\n")
        if card == computerCardPicked:
            print(f"{bcolors.WARNING}Round empatado!{bcolors.ENDC}")
        else:
            if self.game_getwinner(card, computerCardPicked):
                if self.ONLY_ONE_ROUND:
                    player.add_points(self)
                    self.finish_game(player)
                else:
                    print(f"{bcolors.OKGREEN}Você ganhou o round!{bcolors.ENDC}")
                    player.add_points(self)
            else:
                if self.ONLY_ONE_ROUND:
                    player.computer_add_points(self)
                    self.finish_game(player)
                else:
                    print(f"{bcolors.FAIL}Você perdeu o round!{bcolors.ENDC}\n")
                    player.computer_add_points(self)
        self.next_round(player)

    def next_round(self, player):
        if self.MAX_ROUNDS <= self.Round:
            self.finish_game(player)
        else:
            pp = player.get_points(self)
            cp = self.computer_get_points()
            if pp > (self.MAX_ROUNDS / 2) and pp > cp:
                self.finish_game(player)
            if cp > (self.MAX_ROUNDS / 2) and cp > pp:
                self.finish_game(player)
            self.Round += 1
            player.play_card(self)

    def finish_game(self, player):
        pp = player.get_points(self)
        cp = self.computer_get_points()
        if pp > cp:
            print(f"\n{bcolors.OKGREEN}Parabéns, você venceu a partida!{bcolors.ENDC}")
        elif pp < cp:
            print(f"\n{bcolors.FAIL}Não foi dessa vez, você perdeu a partida!{bcolors.ENDC}")
        else:
            print(f"\n{bcolors.WARNING}A partida finalizou sem um vencedor, ambos os jogadores empataram!{bcolors.ENDC}")
        self.play_again(player)

    def play_again(self, player):
        response = input(f"\n{bcolors.OKCYAN}Jogar novamente? (Sim/Não){bcolors.ENDC}\n")
        if response.lower() == "sim" or response.lower() == "sin" or response.lower() == "si" or response.lower() == "s" or response.lower() == "y" or response.lower() == "yes":
            self.restart_game(player)
        elif response.lower() == "não" or response.lower() == "nao" or response.lower() == "na" or response.lower() == "n" or response.lower() == "no" :
            quit()
        else:
            print(f"{bcolors.WARNING}Resposta inválida! Responda com SIM ou NÃO.{bcolors.ENDC}")
            self.play_again(player)

    def game_getwinner(self, card1, card2):
        if card1 == 'Pedra':
            if card2 == 'Tesoura':
                return True
            elif card2 == 'Papel':
                return False
        elif card1 == 'Papel':
            if card2 == 'Pedra':
                return True
            elif card2 == 'Tesoura':
                return False
        elif card1 == 'Tesoura':
            if card2 == 'Pedra':
                return False
            if card2 == 'Papel':
                return True

    def computer_add_points(self):
        self.Computer_Points += 1

    def computer_get_points(self):
        return int(self.Computer_Points)


class Player(Game):
    name = "Player"
    cards = []
    points = 0

    def __init__(self):
        self.name = input(f"{bcolors.OKCYAN}Digite seu nome: {bcolors.ENDC}")
        print("")

    def add_cards(self):
        if self.RANDOM_CARDS:
            for i in range(self.MAX_CARDS):
                value = random.randint(0, 2)
                if value == 0:
                    self.cards.append('Pedra')
                elif value == 1:
                    self.cards.append('Papel')
                elif value == 2:
                    self.cards.append('Tesoura')
        else:
            if self.MAX_CARDS % 3 == 0:
                for i in range(self.MAX_CARDS):
                    self.cards.append('Pedra')
                    self.cards.append('Papel')
                    self.cards.append('Tesoura')
            else:
                print("Para iniciar o jogo sem cartas aleatórias é necessário que o número máximo de cartas seja divisivel por 3")

    def play_card(self):
        if self.Round == 1 and not self.cards:
            self.add_cards()
        print(f"\n{bcolors.OKCYAN}Selecione a carta que deseja jogar:{bcolors.ENDC}")
        for i in range(len(self.cards)):
            print(f"{bcolors.BOLD}{i+1} - {self.cards[i]}{bcolors.ENDC}")
        response = input("")
        try:
            response = int(response)
            response -= 1
        except:
            print(f"\n{bcolors.WARNING}Você deve digitar o número da carta que deseja jogar!{bcolors.ENDC}")
            self.play_card()
        if response < 0 or response > len(self.cards) - 1:
            print(f"\n{bcolors.WARNING}O valor digitado não existe!{bcolors.ENDC}")
            self.play_card()
        playcard = self.cards[response]
        self.cards.pop(response)
        Game.play_round(self, playcard, Player)

    def get_name(self):
        return self.name

    def add_points(self):
        self.points += 1

    def get_points(self):
        return int(self.points)

