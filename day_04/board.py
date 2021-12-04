class Board:
    def __init__(self):
        self.totalnums = set()
        self.rows = []
        self.columns = [set() for i in range(5)]
        self.total = 0

    def add_numbers(self, numbers):
        for row in numbers:
            self.totalnums.update(row)
            self.rows.append(set(row))

            for i in range(5):
                self.columns[i].add(row[i])

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