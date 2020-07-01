#!/usr/bin/env python
# Author: Jesse Morgan (morgajel)
# Created to emulate code by Justin Faler
# Mutified by Cfomodz - Note on this: I adapted this code to my own personal needs.
  """ This wont be for everyone, but it does open up the possibilities for diferent implementations of Soup.
  Further note: I am still a student of Python and computer programming. I know I have made errors and
  done things in a non-pythonic way through either making this more difficult than they need to be,
  using style that would not be considered best practice, etc. PLEASE make pull requests with any fixes that
  you see need to be made, small or large, or open an issue, and I can do some Googling and figure out how to
  solve the problem that I created.
  Items that likely need fixed: My implementation of a 'send during the day' time based controller.
  Sub item to that, making those user input instead of hard coded.. maybe?
  Maybe a mode select (menu) instead of always just asking if they want to input times to make calls, then
  go on to ask if they want to skip saved (hard coded) numbers, then if they say no, asking if they want to
  call each one individually, etc.
  """

import time
import datetime as dt
# NOTE: This requires python 3 and the twilio library to be installed (pip install twilio)
from twilio.rest import Client

accountSid = "A***************************"
authtoken = "*****************************"
voiceml= "http://demo.twilio.com/docs/voice.xml"

# Replace these with phone numbers on your Twilio account - either verified or purchased from Twilio.            
sourceNumbers = ["+18005552525", "+18665555252", "+18445552525"]

def callThem(toNumber, fromNumber):
	try:
		call = client.calls.create(
			to = toNumber,
			from_ = fromNumber,
			url = voiceml,
			machine_detection = "DetectMessageEnd",
			machine_detection_timeout = "21",
			record = "true",
			trim = "do-not-trim",
			method = "GET",
			)
		print("Started call to %s from %s" % (toNumber, fromNumber));
	except Exception as err:
		print("Error on  %s from %s: %s" % (toNumber, fromNumber, err));

print (originally based on: )
print(r""" 

 /$$                   /$$    
| $$                  | $$    
| $$$$$$$   /$$$$$$  /$$$$$$  
| $$__  $$ /$$__  $$|_  $$_/  
| $$  \ $$| $$  \ $$  | $$    
| $$  | $$| $$  | $$  | $$ /$$
| $$  | $$|  $$$$$$/  |  $$$$/
|__/  |__/ \______/    \___/  
                              
   _____ ____  __  ______ 
  / ___// __ \/ / / / __ \
  \__ \/ / / / / / / /_/ /
 ___/ / /_/ / /_/ / ____/ 
/____/\____/\____/_/      
					  
			""")

numsToCall = []

#decide if we are using saved phone numbers or numbers from user input
skip_all = raw_input("Would you like to skip all saved phone numbers \
  and jump to inputing your own number(s) manually? (Y/N): ")
skip_all = skip_all.lower()
if skip_all == y or skip_all == yes:
	skip_all = True
else skip_all = False

if not skip_all:
  call_all = raw_input("Would you like to call all saved phone numbers?: (Y/N): ")
  call_all = call_all.lower()
  if call_all == "y" or call_all == "yes": #add all saved numbers to our list of nums
    numsToCall.append(num1)
    numsToCall.append(num2)
    numsToCall.append(num3)
    numsToCall.append(num4)
    numsToCall.append(num5)
    numsToCall.append(num6)
  else: #use hard coded numbers
    
    """This script can easily be modified (check for second version)
    in a way that will only support hard coded phone numbers and other configerable
    values, and thus will not have any user-input, allowing you to bash script it,
    set it up with a cron job, etc.
    """

    #start phone number 1
    #notes on phone number
    num1 = "+14748589696"
    num1_title = "This can be the name of the person"
    add_1 = raw_input("You would like to call " + num1_title + "? (Y/N): ")
    add_1 = add_1.lower()
    if add_1 == "y" or add_1 == "yes":
      numsToCall.append(num1)
      print(num1 + " has been added to the list")
    #------------------------------------#

    #start phone number 2
    #notes on phone number
    num2 = "+15462127878"
    num2_title = "Or the name of the business"
    add_2 = raw_input("You would like to call " + num2_title + "? (Y/N): ")
    add_2 = add_2.lower()
    if add_2 == "y" or add_ == "yes":
      numsToCall.append(num2)
      print(num2 + " has been added to the list")
    #------------------------------------#

    #start phone number 3
    #notes on phone number
    num3 = ""
    num3_title = ""
    add_3 = raw_input("You would like to call " + num3_title + "? (Y/N): ")
    add_3 = add_3.lower()
    if add_3 == "y" or add_3 == "yes":
      numsToCall.append(num3)
      print(num3 + " has been added to the list")
    #------------------------------------#


    #start phone number 4
    #notes on phone number
    num4 = ""
    num4_title = ""
    add_4 = raw_input("You would like to call " + num4_title + "? (Y/N): ")
    add_4 = add_4.lower()
    if add_4 == "y" or add_4 == "yes":
      numsToCall.append(num4)
      print(num4 + " has been added to the list")
    #------------------------------------#

    #start phone number 5
    #notes on phone number
    num5 = ""
    num5_title = ""
    add_5 = raw_input("You would like to call " + num5_title + "? (Y/N): ")
    add_5 = add_5.lower()
    if add_5 == "y" or add_5 == "yes":
      numsToCall.append(num5)
      print(num5 + " has been added to the list")
    #------------------------------------#

    #start phone number 6
    #notes on phone number
    num6 = ""
    num6_title = ""
    add_6 = raw_input("You would like to call " + num6_title + "? (Y/N): ")
    add_6 = add_6.lower()
    if add_6 == "y" or add_6 == "yes":
      numsToCall.append(num6)
      print(num6 + " has been added to the list")
    #------------------------------------#

#user input of callees if no saved numbers are selected to call
if not numsToCall:
	numOfNumsToAdd = raw_input("How many numbers would you like to call?(Integer only): ")
	for i in range(numOfNumsToAdd):
		new_num = input("Enter the number you would like to call (+1 MUST BE IN FRONT!): ")
		numsToCall.append(new_num)

#allowing user to enter desired sleep times
#after each call
after_call_delay = int(raw_input("How many minutes would you like to wait after each call? (Press Enter for default of : "))
after_call_delay *= 60

#after each round - one caller number making each call to list of callees
after_round_delay = int(raw_input("How many minutes would you like to wait after each round of calls \
  (each number having been called once by a single target number)?: "))
after_round_delay *= 60

"""after each series - all caller numbers making each call to list of callees
if you just want each caller number to call each callee number and then finish,
simply break the loop on line 213 by setting run = False instead of sleeping for
the after_series_delay, then breaking out of the True loop on line 232.
"""
after_series_delay = int(raw_input("How many minutes would you like to wait after each series of calls \
  (each number having been called once by every source number - All possible combinations of callers and \
  callees, essentially the reset timer if you want to keep calling the same people from the same numbers, \
  I often use 24 hours (1440) so that each person is getting a call from each source number once every 24 \
  hours-ish (not including other delay timers))?: "))
after_series_delay *= 60

#Starting the call automation
client = Client(accountSid, authtoken)

#makes calls after start time and before stop time. Does not make calls between pause time and start time, or after stop time
now = dt.datetime.now()
print(now)
pause = dt.datetime(now.year, now.month, now.day, 0)
start = dt.datetime(now.year, now.month, now.day, 7)
stop = dt.datetime(now.year, now.month, now.day, 17)

#initiation is by default disabled, and is only enabled if the time of day is within acceptable limits
run = False
count = 0;
while True: #begin main loop
	if now >= pause and now < start: #check if time is acceptable
		run = False
		print("Before start")
		time.sleep(1800)
	elif now >= stop:
		run = False
		print("After stop")
		time.sleep(1800)
	else: #if there is no objection, start calling
		run = True
  while run == True: #calling loop, controlled by run == True
		for sourceNumber in sourceNumbers: #for each caller number that you have, begin using that number for a round of calls
			count += 1
			print("Starting call batch %s with number: " + sourceNumber + " [ %s calls to make.]" % (count, len(numsToCall) ))

			for numToCall in numsToCall: #for each callee number that you have selected or entered, call it with the current source number for this round
				callThem(numToCall, sourceNumber)
        time.sleep(after_call_delay) #wait after a call (any call)
      time.sleep(after_round_delay) #wait after a round of calls (one caller number exhasted (having called each callee number once))
		time.sleep(after_series_delay) #wait after a series of calls (all caller numbers eshasted (having each called each callee number once))
		
    #redetermining if it is a good time of day to be making calls before beginning a new series
    """Please remember that this redetermination is only made at the end of each series. Depending on your delays, number of callers,
    and number of callees, a serious could take hours to complete, and a series started a minute before the stop time would in that
    case continue for hours past the time you likely wished to stop calling. This can easily be accomodated by multiplying your
    after_call_delay by the number of calls in a series [len(sourceNumbers) * len(numsToCall)] and then adding that product to the
    total delay from after_round_delay 's, which is simply the after_round_delay * len(sourceNumbers), then subtract that sum of time
    from when you would like to stop making phone calls, and make that your stop value, thus, a series will not begin after that time,
    and will thus complete before the real cutoff time that you used to calculate your stop value.
    """
		now = dt.datetime.now()
		print(now)
		if now >= pause and now < start:
			run = False
		elif now >= stop:
			run = False
		else:
			run = True
