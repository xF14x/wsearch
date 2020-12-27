from webbrowser import open
print("")
print("Youtube (1) Twitter (2) GitHub(3)")
print("")
web = input("Please Enter What you want to search : ")
print("-" * 60)
if web =="1" :
    search = input("Please Enter What you want to search : ")
    open('https://www.youtube.com/results?search_query=' + search)
elif web =="2" :
    search = input("Please Enter What you want to search : ")
    open('https://twitter.com/search?q=' + search)
elif web =="2":
    search = input("Please Enter What you want to search : ")
    open('https://github.com/search?q=' + search)
else:
    exit("Error... Please Enter [1] or [2] or [3]")
