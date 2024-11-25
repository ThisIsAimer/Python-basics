import webbrowser

site = input("please enter your site: ").replace(" ", "+")

webbrowser.open("https://www.google.com/search?q="+site)