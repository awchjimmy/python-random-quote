def primary():
    f = open("quotes.txt","r",encoding="utf-8")
    quotes = f.readlines()
    f.close()

    print(quotes[13])

if __name__== "__main__":
    primary()
