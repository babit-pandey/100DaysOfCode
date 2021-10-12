import pyshorteners

url = input("Enter your url: ")
print("Your url: ", pyshorteners.Shortener().tinyurl.short(url))
