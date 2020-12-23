from webbrowser import open
print("")
print("Youtube (1) Twitter (2)")
print("")
program = input("Please Enter What you want to search : ")
print("-" * 60)
if program =="1" :
    search = input("Please Enter What you want to search : ")
    open('https://www.youtube.com/results?search_query=' + search)
elif program =="2" :
    search = input("Please Enter What you want to search : ")
    open('https://twitter.com/search?q=' + search)
else:
    exit("Error... Please Enter [1] or [2]")