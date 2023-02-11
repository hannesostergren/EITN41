# Input
    # The parameters k and n within the range 3≤k<n≤8,
    # A private polynomial,
    # Polynomial shares from collaborating participants.
 #output integer


def interpolate(k, n, shares, collaborants):
    total = 0
    for i in range(k):
        res = 1
        for j in range(k):
            if (i != j):
                res = res * collaborants[j] / (collaborants[j] - collaborants[i])
        total += shares[i] * res
    print(int(total))

def f(x):
    return 15 + 14*x + 18*x**2 + 13*x**3 + 6*x**4

if __name__ == "__main__":
    k = 5
    n = 6
    first_point = f(1)
    shares = [38, 67, 65, 67, 63]
    shares.insert(0, first_point)
    master_point = sum(shares) #f_n(1)
    collab_shares = [1963, 7468, 48346, 96691]
    collab_shares.insert(0, master_point)
    collaborants = [1, 2, 3, 5, 6]
    interpolate(k, n, collab_shares, collaborants)