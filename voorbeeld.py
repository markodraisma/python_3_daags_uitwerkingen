def upper(lijst):
    for woord in lijst:
        yield woord.upper()[::-1]

if __name__ == "__main__":

    woorden = ["een", "twee", "drie"]
    print(list(upper(woorden)))

    for x in upper(woorden):
        print(x)
