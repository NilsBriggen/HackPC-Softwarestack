def convert(binFile):
    hexFile = [hex(int(line, 2))[2:].zfill(4) for line in binFile]
    return " ".join(hexFile)
