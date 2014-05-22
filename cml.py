import sys
import time
import argparse

def get_data(skip):
     """
     """
     with open("20140521_clean.txt", "r") as f:
          next(f) # skip the header
          for i in range(skip - 1):
               next(f) # skip line number
          print("Will read file from line %d" % skip)
          for line in f:
               yield line

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", type=int,
                    help="line number you want to start with.")
args = parser.parse_args()

print("Please enter your name:")
name = sys.stdin.readline().replace("\n", "")
filename = name + ".txt"
print("The result will be saved in " + filename + \
           " and\nthe previous content in the file won't be overwritten.\n")
time.sleep(3)


               
f = get_data(args.number)
while True:
     line = f.next()
     for elem in line.split("\" "):
          for kv in elem.replace("\"", "").split(","):
               print(kv)
          print("--------")
     print("""Are they from the same device?
(Type ONLY the number and then press ENTER.)
1: Yes
2: No
3: Not Sure""")
     result = sys.stdin.readline().replace("\n", "")
     if result in ["1", "2", "3"]:
          target = open(filename, "a")
          target.write(line.replace("\n", "") + " " + result + "\n")
          target.close()
          print("Record saved as " + result + " in " + filename + ".\n\n\n")
          time.sleep(1)
     else:
          print("Invalid format. This one will be skipped.\n\n\n")
          time.sleep(1.8)
          print("Now the NEXT ONE:\n")
