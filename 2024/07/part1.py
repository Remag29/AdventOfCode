def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


class Equation:
    def __init__(self, result: int, composants: list[int]):
        self.result = result
        self.composants = composants
        self.operators = []

    def is_solvable(self) -> bool:
        new_main_numbers = [self.composants[0]]

        for composant in self.composants[1:]:
            main_numbers = new_main_numbers
            new_main_numbers = []

            for main_number in main_numbers:
                addition = main_number + composant
                multiplication = main_number * composant

                if addition <= self.result:
                    new_main_numbers.append(addition)
                if multiplication <= self.result:
                    new_main_numbers.append(multiplication)

        if self.result in new_main_numbers:
            return True
        else:
            return False


if __name__ == '__main__':
    print("Starting resolution...")

    lines = load_data()

    solvable = 0
    for line in lines:
        equation = Equation(int(line.split(':')[0]), [int(x) for x in line.split(':')[1].strip().split(' ')])
        if equation.is_solvable():
            solvable += equation.result

    print(f'The resutl is {solvable}')

    # 850 To low
