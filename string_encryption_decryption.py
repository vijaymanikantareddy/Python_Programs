from cryptography.fernet import Fernet
msg = input('enter a string: ')

key = Fernet.generate_key()

fernet = Fernet(key)

encmsg = fernet.encrypt(msg.encode())

print('original string: ',msg)
print('encrypted string: ',encmsg)

decmsg = fernet.decrypt(encmsg).decode()
print('decrypted string: ',decmsg)
