with open("F:\\DSA_HARRY\\File IO\\sample.txt", "r") as f:
    for line in f:
        print(line.strip())

with open("F:\\DSA_HARRY\\File IO\\sample.txt", "a") as b:
    b.write("Hello\n") 

# with open("F:\\DSA_HARRY\\File IO\\sample.txt", "w") as c:
#     b.write("Hello\n")