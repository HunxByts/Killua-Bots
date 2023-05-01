#!/usr/bin/python
# << CODE BY HUNX04
# << MAU RECODE ??? IZIN DULU LAH , MINIMAL TAG AKUN GITHUB MIMIN YANG MENGARAH KE AKUN INI, LEBIH ENAKNYA SIH FORK 
# << KALAU DI ATAS TIDAK DI IKUTI MAKA AKAN MENDAPATKAN DOSA KARENA MIMIN GAK IKHLAS DUNIA AKHIRAT SAMPAI 7 TURUNAN
# “Wahai orang-orang yang beriman! Janganlah kamu saling memakan harta sesamamu dengan jalan yang batil,” (QS. An Nisaa': 29). Rasulullah SAW juga melarang umatnya untuk mengambil hak orang lain tanpa izin.

import os
from sys import stderr
import time
import socket
import requests
import datetime
import random
import platform
import subprocess

Bl='\033[30m' # VARIABLE COLOR 
Re='\033[1;31m'
Gr='\033[1;32m'
Ye='\033[1;33m'
Blu='\033[1;34m'
Mage='\033[1;35m'
Cy='\033[1;36m'
Wh='\033[1;37m'

os.system('clear')
stderr.writelines(f"""{Wh}
╭╮╭━╮╭╮╭╮╱╱╱╱╱╱╱╱╱╭━━╮╱╱╱╭╮
┃┃┃╭╯┃┃┃┃╱╱╱╱╱╱╱╱╱┃╭╮┃╱╱╭╯╰╮
┃╰╯╯╭┫┃┃┃╭╮╭┳━━╮╱╱┃╰╯╰┳━┻╮╭╋━━╮
┃╭╮┃┣┫┃┃┃┃┃┃┃╭╮┣━━┫╭━╮┃╭╮┃┃┃━━┫   {Cy}[  {Wh}KILLUA   BOTS  {Cy}]
┃┃┃╰┫┃╰┫╰┫╰╯┃╭╮┣━━┫╰━╯┃╰╯┃╰╋━━┃  {Wh}CODE BY HUNXBYTS V1.1{Cy}
╰╯╰━┻┻━┻━┻━━┻╯╰╯╱╱╰━━━┻━━┻━┻━━╯
{Wh}<<=============================================================>>\n
""")
def menu():
  print(f"""
          {Cy}.:: {Wh}MENU KILLUA-BOTS {Cy}::.

  {Wh}[{Cy}1{Wh}] !Cek IP Private          {Wh}[{Cy}11{Wh}]  !Cek System
  {Wh}[{Cy}2{Wh}] !Cek IP Public           {Wh}[{Cy}12{Wh}]  !Ping
  {Wh}[{Cy}3{Wh}] !Cek Hari                {Wh}[{Cy}13{Wh}]  !Convert Yt ke Mp3 [ERROR]
  {Wh}[{Cy}4{Wh}] !Cek Jam                 {Wh}[{Cy}14{Wh}]  !Dowload Vidio Yt [ERROR]
  {Wh}[{Cy}5{Wh}] !Cek Author              {Wh}[{Cy}15{Wh}]  !Short-link 
  {Wh}[{Cy}6{Wh}] !Cek Nama Bot            
  {Wh}[{Cy}7{Wh}] !Cek Cewek               
  {Wh}[{Cy}8{Wh}] !Cek Gay                 
  {Wh}[{Cy}9{Wh}] !Cek Lesby            
  {Wh}[{Cy}10{Wh}] !Cek Pintar         
""")

#VARIABLE BOT
My_Bot = "Killua-Bots"
Message = f"Selamat datang di [{Cy}Killua-Bots{Wh}] Silahkan ketik {Wh}[{Cy}menu{Wh}] untuk melihat opsi menu"
pr = "!"

#VARIABLE MENU
user = socket.gethostname()
ipPrv = socket.gethostbyname(user)

respone = requests.get('https://api.ipify.org/')
ipPbl = respone.text

day = datetime.datetime.now().strftime('%A')

if day == 'Monday':
  day = 'Senin'
elif day == 'Tuesday':
  day = 'Selasa'
elif day == 'Wednesday':
  day = 'Rabuh'
elif day == 'Thursday':
  day = 'kamis'
elif day == 'Friday':
  day = 'Jumat'
elif day == 'Saturday':
  day = 'Sabtu'
elif day == 'Sunday':
  day = 'Minggu'

time = datetime.datetime.now().strftime('%H:%M:%S')

cekGay = [f"""
{Wh}0%
{Cy}█▒▒▒▒▒▒▒▒▒
""",f"""
{Wh}10%
{Cy}███▒▒▒▒▒▒▒
""",f"""
{Wh}30% 
{Cy}█████▒▒▒▒▒""",f"""
{Wh}50%
{Cy}███████▒▒▒""",f"""
{Wh}100%
{Cy}██████████"""
]

cek_gay = random.choices(cekGay)
gay = ', '.join(cek_gay)

system_info = platform.uname()

def generate_response(user_input):
  if user_input.lower() in ["hi","oy","woy","bang","kak"]:
    return "Apa yang bisa killua bantu ?"
  elif user_input.lower() == "menu":
    menu()
    return f"{Wh}Kak [{Ye}{user}{Wh}] {Wh}bisa menggunakan menu itu untuk kebutuhan!"
  elif user_input == f'{pr}Cek IP Private':  
    return f"IP Private mu : {Ye}{ipPrv}"
  elif user_input == f'{pr}Cek IP Public':
    return f"IP Public mu : {Ye}{ipPbl}"
  elif user_input == f'{pr}Cek Hari':
    return f"Hari ini : {Ye}{day}"
  elif user_input == f'{pr}Cek Author':
    return f"""\n
    {Wh}Athor ku  : {Ye}Hunx
    {Wh}Github    : {Ye}HunxByts
    {Wh}Instagram : {Ye}faiss.010__
    {Wh}Whatsapp  : {Ye}Null\n"""
  elif user_input == f'{pr}Cek Jam':
    return f"Jam sekarang : {Ye}{time}"
  elif user_input == f'{pr}Cek Nama Bot':
    return f"Nama ku : {Ye}Killua-Bots"
  elif user_input == f'{pr}Cek Gay':
    return f"""
  Skor Gay mu :
    {Ye}{gay}
  """
  elif user_input == f'{pr}Cek Lesby':
    return f"""
  Skor Lesbian mu :
    {Ye}{gay}
  """
  elif user_input == f'{pr}Cek Pintar':
    return f"""
  Skor Pintar mu :
    {Ye}{gay}
  """
  elif user_input == f'{pr}Cek System':
    return f"""
  .:: {Ye}System Info ::.
  System: {system_info.system}
  Node Name: {system_info.node}
  Release: {system_info.release}
  Version: {system_info.version}
  Machine: {system_info.machine}
  Processor: {system_info.processor}
  """
  elif user_input == f'{pr}Ping':
    host = input(f"Masukan Web target : ")
    try:
      ip_address = socket.gethostbyname(host)
      print(f"Ping ke {host}")
      result = subprocess.run(["ping", "-c", "3", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      output = result.stdout.decode()
      print(output)
    except socket.gaierror:
        print(f"URL {host} tidak valid")
  elif user_input == f'{pr}Short-link ':
    def shorten_url(url):
      url = input(f"{Wh}[{Cy}+{Wh}] {Wh}Masukan Url nya : {Cy}")  
      shortened_url = ''
      try:
          response = requests.post('http://tinyurl.com/api-create.php?url=' + url)
          if response.status_code == 200:
              shortened_url = response.text.strip()
      except requests.exceptions.RequestException as e:
          print(e)
      return shortened_url
    short_url = shorten_url(url)
    print(f"{Wh}[{Cy}+{Wh}] Url sudah di pendekin : {Cy}{short_url}")


  elif user_input.lower() in ["apa kabar ?","apa kabar bro ?","apa kabar kak ?","apa kabar bang ?","apa kabar ngab ?","apa kabar"]:
    return f"Aku baik, kalo kamu {user} ?"
  elif user_input.lower() in ["baik","baik juga","baik juga"]:
    return "Oke sippp"
  elif user_input.lower() == "goodbye":
    return "Goodbye!"
  elif user_input.lower() in ["nama kamu siapa","nama kamu siapa ?","kamu siapa","kamu siapa ?"]:
    return "Saya adalah Killua-Bots"
  elif user_input.lower() in ["assalamualaikum", "Asslamualaikum"]:
    return "Waalaikum salam"
  elif user_input.lower() in ["ok","oke","yoi","baik lah"]:
    return "woke"
  elif user_input.lower() in ["p","pp","ppp","pppp"]:
    return "Jangan p pp aja salam deck!!"
  elif user_input.lower() in ["iy","ya","iya","iyaa","yaa"]:
    return "iyaa"
  elif user_input.lower() in ["ohh","ohh iya","ouu","Ooo"]:
    return "Hoo"
  elif user_input.lower() in ["cok","asw","jancok","bangsat","bajngan","ngentod","asu","babi","bacot"]:
    return "Jangan ngomong kasar kak nanti dosa!!"
  elif user_input.lower() in ["maaf","maaf ya","maaf yaa"]:
    return "Iyaa"
  elif user_input.lower() in ["umur mu berapa", "umur mu berapa ?", "berapa umur mu", "berapa umur mu ?", "kamu umur berapa ?","kamu umur berapa","umur kamu berapa","umur kamu berapa ?"]:
    return "Umurku 16 tahun, kalo kamu ?"
  elif user_input.isdigit():
    age = int(user_input)
    if age <= 15:
      return "Ohh masih bocil yaa"
    elif age >= 16 and age <= 19:
      return "Wah kita sama udah remaja hehe"
    else:
      return f"Wah udah abang - abang, kalo boleh tau abang udah kerja ?"
  elif user_input.lower() in ["udh","udah"]:
    return "Oke deh semangat bang"
  elif user_input.lower() in ["blm","belum","belom"]:
    return "Ouuu"
  elif user_input.lower() in ["udah punya pacar","udah punya pacar ?","dh punya pacar ?","udah punya pacar belom","udah punya pacar belom","kamu udah punya pacar ?","kamu udah punya pacar"]:
    return "Belom aku jomblo, boleh gk carikan aku pacar ?"
  elif user_input.lower() in ["blh","boleh","bole","bowlee","boleh kok"]:
    return "Carikan yaa ^_^"
  elif user_input.lower() in ["gk","engga","gak","ga","gak mau"]:
    return "Yaudah"
  elif user_input.lower() in ["makasih","terimakasih"]:
    return "Sama - Sama"
  elif user_input.lower() in ["hm","hmm","hmmm","hmmmm"]:
    return "hmm"
  elif user_input.lower() in ["keren","mantap","bagus","gg"]:
    return "Iyalah Killua gituh hehe"
  elif user_input.lower() in ["lucu","ngakak"]:
    return "^_^"
  elif user_input.lower() in ["wk","wkwk"]:
    return "wkwk"
  elif user_input.lower() in ["apa","kenapa","bagaimana"]:
    return "paan ?"
  else:
    return f"Maaf bang pesan [{Cy}{user_input}{Wh}] {Wh}tidak ada di library killua!"
print(f'{Cy}{My_Bot} {Wh}: {Message}')
try:
  while True:
    user_input = input(f'{Ye}{user} {Wh}: ')
      
    bot_response = generate_response(user_input)
      
    print(f'{Cy}{My_Bot} {Wh}: {bot_response}')
except KeyboardInterrupt:
  print(f"Bot Berhenti...")

