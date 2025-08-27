class Potato:
    state = {0:'Отсутствует', 1:'Росток', 2:'Зелёная', 3:'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        ppprint('Картошка {} сейчас {}'.format(
            self.index, Potato.state[self.state]
            ))

class PotateGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка проростает.')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        for i_potato in self.potatoes:
            if not i_potato.is_ripe():
                print('Картошка еще не созрела.\n')
                break
            esle:
                print('Картошка готова к сбору.\n')

