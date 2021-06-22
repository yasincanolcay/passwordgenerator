#abcçdefgğhıijklmnoöprsştuüvyz
#ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ
#passworder
#'abcçdefgğhıijklmnoöprsştuüvyz1234567890ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ!@#$%^&*'

banner = """                                                                                                                              
 ████████   ██████    █████   █████                             
░░███░░███ ░░░░░███  ███░░   ███░░                              
 ░███ ░███  ███████ ░░█████ ░░█████                             
 ░███ ░███ ███░░███  ░░░░███ ░░░░███                            
 ░███████ ░░████████ ██████  ██████                             
 ░███░░░   ░░░░░░░░ ░░░░░░  ░░░░░░                              
 ░███                                                           
 █████                                                          
░░░░░                                                           
                                        █████                   
                                       ░░███                    
 █████ ███ █████  ██████  ████████   ███████   ██████  ████████ 
░░███ ░███░░███  ███░░███░░███░░███ ███░░███  ███░░███░░███░░███
 ░███ ░███ ░███ ░███ ░███ ░███ ░░░ ░███ ░███ ░███████  ░███ ░░░ 
 ░░███████████  ░███ ░███ ░███     ░███ ░███ ░███░░░   ░███     
  ░░████░████   ░░██████  █████    ░░████████░░██████  █████    
   ░░░░ ░░░░     ░░░░░░  ░░░░░      ░░░░░░░░  ░░░░░░  ░░░░░                                                                                                                                                                                                
"""
print(banner)


import random

karakter = 'abcçdefgğhıijklmnoöprsştuüvyz1234567890ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ!@#$%^&*'
numara = input('>>>[+]OLUŞTURMAK İSTEDİGİDİZ PAROLA SAYISI? : ')
numara = int(numara)
uzunluk = input('>>>[+]PAROLA UZUNLUGU GİRİNİZ: ')
uzunluk = int(uzunluk)

for password in range(numara):
    parola = ''
    for char in range(uzunluk):
        parola += random.choice(karakter)
    print("[*]Parolanız: ",parola)

input()