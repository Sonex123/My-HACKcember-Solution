with open("rockyou.txt", "rb") as f:
    for i in f.read().splitlines():
        if len(i) == 96:
            print(i)

# Then just try the Printet passwords (off course without the binary-marks)