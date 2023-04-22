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