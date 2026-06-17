from matrix_multiplication import matmul

def marbles_experiment(): #no probability uses, all is definitive
    n = int(input("Enter number of vertices: "))


    M = [[0]*n for _ in range(n)]

    while(True):
        prompt = input("Want to add a path? (y/n): ")
        if(prompt == 'y' or prompt == 'Y'):
            j = int(input("Path from vertex: "))
            i = int(input("to vertex: "))
            M[i][j] = 1
            print("Path added")
        else:
            break

    S = [[0] for _ in range(n)]

    for i in range(n):
        x = float(input(f"How many marbles on vertex {i}: "))
        S[i][0] = x

    t = int(input("How many time clicks later do you want to check? "))

    for _ in range(t):
        S = matmul(M,S)

    print(f"This is the state of the system after {t} time clicks: ")
    print(S)



