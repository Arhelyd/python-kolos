import re

tekst="To jest test. To jest przykład działania testowych wyrażeń regularnych."

finditerObj=re.finditer(r'(.jest\W*test*)',tekst)
for slowo in finditerObj:
    print(slowo.group(0))
