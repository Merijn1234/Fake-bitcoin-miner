import colorama
import time
from colorama import Fore

btc = 0


for x in range(100000):
    time.sleep(0.12)
    print(Fore.RED + 'Have searched in: ', btc, "Wallets", "Have found btc:", "0.000000000")
    btc += 1
    if btc == 96770:
        break

print(Fore.GREEN + "Have found 1.43356 BTC!")











