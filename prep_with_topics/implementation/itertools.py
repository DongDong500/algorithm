import itertools


if __name__ == "__main__":
    nCr = itertools.combinations([i for i in range(5)], 2)
    print("nCr:", *nCr)