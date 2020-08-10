def get_matrix():
    rows, columns = input().split()
    matrix = [input().split(" ") for _ in range(int(rows))]
    return matrix


list_one = get_matrix()
list_two = get_matrix()

if len(list_one) != len(list_two) or len(list_one[0]) != len(list_two[1]):
    print("ERROR")
else:
    together = []
    for i in range(len(list_one)):
        together.append([])
        for j in range(len(list_one[i])):
            together[i].append(str(int(list_one[i][j]) + int(list_two[i][j])))

    for i in range(len(together)):
        print(" ".join(together[i]))
