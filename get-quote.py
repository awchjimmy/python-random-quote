import random

def primary():
    

    f = open("quotes.txt","r",encoding="utf-8")
    quotes = f.readlines()
    f.close()

    last = 13
    rnd = random.randint(0, last)
    print(quotes[rnd])

if __name__== "__main__":
    primary()
