
class SubCipher():
    def __init__(self):
        self.__base_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
    def encrypt(self,message,key):
        return self._translate(message,key,'encrypt')

    def decrypt(self,ciphertext,key):
        return self._translate(ciphertext,key,'decrypt')

    def _translate(self,message,key,mode):
        if not self._is_key_valid(key):
            raise Exception("Invalid Key")
        
        key_list= key.lower()
        letters_list=self.__base_key.lower()
        message_to_use = message
        
        if mode == "decrypt":
            key_list,letters_list = letters_list,key_list

        translate_message=''

        for each_letter in message_to_use:
            postition_index = letters_list.find(each_letter.lower())
            new_letter=''

            if postition_index<0:
                new_letter=each_letter
            else:
                new_letter=key_list[postition_index]
                if each_letter.isupper():
                    new_letter = new_letter.upper()

            translate_message+= new_letter    
        
        return translate_message

    def _is_key_valid(self,inp_key):
        key_list=list(inp_key.lower())
        letters_list=list(self.__base_key.lower())
        key_list.sort()
        letters_list.sort()
        return key_list==letters_list

        


