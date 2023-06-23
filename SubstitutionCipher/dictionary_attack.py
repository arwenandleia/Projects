import json
#0 Arranged dictionary to word patterns ---DONE
# FORMAT of DICT = { key=number_of letters : { key=word pattern : [list of words with that patters]  }  } ---DONE
#1 list of words from ciphertext
#2 arrange words from longest to shortest
#3 from longest -- search for word pattern and possible matches
#4 create possible key mappings
#5 if certainity on one key, update possible keymapping
#6 next longest word.

class HackCipher():
    def __init__(self):
        self._ciphertext_in_words=True #each word is seperated by space
        self._are_conditions_met=False
        self._filename_for_dictionary="dictionary.txt"
        self._filename_for_arranged_dict="spec_dict.txt"

        self._are_conditions_met = self.__dictionary_check()
        if not self._are_conditions_met:
            raise Exception("Dictionary not present or in wrong format")
        

    def __dictionary_check(self):
        is_dictionary_present=False
        is_arranged_dict_present=False

        try:
            with open(self._filename_for_dictionary) as f:
                #text=f.read()
                #words=text.split()
                #print(f"Dictionary is {len(words)} words long")
                is_dictionary_present=True
        except FileNotFoundError:
            print("Dictionary file not found ")
        
        try:
            with open(self._filename_for_arranged_dict) as f:
                #print("Arranged Dictionary file exists")
                is_arranged_dict_present=True
        except FileNotFoundError:
            print("Arranged Dictionary file not found ")
            
        if is_arranged_dict_present and is_dictionary_present:
            print("Both Dictionary and Arranged Dictionary Found")
            return True
        elif is_dictionary_present and not is_arranged_dict_present:
            print("We have a dictionary - Creating arranged dictionary from it")
            return self.__create_arranged_dictionary()
        else:
            return False

    def __create_arranged_dictionary(self):
        print("creating arranged dictionary")
        words=self.__get_list_of_words()
        if not words:
            return False
        words.sort(key=len,reverse=True)
        special_dict = self.__get_arranged_dictionary(words)
        with open(self._filename_for_arranged_dict,"w") as outfile:
           json.dump(special_dict,outfile)
           return True

    def __get_list_of_words(self):
        try:
            with open(self._filename_for_dictionary) as f:
                text=f.read()
                return text.split()
                
        except FileNotFoundError:
            print("file not found")
            return None

    def __get_arranged_dictionary(self,words):
        arranged_dictionary={}
        
        for each_word in words:
            each_word=each_word.lower()
            length_of_word = len(each_word)
            word_pattern = self.__get_word_pattern(each_word)

            if length_of_word in arranged_dictionary:
                if word_pattern in arranged_dictionary[length_of_word]:
                    arranged_dictionary[length_of_word][word_pattern].append(each_word)
                else:
                    arranged_dictionary[length_of_word][word_pattern]=[each_word]
                
            else:
                arranged_dictionary[length_of_word]= { word_pattern: [each_word]}

        return arranged_dictionary
    
    def __get_word_pattern(self,single_word):
        single_word=single_word.lower()
        word_pattern_string=''
        word_pattern_list=[]
        
        for each_letter in single_word:
            if each_letter not in word_pattern_list:
                word_pattern_list.append(each_letter)

            index_of_letter_in_list= word_pattern_list.index(each_letter)
            word_pattern_string+= str(index_of_letter_in_list)+'.'

        return word_pattern_string




