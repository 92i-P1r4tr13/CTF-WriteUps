with open("out.txt", 'rb') as f:
    data = f.read()
    n = 8
    data = data[::2]
    out = [data[i:i+n].decode() for i in range(0, len(data), n)]
    disp = " ".join(out)
    print(disp, end="")
