new_file = open("document.bin", mode="wb")
st = "This is good"
decoded = [str(ord(c)) for c in st]
string = "".join(decoded)
new_file.write(string.encode())
new_file.close()
