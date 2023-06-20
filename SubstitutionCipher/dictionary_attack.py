
#0 Arranged dictionary to word patterns
# FORMAT of DICT = { key=number_of letters : { key=word pattern : [list of words with that patters]  }     }
#1 list of words from ciphertext
#2 arrange words from longest to shortest
#3 from longest -- search for word pattern and possible matches
#4 create possible key mappings
#5 if certainity on one key, update possible keymapping
#6 next longest word.





class HackCipher():
    def __init__(self):
        self._ciphertext_in_words=True
        self._are_conditions_met=False
        self._filename_for_dictionary="dictionary.txt"
        self._filename_for_arranged_dict="arranged_dict.txt"

        self._are_conditions_met = self.__dictionary_check()
        if not self._are_conditions_met:
            raise Exception("Dictionary not present")
        
        #check if dictionary and arranged dictionary exist
        #if not create arranged dictionary

    def __dictionary_check(self):
        is_dictionary_present=False
        is_arranged_dict_present=False

        try:
            with open(self._filename_for_dictionary) as f:
                text=f.read()
                words=text.split()
                print(f"Dictionary is {len(words)} words long")
                is_dictionary_present=True
        except FileNotFoundError:
            print("Dictionary file not found ")
            
        
        try:
            with open(self._filename_for_arranged_dict) as f:
                print("Arranged Dictionary file exists")
                is_arranged_dict_present=True
        except FileNotFoundError:
            print("Arranged Dictionary file not found ")
            
        if is_arranged_dict_present and is_dictionary_present:
            return True
        elif is_dictionary_present and not is_arranged_dict_present:
            print("We have a dictionary - Creating arranged dictionary from it")
            self.__create_arranged_dictionary()
            return True
        else:
            return False
        

    def __create_arranged_dictionary():
        pass






