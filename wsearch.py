from webbrowser import open
print("")
print("""
Programmit By Suliman | Twitter : F14Commander
Youtube (1) Twitter (2) GitHub(3)

Programmit By Sultan | Twitter | sultaan17_
Google translate(4) Shodan(5)

""")
print("")
# By Suliman
web = input("Please Enter What you want to search : ")
print("-" * 60)
if web =="1" :
    search = input("Please Enter What you want to search : ")
    open('https://www.youtube.com/results?search_query=' + search)
elif web =="2" :
    search = input("Please Enter What you want to search : ")
    open('https://twitter.com/search?q=' + search)
elif web =="3":
    search = input("Please Enter What you want to search : ")
    open('https://github.com/search?q=' + search)
    # By Sultan
elif web == "4":
    search = input("Please Enter What you want to search : ")
    open('https://translate.google.com/?sl=en&tl=ar&text='+ search +'&op=translate')
elif web == "5":
    search = input("Please Enter What you want to search : ")
    open("https://www.shodan.io/search?query="+ search )
else:
    exit("Error... Please Enter [1] or [2] or [3] or [4] or [5]")
