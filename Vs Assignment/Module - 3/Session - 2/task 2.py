def read_next_line(filename):
    file = open(filename, "rb")

    file.seek(20)
    line = file.readline()

    print(line.decode("utf-8").strip())

    file.close()


read_next_line("lyrics.txt")