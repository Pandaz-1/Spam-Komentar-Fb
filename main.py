'''
Name: Spam Komentar
Author: Pandas ID
Date: 04-06-2020
Deskription: Codenya open source jadi bisa kalian pelajari,namun saya benar" tidak
rela jika script saya kalian upload ke github kalian tanpa mencantumkan code sumbernya (github saya)

Sepro apapun kalian jika belum bisa menghargai karya orang maka kalian belum ada
apa-apanya di mata sang pencipta.

Semoga bermanfaat....
'''

class Main:

    banner = '''
    [---------------------]
        Spam Komentar FB
    [---------------------]'''

    def __init__(self):
        os.system('clear')
        self.banner = Main.banner
        self.head = 'https://mbasic.facebook.com'
        self.req = requests.Session()
        self.listfile = []
        for li in os.listdir('.'):
            if '.log' in li:
                self.listfile.append(li)
        if len(self.listfile) != 0:
            self.login()
        else:
            print(self.banner)
            print('    -!> Silahkan buat file cookie')
            print('    -!> Cara mengambil cookie FB: https://pandasid.blogspot.com')
            exit()

    def login(self):
        os.system('clear')
        print(self.banner)
        print('    [ "0" untuk Info ]')
        print('    [ Login ]')
        print()
        for li in self.listfile:
            print(f'    [{self.listfile.index(li)+1}] {li}')
        try:
            select = int(input('    -•> '))
        except ValueError:
            exit('    -!> Masukan angka')
        if select == 0:
            self.info()
        else:
            try:
                read = open(self.listfile[select-1], 'r').read()
            except IndexError:
                exit('    -!> Pilihan tidak tersedia')
        head = headerz().parser(read)
        cook = headerz().cookie_builder(head['cookie'])
        self.cookie = {'Cookie':cook}
        test = self.req.get(self.head+'/me', cookies=self.cookie)
        if 'Buat Akun Baru' in test.text:
            print('    -!> Invalid Cookie')
            os.system('rm -rf '+self.listfile[int(select)-1])
            exit()
        else:
            self.username = re.search(r'\<title\>(.*?)\<\/title\>', test.text).group(1)
            self.menu()

# MENU
    def menu(self):
        os.system('clear')
        print(self.banner)
        print(f'    [ {self.username} ]')
        print()
        print('    [1] Spam komentar di Beranda')
        print('    [2] Spam komentar di Beranda Teman')
        print('    [3] Spam komentar di satu Postingan')
        print('    [4] Spam komentar di Group')
        print('    [5] Spam komentar di Fanspage')
        print('    [6] Info')
        print('    [0] Keluar')
        print()
        self.selectMenu()

# PILIHAN MENU
    def selectMenu(self):
        selected = input('    -•> ')
        if selected == '1':
            self.homepage()
        elif selected == '2':
            self.friendHomepage()
        elif selected == '3':
            self.singleSpam()
        elif selected == '4':
            self.grupHomepage()
        elif selected == '5':
            self.fansPage()
        elif selected == '6':
            self.info()
        elif selected == '0':
            exit('    -!> Keluar')
        else:
            print('    -!> Pilihan tidak tersedia')
            time.sleep(1)
            self.menu()

    def homepage(self):
        comment = input('    -•> Komentar: ')
        print('    -!> CTRL + C untuk berhenti')
        print()
        count = 1
        while True:
            self.getLink(self.head)
            for s in self.list_of_link:
                try:
                    self.sendComment(self.head+s,comment)
                    print('\r    --> Terkirim ke: '+str(count)+' postingan', end="", flush=True)
                    count += 1
                except AttributeError:
                    pass
            del self.list_of_link[0:]

    def friendHomepage(self):
        inpidf = input('    -•> ID Teman: ')
        profil = self.req.get(self.head+'/'+inpidf, cookies=self.cookie)
        if 'Konten Tidak Ditemukan' in profil.text:
            print()
            exit('    -!> ID Teman tidak ditemukan')
        elif 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in profil.text:
            print()
            exit('    -!> Melanggar komonitas')
        else:
            comment = input('    -•> Komentar: ')
            print('    -!> CTRL + C untuk berhenti')
            print()
            count = 1
            while True:
                self.getLink(profil.url)
                for s in self.list_of_link:
                    try:
                        self.sendComment(self.head+s, comment)
                        print('\r    --> Terkirim ke: '+str(count)+' postingan', end="", flush=True)
                        count += 1
                    except AttributeError:
                        pass
                del self.list_of_link[0:]

    def singleSpam(self):
        inplink = input('    -•> Link: ').replace('www', 'mbasic')
        comment = input('    -•> Komentar: ')
        try:
            inpjmlh = int(input('    -•> Jumlah: '))
        except ValueError:
            exit('    -!> Masukan angka')
        print('    -!> CTRL + C untuk berhenti')
        print()
        count = 1
        t = 0
        for s in range(inpjmlh):
            self.sendComment(inplink, comment)
            if 'Gabung ke Grup' in self.gettarget:
                exit('    -!> Anda belum bergabung ke grup')
            print('\r    --> Komentar terkirim: '+str(count), end="", flush=True)
            count += 1
            t += 1
            if t == 5:
                time.sleep(5)
                t == 0
                print('    --> Delay 5 detik')
        exit('    -•> Selesai')

    def grupHomepage(self):
        inpidg = input('    -•> ID Group: ')
        groups = self.req.get(self.head+'/'+inpidg, cookies=self.cookie)
        if 'Konten Tidak Ditemukan' in groups.text:
            print()
            exit('    -!> ID Grup tidak  ditemukan')
        elif 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in groups.text:
            print()
            exit('    -!> Melanggar komonitas')
        else:
            comment = input('    -•> Komentar: ')
            print('    -!> CTRL + C untuk berhenti')
            print()
            count = 1
            while True:
                self.getLink(groups.url)
                for s in self.list_of_link:
                    try:
                        self.sendComment(self.head+s, comment)
                        print('\r    --> Terkirim ke: '+str(count)+' postingan', end="", flush=True)
                        count += 1
                    except AttributeError:
                        pass
                del self.list_of_link[0:]

    def fansPage(self):
        inpidfp = input('    -•> ID Fanspage: ')
        fanspage = self.req.get(self.head+'/'+inpidfp, cookies=self.cookie)
        if 'Konten Tidak Ditemukan' in fanspage.text:
            print()
            exit('    -!> ID Fanspage tidak ditemukan')
        elif 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in profil.text:
            print()
            exit('    -!> Melanggar komonitas')
        else:
            comment = input('    -•> Komentar: ')
            print('    -!> CTRL + C untuk berhenti')
            print()
            count = 1
            while True:
                self.getLink(fanspage.url)
                for s in self.list_of_link:
                    try:
                        self.sendComment(self.head+s, comment)
                        print('\r    --> Terkirim ke: '+str(count)+' postingan', end="", flush=True)
                        count += 1
                    except AttributeError:
                        pass
                del self.list_of_link[0:]

### BOT
# MENGAMBIL LINK TARGET
    def getLink(self, pages):
        self.list_of_link = []
        page = self.req.get(pages, cookies=self.cookie).text
        soup = BeautifulSoup(page, 'html.parser')
        link = soup.find_all('a')
        for l in link:
            if 'Komentar' in str(l):
                href = re.search(r'href="(.*?)"', str(l)).group(1)
                self.list_of_link.append(html.unescape(href))

# MENGIRM KOMENTAR
    def sendComment(self, target, text):
        data = {
            'comment_text':text,
            'submit':'Komentari'
        }
        self.gettarget = self.req.get(target, cookies=self.cookie).text
        soup = BeautifulSoup(self.gettarget, 'html.parser')
        list_input = soup.find_all('input', {'type':'hidden'})
        for i in list_input:
            try:
                data[i['name']] = i['value']
            except KeyError:
                data[i['name']] = ""
        urlpost = html.unescape(re.search(r'\<form\ method\=\"post\"\ action\=\"(.*?)\"\>', self.gettarget).group(1))
        send = self.req.post(self.head+urlpost, data=data, cookies=self.cookie)

#INFO
    def info(self):
        print('            [ INFO ]')
        print('    [---------------------]')
        print('      AUTHOR: Pandas ID')
        print('      FB    : Pandas ID')
        print('      WA    : 082250223147')
        print('      BLOG  : https://pandasid.blogspot.com')
        print('    [---------------------]')
        input('    [ Keluar ]')
        exit()

#IMPORT MODUL
from headerz import headerz
from bs4 import BeautifulSoup
import requests
import time
import html
import os
import re

if __name__ == '__main__':
    try:
        Main()
    except KeyboardInterrupt:
        exit('    -!> Keluar')
    except requests.ConnectionError:
        exit('    -!> Koneksi Error')
