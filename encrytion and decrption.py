from cryptography.fernet import Fernet

def encrypt():
    user_name = input('Enter Name: ')
    if user_name=='everest':
        password = input('Enter key: ')
        key = password.encode()
        input_file = str(input('Enter file name: '))
        out=input_file.split('.')
        output_file = out[0]+'.encrypted'
        with open(input_file, 'rb') as f:
            data = f.read()

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)

        with open(output_file, 'wb') as f:
            f.write(encrypted)
    else:
        print('Incorect Name')

def decrypt():
    user_name = input('Enter Name: ')
    if user_name=='everest':
        password = input('Enter key: ')
        key = password.encode()
        input_file = str(input('Enter file name: '))
        out=input_file.split('.')
        output_file = out[0]+'.docx'
        with open(input_file, 'rb') as f:
            data = f.read()

        fernet = Fernet(key)
        encrypted = fernet.decrypt(data)

        with open(output_file, 'wb') as f:
            f.write(encrypted)
    else:
        print('Incorect Name')


num = input('-press 1 to encrypt \n-press 2 to decrypt')
if num=='1':
    encrypt()
else:
    decrypt()