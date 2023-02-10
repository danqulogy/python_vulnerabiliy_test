import subprocess

input = b'A'

while True:
    p = subprocess.Popen("./globomantics.out", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.stdin.write(input)
    output = p.communicate()
    print(str(output))

    if str(output).find("None") != -1 and len(str(output)) == 11 :
        print("segmentation fault")
        print(len(str(input)))
        break
    else:
        input += b"A"