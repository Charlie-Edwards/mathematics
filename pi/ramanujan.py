import colorama, math

k = 0
term = (math.factorial(4*k) * (1103 + 26390*k)) / (math.factorial(k)**4 * 396**(4*k))

pi = 1 / ((2*math.sqrt(2)/9801) * term)

pi = str(pi)
truepi = "3.1415926535897932"

for truedigit in truepi:
    print(f"{colorama.Fore.GREEN}{truedigit}{colorama.Fore.RESET}", end="")

print("")

for i, digit in enumerate(pi):
    if i < len(truepi) and digit == truepi[i]:
        print(f"{colorama.Fore.GREEN}{digit}{colorama.Fore.RESET}", end="")
    else:
        print(f"{colorama.Fore.RED}{digit}{colorama.Fore.RESET}", end="")
