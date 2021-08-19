def read(file):
    try:
        f = open(file, "r")
        r=f.read()
        f.close()
        return r
    except:
        return ""
def write(file,txt):
    f = open(file, "w+")
    f.write(txt)
    f.close()
def append(file,txt):
    write(file,read(file)+txt)
print(read("ciao"))
append("file","ciao")
print(read("file"))
