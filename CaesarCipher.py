#! usr/bin/env python3
# Code written by Security Programmer: AbdulMuaz Aqeel, Iraq - Baghdad
# Social Media: facebook.com/AbdulMuaz.Aqeel.SSP
Intro = '''
              00000         aa         eeeeeeee    ggggg          aa         oooooooo
             00            aaaa        ee         gg    gg       aaaa        oo     oo
            00            aa  aa       ee          gg           aa  aa       oo    oo
           00            aa    aa      eeeeeeee      ggg       aa    aa      oooooo*
            00          aaaaaaaaaa     ee               gg    aaaaaaaaaa     oo   oo
             00        aa        aa    ee         gg   gg    aa        aa    oo    oo
              00000   aa          aa   eeeeeeee     ggg     aa          aa   oo     oo

              ============================[Caesar Cipher]=============================
                   Programmed by: AbdulMuaz Aqeel (Security Systems Programmmer)
                            Facebook: facebook.com/AbdulMuaz.Aqeel.SSP
'''
def main():
    secret_user_key = 0
    en_de_crypt_msg = ''
    Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz' \
              '!@#$%&*(){}[]<>/\|";:\n-=+.,?1234567890'
    print(Intro)
    print('\nCaesar Cipher v1.0 - based on Python3.5')
    print("Okay Sir, What's Your Choice:")
    print('   1. Encryption\n   2. Decryption')
    option = input(' > ')
    if option == '1':
        print('All Right Sir..You Choosed({0})..Now Which One You are going to Choose:'.format(option))
        print('   1. Encrypt Text File\n   2. Encrypt Direct Message')
        option_2 = input(' > ')
        if option_2 == '1':
            file = input('  >> What Text File Would You Like To Encrypt: ')
            while secret_user_key == '' or secret_user_key == '0' or secret_user_key == 0:
                secret_user_key = input('  >> Enter Encryption Key [Integer Number 1 - 90] : ')
            if file.endswith('.txt'):
                try:
                    file_message = open(file, 'r').read()
                except(IOError, FileExistsError, FileNotFoundError):
                    print('Error_File: Check The Text File.')
                for char in file_message:
                    if char in Letters:
                        number = Letters.find(char)
                        try:
                            number = number + int(secret_user_key)
                        except(ValueError) as Value_Error:
                            print('Error_Key: Incorrect key.')
                            break
                        if number >= len(Letters):
                            number = number - len(Letters)
                        elif number < 0:
                            number = number + len(Letters)
                        en_de_crypt_msg = en_de_crypt_msg + Letters[number]
                    else:
                        en_de_crypt_msg = en_de_crypt_msg + char
                    save_file = open('Encrypted_File.txt', 'w')
                    save_file.write(en_de_crypt_msg)
                    save_file.close()
        elif option_2 == '2':
            user_message = input('  >> What Message Would You Like To Encrypt: ')
            while secret_user_key == '' or secret_user_key == '0' or secret_user_key == 0:
                secret_user_key = input('  >> Enter Encryption Key [Integer Number 1 - 90] : ')
            for char in user_message:
                if char in Letters:
                    number = Letters.find(char)
                    try:
                        number = number + int(secret_user_key)
                    except(ValueError) as Value_Error:
                        print('Error_Key: Incorrect key.')
                        break
                    if number >= len(Letters):
                        number = number - len(Letters)
                    elif number < 0:
                        number = number + len(Letters)
                    en_de_crypt_msg = en_de_crypt_msg + Letters[number]
                else:
                    en_de_crypt_msg = en_de_crypt_msg + char
            print('Message has been Encrypted: ', en_de_crypt_msg, '\n')
    elif option == '2':
        print('All Right Sir..You Choosed({0})..Now Which One You are going to Choose:'.format(option))
        print('   1. Decrypt Text File\n   2. Decrypt Direct Message')
        option_2 = input(' > ')
        if option_2 == '1':
            file = input('  >> What Text File Would You Like To Decrypt: ')
            while secret_user_key == '' or secret_user_key == '0' or secret_user_key == 0:
                secret_user_key = input('  >> Enter Decryption Key [1 - 90] <Note: The Same Encryption Key!> : ')
            if file.endswith('.txt'):
                try:
                    file_message = open(file, 'r').read()
                except(IOError, FileExistsError, FileNotFoundError):
                    print('Error_File: Check The Text File.')
                for char in file_message:
                    if char in Letters:
                        number = Letters.find(char)
                        try:
                            number = number - int(secret_user_key)
                        except(ValueError) as Value_Error:
                            print('Error_Key: Incorrect key.')
                            break
                        if number >= len(Letters):
                            number = number - len(Letters)
                        elif number < 0:
                            number = number + len(Letters)
                        en_de_crypt_msg = en_de_crypt_msg + Letters[number]
                    else:
                        en_de_crypt_msg = en_de_crypt_msg + char
                    save_file = open('Decrypted_File.txt', 'w')
                    save_file.write(en_de_crypt_msg)
                    save_file.close()
        elif option_2 == '2':
            user_message = input('  >> What Message Would You Like To Decrypt: ')
            while secret_user_key == '' or secret_user_key == '0' or secret_user_key == 0:
                secret_user_key = input('  >> Enter Decryption Key [1 - 90] <Note: The Same Encryption Key!> : ')
            for char in user_message:
                if char in Letters:
                    number = Letters.find(char)
                    number = number - int(secret_user_key)
                    if number >= len(Letters):
                        number = number - len(Letters)
                    elif number < 0:
                        number = number + len(Letters)
                        en_de_crypt_msg = en_de_crypt_msg + Letters[number]
                else:
                    en_de_crypt_msg = en_de_crypt_msg + char
            print(en_de_crypt_msg)

if __name__ == '__main__':
    main()