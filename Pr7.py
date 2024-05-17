import math


def Func(x, y):
    return math.exp(-x - y) + 0.5 * y ** 2


def Euler(X0, Y0, B, N):
    H = (B - X0) / N
    X = X0
    Z = Y0

    for i in range(1, N + 1):
        Y = Z
        F = Func(X, Y)
        Y = Z + H * F
        X = X + H

        print(X, Y)

        Z = Y


def EulerCauchy(X0, Y0, B, N):
    H = (B - X0) / N
    H2 = H / 2
    X = X0
    Z = Y0
    Y = Z

    for i in range(1, N):
        F = Func(X, Y)
        V = F
        Y = Z + H * F
        X = X + H
        F = Func(X, Y)
        Y = Z + H2 * (V + F)

        print(X, Y)

        Z = Y


def ImprovedEuler(X0, Y0, B, E, N):
    H = (B - X0) / N
    H2 = H / 2
    X = X0
    Z = Y0
    W = Z

    for i in range(1, N + 1):
        Y = Z
        F = Func(X, Y)
        V = F
        X = X + H
        while True:
            V = W
            F = Func(X, Y)
            P = Z + H2 * (V + F)
            R = P - W

            if abs(R) < E:
                Y = P
                Z = P
                break
            else:
                W = P
        print(X, Y)


def RungeKutta(X0, Y0, B, N):
    H = (B - X0) / N
    H2 = H / 2
    X = X0
    Z = Y0
    Y = Z

    for i in range(0, N + 1):
        F = Func(X, Y)
        K1 = H * F
        X = X + H2
        Y = Z + K1 / 2

        F = Func(X, Y)
        K2 = H * F
        Y = Z + K2 / 2

        F = Func(X, Y)
        K3 = H * F
        X = X + H2
        Y = Z + K3

        F = Func(X, Y)
        K4 = H * F
        Y = Z + (K1 + 2 * (K2 + K3) + K4) / 6

        print(X, Y)
        Z = Y


if __name__ == "__main__":
    print("Метод Ейлера")
    Euler(0.5, 2, 1, 10)
    print("\n\nМетод Ейлера Коши")
    EulerCauchy(0.5, 2, 1, 10)
    print("\n\nУдосконалений метод Ейлера з ітераційною обробкою")
    ImprovedEuler(0.5, 2, 1, 0.1 * 10 ** -6, 10)
    print("\n\nМетод Рунге-Кутта")
    RungeKutta(0.5, 2, 1, 10)
