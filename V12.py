import sys,os,re,socket,binascii,time,json,random,threading,Queue,pprint,urlparse,smtplib,telnetlib,os.path,hashlib,string,urllib2,glob,sqlite3,urllib,argparse,marshal,base64,requests
from colorama import *
from random import choice
from colorama import Fore,Back,init
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import system
from Queue import Queue
from time import strftime
from urlparse import urlparse
from urllib2 import urlopen
init()

la7mar  = '\033[91m'
lazra9  = '\033[94m'
la5dhar = '\033[92m'
movv    = '\033[95m'
lasfar  = '\033[93m'
ramadi  = '\033[90m'
blid    = '\033[1m'
star    = '\033[4m'
bigas   = '\033[07m'
bigbbs  = '\033[27m'
hell    = '\033[05m'
saker   = '\033[25m'
labyadh = '\033[00m'
cyan    = '\033[0;96m'

def logo():
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37  ]

        x = """ 

  ______               _     _   ____        _    __      ____ ___  
 |___  /              | |   (_) |  _ \      | |   \ \    / /_ |__ \ 
    / / ___  _ __ ___ | |__  _  | |_) | ___ | |_   \ \  / / | |  ) |
   / / / _ \| '_ ` _ \| '_ \| | |  _ < / _ \| __|   \ \/ /  | | / / 
  / /_| (_) | | | | | | |_) | | | |_) | (_) | |_     \  /   | |/ /_ 
 /_____\___/|_| |_| |_|_.__/|_| |____/ \___/ \__|     \/    |_|____|                                                                      
 Zombi Bot V12    |   Ultra Priv8 Bot    | |  Code by Viper1337                           
                                             
                      
 [+] ICQ: 744289868


 [+] 1. Run Bot Zombi Bot v12 [ New ]
 [+] 2. Checker Shell [ Live or Dead ]
 [+] 3. Scanner & Exploiter [ Joomla, Wordpress, Magento,Drupal ]
 [+] 4. BruteForce OpenCart & Auto Upload Shell [ Fixed ]
 [+] 5. Checker Valid Amazon [ MultiThread Fast ]
 [+] 6. Checker Valid Apple [ MultiThread Fast ]
 [+] 7. Auto Exploit Magento [ Multy Exploit ]
 [+] 8. CMS Filter
 [+] 9. Brute Force [ Wordpress, Joomla, OpenCart, Drupal ]
 [+] 10. Mass Domain To Ip
 [+] 11. Viper 1337 SMTP Cracker v1
 [+] 12. zone-h Grabber
 [+] 13. Reverse Ip Priv8 Unlimted
 [+] 14. Mass Mailst From Config
 [+] 15. Smtp Tester [ Work Or Not ]
 [+] 16. MassGrabber [ Mass Admin Panel Finder ]
 [+] 17. Cpanel Cracker [ Wordpress, Joomla, OpenCart, Drupal ]
 [+] 18. 0day Private Bot  [ Wordpress, Joomla, OpenCart, Drupal ]
 [+] 19. PrestaShop Mass Shell upload
 [+] 20. Check For Latest Update
 
			                  """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)


logo()


choice=raw_input(' [+] Enter Number : ')
if choice=='1':
  t=raw_input(' [+] Open File IzanamiBot And Save ==> list.txt [y/n] : ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd File/IzanamiBot && chmod +x run.pyc list.txt && python run.pyc list.txt")
   if system() == 'Windows':
    os.system('cd File/IzanamiBot && run.pyc list.txt')
   else:
    print('ERROR GOBLOK !')
  elif t=='n':
   main()
  else :
   print('ERROR GOBLOK !')
if choice=='2':
  t=raw_input(' [+] Open File Checker And Save ==> list.txt [y/n] : ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd File\Checker && chmod +x checker.py list.txt && python checker.py list.txt")
   if system() == 'Windows':
    os.system('cd File\Checker && checker.py list.txt')
   else:
    print('ERROR GOBLOK !')
  elif t=='n':
   main()
  else :
   print('ERROR GOBLOK !')
if choice=='3':
  t=raw_input(' [+] Open File Scanner And Save your list in folder TargetList [y/n] : ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd File\Scanner && chmod +x run.bat && run.bat")
   if system() == 'Windows':
    os.system('cd File\Scanner && run.bat')
   else:
    print('ERROR GOBLOK !')
  elif t=='n':
   main()
  else :
   print('ERROR GOBLOK !')
if choice=='4':
  t=raw_input(' [+] Open File OPC And Save ==> list.txt [y/n] : ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd File\OPC && chmod +x run.py list.txt && run.py list.txt")
   if system() == 'Windows':
    os.system('cd File\OPC && run.py list.txt')
   else:
    print('ERROR GOBLOK !')
  elif t=='n':
   main()
  else :
   print('ERROR GOBLOK !')
if choice=='5':
  t=raw_input(' [+] Open File AmzVal And Save ==> list.txt [y/n] : ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd File\AmzVal && chmod +x run.bat && run.bat")
   if system() == 'Windows':
    os.system('cd File\AmzVal && run.bat')
   else:
    print('ERROR GOBLOK !')
  elif t=='n':
   main()
  else :
   print('ERROR GOBLOK !')
if choice=='6':
  t=raw_input(' [+] Open File AppVal And Save ==> list.txt , Note : Use python3 check README.MD')
if choice=='7':
  t=raw_input(' [+] Open File Magento And Save ==> list.txt [y/n] : ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd File\Magento && chmod +x run.bat list.txt && list.txt")
   if system() == 'Windows':
    os.system('cd File\Magento && run.bat list.txt')
   else:
    print('ERROR GOBLOK !')
  elif t=='n':
   main()
  else :
   print('ERROR GOBLOK !')
if choice=='8':
  t=raw_input(' [+] Open File CMS And Save ==> list.txt [y/n] : ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd File\CMS && chmod +x cms.py && python cms.py")
   if system() == 'Windows':
    os.system('cd File\CMS && cms.py')
   else:
    print('ERROR GOBLOK !')
  elif t=='n':
   main()
  else :
   print('ERROR GOBLOK !')
if choice=='9':
  t=raw_input(' [+] Open File BruteForce And Save ==> list.txt [y/n] : ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd File\BruteForce && chmod +x bf.py && python bf.py")
   if system() == 'Windows':
    os.system('cd File\BruteForce && bf.py')
   else:
    print('ERROR GOBLOK !')
  elif t=='n':
   main()
  else :
   print('ERROR GOBLOK !')
if choice=='10':
  t=raw_input(' [+] Open File domain And Save ==> ips.txt [y/n] : ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd File\domain && chmod +x ipfromdomain.py && python ipfromdomain.py")
   if system() == 'Windows':
    os.system('cd File\domain && ipfromdomain.py')
   else:
    print('ERROR GOBLOK !')
  elif t=='n':
   main()
  else :
   print('ERROR GOBLOK !') 
if choice=='11':
  t=raw_input(' [+] Open File Smtp And Save ==> results.txt [y/n] : ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd File\Smtp && chmod +x priv8.py && python priv8.py")
   if system() == 'Windows':
    os.system('cd File\Smtp && priv8.py')
   else:
    print('ERROR GOBLOK !')
  elif t=='n':
   main()
  else :
   print('ERROR GOBLOK !') 
if choice=='12':
  t=raw_input(' [+] Open File Zone-h And Save ==> hunted_urls.txt [y/n] : ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd File\Zone-h && chmod +x zone.py && python zone.py")
   if system() == 'Windows':
    os.system('cd File\Zone-h && zone.py')
   else:
    print('ERROR GOBLOK !')
  elif t=='n':
   main()
  else :
   print('ERROR GOBLOK !')    
if choice=='13':
  t=raw_input(' [+] Open File ReverseIp And Save ==> Grabbed.txt [y/n] : ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd File\ReverseIp && chmod +x api.py && python api.py")
   if system() == 'Windows':
    os.system('cd File\ReverseIp && api.py')
   else:
    print('ERROR GOBLOK !')
  elif t=='n':
   main()
  else :
   print('ERROR GOBLOK !')   
if choice=='13':
  t=raw_input(' [+] Open File ReverseIp And Save ==> Grabbed.txt [y/n] : ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd File\ReverseIp && chmod +x api.py && python api.py")
   if system() == 'Windows':
    os.system('cd File\ReverseIp && api.py')
   else:
    print('ERROR GOBLOK !')
  elif t=='n':
   main()
  else :
   print('ERROR GOBLOK !') 
if choice=='14':
  t=raw_input(' [+] Open File Mailist And Save ==> Results.txt [y/n] : ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd File\Maillist && chmod +x maillist.py && python maillist.py")
   if system() == 'Windows':
    os.system('cd File\Maillist && Maillist.py')
   else:
    print('ERROR GOBLOK !')
  elif t=='n':
   main()
  else :
   print('ERROR GOBLOK !')
if choice=='15':
  t=raw_input(' [+] Open File SmtpTester And Save ==> Results.txt [y/n] : ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd File\SmtpTester && chmod +x smtp.py && python smtp.py")
   if system() == 'Windows':
    os.system('cd File\SmtpTester && smtp.py')
   else:
    print('ERROR GOBLOK !')
  elif t=='n':
   main()
  else :
   print('ERROR GOBLOK !')
if choice=='16':
  t=raw_input(' [+] Open File MassGrabber And Save ==> shariq.txt [y/n] : ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd File\MassGrabber && chmod +x massgrab.py && python massgrab.py")
   if system() == 'Windows':
    os.system('cd File\MassGrabber && massgrab.py')
   else:
    print('ERROR GOBLOK !')
  elif t=='n':
   main()
  else :
   print('ERROR GOBLOK !')  
if choice=='17':
  t=raw_input(' [+] Open File cpanel And Save ==> vuln_cpanel.txt [y/n] : ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd File\cpanel && chmod +x bruter.py 50 domins.txt password.txt && python bruter.py 50 domins.txt password.txt")
   if system() == 'Windows':
    os.system('cd File\cpanel && bruter.py 50 domins.txt password.txt')
   else:
    print('ERROR GOBLOK !')
  elif t=='n':
   main()
  else :
   print('ERROR GOBLOK !')
if choice=='18':
  t=raw_input(' [+] Open File 0day And Save ==> 3.txt [y/n] : ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd File\0day && chmod +x 2.py && python 2.py")
   if system() == 'Windows':
    os.system('cd File\0day && 2.py')
   else:
    print('ERROR GOBLOK !')
  elif t=='n':
   main()
  else :
   print('ERROR GOBLOK !') 
if choice=='19':
  t=raw_input(' [+] Open File Prestashop And Save ==> Shells.txt [y/n] : ')
  if t=='y':
   if system() == 'Linux':
    os.system("cd File\Prestashop && chmod +x presta.py && python presta.py")
   if system() == 'Windows':
    os.system('cd File\Prestashop && presta.py')
   else:
    print('ERROR GOBLOK !')
  elif t=='n':
   main()
  else :
   print('ERROR GOBLOK !')
if choice=='20':
  t=raw_input(' [+] DONT HAVE UPDATE, CONTACT OWNER ! ')