run = True
print("File name: ", end = "")
filename = input()
while run:
    print("> ", end = "")
    command = input().split()
    if len(command) == 0:
        continue
    mode = command[0]
    command.pop(0)
    if mode == "append":
        i = 0
        with open(filename, 'a') as f:
            f.write('\n')
            while i < len(command):
                f.write(command[i])
                if i != len(command) - 1:
                    f.write(" ")
                i += 1
    elif mode == "read":
        cnt = 1
        with open(filename, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                if int(command[0]) <= cnt <= int(command[1]):
                    print(line, end = "")
                cnt += 1
        print()
    elif mode == "count":
        cnt = 0
        with open(filename, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                cnt += 1
            print(cnt)
    elif mode == "exit":
        run = False
