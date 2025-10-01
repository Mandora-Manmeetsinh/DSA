# ======================================================== #
# OS Module #
# ======================================================== #
# function of OS Module #
# ======================================================== #
# print the current working directory
# print("Current working directory: {0}".format(os.getcwd()))
# create a directory
# os.mkdir("newdir")
# create a directory with parent permission
import os

os.mkdir("data")
os.mkdir("data/processed")
os.mkdir("data/raw")
os.mkdir("data/raw/processed")
os.mkdir("data/raw/processed/processed")

os.chmod("data" , 777)
os.chmod("data/processed" , 100)
os.chmod("data/raw" , 102)
os.chmod("data/raw/processed" , 111)
os.chmod("data/raw/processed/processed" , 564)

