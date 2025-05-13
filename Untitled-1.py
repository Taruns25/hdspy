
f= open("demo.txt","w")
f.write("this is a demofile")
f.write("This file is for testing purposes.")
f.write("Good Luck!")
f= open("demo.txt","r")
print(len(f.read()))
print((f.readline()))