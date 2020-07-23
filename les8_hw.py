from random import randint, sample


class Card:
    def __init__(self, title):
        self.title = title
        self.nums = sample(range(1, 90), 15)
        self.field = [self.nums[:5], self.nums[5:10], self.nums[10:]]
        for row in self.field:
            row.sort()
            for i in range(4, 8):
                row.insert(randint(0, i), ' ')
        self.card = '\n'.join('\t'.join(map(str, row)) for row in self.field)

    def __str__(self):
        return f'{self.title:-^34}\n' + self.card + '\n' + '-' * 34

    def closed(self) -> bool:
        return set(self.nums) == {'-'}


class Game:
    def __init__(self):
        self.user_card = Card('Игрок')
        self.comp_card = Card('Компьютер')
        self.kegs = sample(range(1, 91), 90)

    def play(self):
        keg = self.kegs.pop()
        print(f'\nНовый бочонок: {keg} (осталось: {len(self.kegs)})')
        print(f'\n{self.user_card}')
        print(f'user_list = {self.user_card.nums}')
        print(f'\n{self.comp_card}')
        print(f'comp_list = {self.comp_card.nums}')

        user_answer = input('\nЗачеркнуть цифру? (y/n)\t').lower().strip()

        if user_answer == 'y' and keg not in self.user_card.nums or user_answer != 'y' and keg in self.user_card.nums:
            return 2

        if keg in self.user_card.nums:
            self.user_card.nums.insert(self.user_card.nums.index(keg), '-')
            self.user_card.nums.pop(self.user_card.nums.index(keg))
            if self.user_card.closed():
                return 1

        if keg in self.comp_card.nums:
            self.comp_card.nums.insert(self.comp_card.nums.index(keg), '-')
            self.comp_card.nums.pop(self.comp_card.nums.index(keg))
            if self.comp_card.closed():
                return 2

        return 0


if __name__ == '__main__':
    game = Game()
    while True:
        score = game.play()
        if score == 1:
            print('You win')
            break
        elif score == 2:
            print('You lose')
            break
