def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = [lst[0:3], lst[3:6], lst[6:9]]

    calculations = {
        'mean': [
            [sum(col)/3 for col in zip(*matrix)],
            [sum(row)/3 for row in matrix],
            sum(lst)/9
        ],
        'variance': [
            [sum((x - sum(col)/3)**2 for x in col)/3 for col in zip(*matrix)],
            [sum((x - sum(row)/3)**2 for x in row)/3 for row in matrix],
            sum((x - sum(lst)/9)**2 for x in lst)/9
        ],
        'standard deviation': [
            [((sum((x - sum(col)/3)**2 for x in col)/3) ** 0.5) for col in zip(*matrix)],
            [((sum((x - sum(row)/3)**2 for x in row)/3) ** 0.5) for row in matrix],
            (sum((x - sum(lst)/9)**2 for x in lst)/9) ** 0.5
        ],
        'max': [
            [max(col) for col in zip(*matrix)],
            [max(row) for row in matrix],
            max(lst)
        ],
        'min': [
            [min(col) for col in zip(*matrix)],
            [min(row) for row in matrix],
            min(lst)
        ],
        'sum': [
            [sum(col) for col in zip(*matrix)],
            [sum(row) for row in matrix],
            sum(lst)
        ]
    }

    return calculations
