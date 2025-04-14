stri = input("Enter your string: ")
#print(stri)
stri = stri[:0] + '#' + stri[:]
#print(stri)
stri = stri.title()
#print(stri)
string = stri.split()
#print(string)
string = "".join(string)
if len(string) > 140:
    string = string[:140]
print(string)