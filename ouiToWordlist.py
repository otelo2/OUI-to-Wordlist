#To convert OUI of Arris routers into a Wordlist to use in hashcat hybrid atacks
fIn = open("ouis.txt", "r")
fOut = open("ouisWordlist.txt", "w")

for line in fIn:
    prettyLine = line[0:7].replace(":","")
    print(prettyLine)
    fOut.write(prettyLine+"\n")