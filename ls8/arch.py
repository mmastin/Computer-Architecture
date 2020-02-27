for a in [False, True]:
    for b in [False, True]:
        print(f'{a} - {b} -- {not (a or not b) and b or not (a or b}')

