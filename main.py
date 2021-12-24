import random,time,termcolor
class deck:
    def __init__(self,cards):self.cards=cards
    def shuffle(self,*overflow):self.cards=random.sample(self.cards,len(self.cards))
    def sort(self,*overflow):self.cards.sort()
    def selectcard(self,card,*overflow):
        try:
            if card[0]in self.cards:self.selected=card[0]
            else:print('Card not in deck')
        except IndexError:print('You must select a card')
    def checknext(self):
        try:
            if self.selected in self.cards:
                if (c:=self.cards.pop(0))==self.selected:
                    self.cards.append(c)
                    termcolor.cprint(c, 'green')
                    return True
                termcolor.cprint(c, 'red')
                self.cards.append(c)
            return False
        except AttributeError:
            print('No card selected')
            return True

def main():
    karty=[str(i+1)for i in range(32)]
    Deck=deck(karty)
    def play(*overflow):
        while True:
            if Deck.checknext():break
            time.sleep(1)
    def passingfunc(*overflow):print('Not a valid command')
    def end(*overflow):return True

    commands={
        '!shuffle':Deck.shuffle,
        '!sort':Deck.sort,
        '!select':Deck.selectcard,
        '!play':play,
        '!exit':end
    }

    while True:
        try:s=input('command: ')
        except KeyboardInterrupt:exit()
        if commands.get(s.split(' ')[0],passingfunc)(s.split(' ')[1:]or['']):break
    Deck.sort()
    print(*Deck.cards)
    input()

if __name__=='__main__':main()