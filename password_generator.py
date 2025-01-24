import random
import time

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special = '!#$%&*+-=?@^_'

ambigious = 'Il1Lo0O'

def generate(length, chars, exon):
    psw = ''
    while(len(psw)!=length):
        ch = random.choice(chars)
        if exon:
            while ch in ambigious:
                ch = random.choice(chars)
        psw += ch
    return psw
    
def user_interact():
    print('Hello! I will generate passwords for you')
    time.sleep(2)
    quan = input('How much passwords do you need? ')
    while quan.isdigit()==False:
        print('Please enter a number!')
        quan = input()
    quan = int(quan)
    leng = input('How long do you want them to be? ')
    while leng.isdigit()==False:
        print('Please enter a number!')
        leng = input()
    leng = int(leng)
    
    print('Do I include digits? (yes/no)')
    if input().lower().startswith('y'):
        digon = True
    else:
        digon = False
        
    print('Do I include uppercase letters? (yes/no)')
    if input().lower().startswith('y'):
        upon = True
    else:
        upon = False
    
    print('Do I include lowercase letters? (yes/no)')
    if input().lower().startswith('y'):
        lowon = True
    else:
        lowon = False
        
    print('Do I include special characters (!#$%&*+-=?@^_)? (yes/no)')
    if input().lower().startswith('y'):
        spon = True
    else:
        spon = False
        
    print('Do I exclude ambigious characters (Il1Lo0O)? (yes/no)')
    if input().lower().startswith('y'):
        exon = True
    else:
        exon = False
    
    print()
    
    usable = ''
    if digon:
        usable += digits
    if upon:
        usable += uppercase_letters
    if lowon:
        usable += lowercase_letters
    if spon:
        usable += special
    
    time.sleep(1)
    for _ in range(3):
        print('Generating...')
        print()
        time.sleep(1.5)
    
    print('Alright, here are your passwords:')
    for _ in range(quan):
        print (generate(leng, usable, exon))
    time.sleep(1)
    print('Do you want do generate more? (yes/no)')
    if input().lower().startswith('y'):
        return True
    else:
        return False
while user_interact()==True:
    user_interact()