
from getting_inputs import SubCipher
from dictionary_attack import HackCipher

def main():
    the_key="GPSJRTEAMKBWIXCNUOFYZVLHDQ"
    the_message="It is impossible for a Man to learn what HE thinks he already knows."
    
    message_one = SubCipher()
    
    cipher = message_one.encrypt(the_message,the_key)
    decoded_text=message_one.decrypt(cipher,the_key)

    print(the_message)
    print(cipher)
    print(decoded_text)

    hack_message = HackCipher()
    
    



if __name__=="__main__":
    main()
