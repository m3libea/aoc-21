class Board:
    def __init__(self):
        self.totalnums = set()
        self.rows = [ set() ] * 5
        self.columns = [ set() ] * 5 
        self.total = 0

    def add_numbers(self, numbers):
        for i in range(5):
            self.totalnums.update(numbers[i])
            self.rows[i] = numbers[i]

            for n in numbers[i]:
                self.columns[i].add(n)

    def play_num(self, num) -> bool:
        winner = False

        if num in self.totalnums:
            self.totalnums.remove(num)

            for i in range(4):
                if num in self.rows[i]:
                    self.rows[i].remove(num)                
                if num in self.columns[i]:
                    self.columns[i].remove(num)
                
                if len(self.rows[i]) == 0 or len(self.columns[i]) == 0:
                    winner = True
                    break
        return winner

    def calculate_remaining_sum(self) -> int:
        return sum(self.totalnums)