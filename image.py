#!/usr/bin env Python 3.8.X
import requests
import sys
import os
from bs4 import BeautifulSoup
os.system('clear')
logo = ('''
    +-+-+-+-+-+-+-+-+-+-+
    | Image Downloader  |
    +-+-+-+-+-+-+-+-+-+-+

''')

# pengguna dapat memasukkan kata kunci pencarian dan jumlah gambar yang di butuhkan
# unduh gambar dari gambar pencarian google ya
Google_Image = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

# Header permintaan User-Agent berisi string karakteristik
# yang memungkinkan rekan protokol jaringan untuk mengidentifikasi jenis aplikasi,
# sistem operasi, dan versi perangkat lunak dari agen pengguna perangkat lunak yang meminta.
# di butuhkan untuk pencarian google
usr_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',

} #'ini agen pengguna saya' di browser untuk mendapatkan detail agen pengguna browser Anda
Image_Folder = 'Images'

def main():
    if not os.path.exists(Image_Folder):
        os.mkdir(Image_Folder)
    download_images()

def download_images():
    # meminta masukan pengguna
    print (logo)
    print ('[+] Enter your search keywords')
    data = input('=>: ')
    print ('[+] Enter the number of pictures you want')
    num_images = int(input('=>: '))
    print ('')
    print('[+] Download in progress')
    print ('-'*24)
    search_url = Google_Image + 'q=' + data
    # request url, tanpa usr_agent izin ditolak
    response = requests.get(search_url, headers=usr_agent)
    html = response.text
    # temukan semua div di mana class = 'rg_i Q4LuWd'
    b_soup = BeautifulSoup(html, 'html.parser')
    results = b_soup.findAll('img', {'class': 'rg_i Q4LuWd'})
    count = 0
    # ekstrak tautan dari tag div
    imagelinks= []
    for res in results:
        try:
            link = res['data-src']
            imagelinks.append(link)
            count = count + 1
            if (count >= num_images):
                break
            
        except KeyError:
            continue
    print(f'Found {len(imagelinks)} images')
    print ('-'*24)
    for i, imagelink in enumerate(imagelinks):
        # buka tautan gambar dan simpan sebagai file
        response = requests.get(imagelink)
        imagename = Image_Folder + '/' + data + str(i+1) + '.png'
        with open(imagename, 'wb') as file:
            file.write(response.content)
    print('[+] Download Successfully')
    print ('')
    quit()

# Untuk perulangan
def quit():
    cb = input('[?] Want to Download Again (y/t): ')
    if cb[0].upper() == 'T':
        print ('-'*24)
        print ('[+] Created By Edi ID')
        sys.exit()
    else:
        os.system('clear')
        main()
    
if __name__ == '__main__':
    main()