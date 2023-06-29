
from getting_inputs import SubCipher
from dictionary_attack import HackCipher

#stuff left to do

# get key -- verify key
# get message -- verify message
# In final message check case
# copy paste messages
# options menu 1. encode 2.decode 3. hack.. option to save to file


def main():
    the_key="GPSJRTEAMKBWIXCNUOFYZVLHDQ"
    the_message="It is impossible for a Man to learn what HE thinks he already knows"
    
    
    
    message_one = SubCipher()
    cipher = message_one.encrypt(the_message,the_key)
    #decoded_text=message_one.decrypt(cipher,the_key)

    print(the_message)
    print(cipher)
    #print(decoded_text)

    hack_message = HackCipher()
    hack_message.force_decrypt(cipher)
    



if __name__=="__main__":
    main()
