import os

files = os.listdir("F:\DSA_HARRY\Exercise\clutter")
i = 1
for file in files :
    if file.endswith(".png") : 
        print(file)

    os.rename(f"F:\DSA_HARRY\Exercise\clutter\{file}.png" , f"F:\DSA_HARRY\Exercise\clutter\{i}.png")
    i = i+ 1