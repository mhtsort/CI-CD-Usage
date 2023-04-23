from datetime import date as date
from datetime import datetime
today: date = date.today()
time: datetime = datetime.now()
print(f'{today} {time.strftime("%H:%M")}  :: Successfully run main')
print("Greek characters and Ελληνικοί Χαρακτήρες μφχθζλξ")
cat_ascii = '''
      /\\_/\\  
     / o o \\ 
    (   "   ) 
     \\~---~/
'''
print(cat_ascii)
with open("README.md","rb") as file:
    data = file.read(-1)
    print(type(int(data)))
    print(data[2:].decode(encoding="utf-8"))
    print(bin(data))
    # Print the binary representation of data
    binary_data = ''.join(format(byte, '08b') for byte in data)
    print(binary_data)