
    def caesar():
        size = 26
        
        enc = input("Enter in The encrypted message: \n").upper()
        enc = enc.replace('"', '')
        enc = enc.replace('\'', '')
        enc = enc.replace('.', '')
        
        print('Enter the key number (1-%s)' % size)
        key = int(input())
        if (key > size):
          print('Key number (1-%s)' % size)
          key = int(input()) # Key for Lab = 23
        
        trans = ''
        
        for letter in enc:
          # Allows Spaces to be ignored
          if letter.isalpha():
             num = ord(letter)
             num += key
        
             if num > ord('Z'):
                num -= 26
             elif num < ord('A'):
                num += 26
        
             trans += chr(num)
        
        print(trans)
    
    
    def vigenere():
       alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
       enc = input("Enter in The encrypted message: \n").upper()
       key = input("Enter in The Key : \n").upper()
    
       length = len(key)
       intkey = [ord(i) for i in key]
       caesartext_int = [ord(i) for i in enc]
       trans = ''
       for i in range(len(caesartext_int)):
           value = (caesartext_int[i] - intkey[i % length]) % 26
           trans += chr(value + 65)
       print(trans)
    
    ############ MAIN #####################################################
    print("Please choose Your Decryption Algorithm\n")
    userIn = int(input("1 for Caesar caesar\nor\n2 for Vigenere\n"))
    if userIn == 1:
        print(userIn)
        caesar()
    elif userIn == 2:
        print(userIn)
        vigenere()
    else:
        print("Input Incorrect! Please Choose 1 or 2")
