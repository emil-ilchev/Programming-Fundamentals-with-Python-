number_of_electrons = int(input())
filled_shells = []
def electron_distribution():
    for shell in range(1, number_of_electrons +1):
        max_electrons_in_shell = 2 * shell ** 2
        if number_of_electrons >= max_electrons_in_shell:
            filled_shells.append(max_electrons_in_shell)
        else:
            filled_shells.append(number_of_electrons)
        number_of_electrons -= 