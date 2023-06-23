class KeyMappings():
    def __init__(self,ciphertext):
          self.__base_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
          self.__keymap = {}
          self.__solved_cipher_letters = {}
          self.__ciphertext=ciphertext
          self.__generate_blank_keymap(ciphertext)

    def __generate_blank_keymap(self,cipher):
        for each_letter in self.__base_key:
            if each_letter not in self.__keymap:
                if each_letter in cipher:
                    self.__keymap[each_letter]=[False] #start by setting first element of list to false. if solved set this to true

    def add_key_to_poss_word(self,cipher_word,possible_solutions):  #possible solutions is a list correspoding to cipher word
        
        for each_poss_sol in possible_solutions:
            tmp_keymap={}
            
            for i in range(len(cipher_word)):
                cipher_letter = cipher_word[i]
                possible_letter = each_poss_sol[i]
                if self.__keymap[cipher_letter][0] and possible_letter not in self.__keymap[cipher_letter]:
                    tmp_keymap=None
                    break
                
                if cipher_letter in self.__solved_cipher_letters:
                    expected_solved_letter = self.__solved_cipher_letters[cipher_letter]
                    if expected_solved_letter is not possible_letter:
                        tmp_keymap=None
                        break

                if cipher_letter not in tmp_keymap:
                    tmp_keymap[cipher_letter]=possible_letter
                    
            
            if tmp_keymap:
                for new_cipher_letter in tmp_keymap:
                    new_possible_letter = tmp_keymap[new_cipher_letter]
                    if new_possible_letter not in self.__keymap[new_cipher_letter]:
                        self.__keymap[new_cipher_letter].append(new_possible_letter)
        
        self.__set_true_for_new_cipher_letters()

    def __set_true_for_new_cipher_letters(self):
        
        for each_key in self.__keymap:
            #if(self.__keymap[each_key][0]):
            #    continue

            len_of_each_key=len(self.__keymap[each_key])
            if len_of_each_key>1:
                self.__keymap[each_key][0]=True

            if len_of_each_key==2: # add each key to solved dict
                if each_key not in self.__solved_cipher_letters:
                    self.__solved_cipher_letters[each_key]=self.__keymap[each_key][1]
                    self.__remove_solved_letters(each_key, self.__keymap[each_key][1])

    def reduce_solved_letters(self):
        were_letters_removed=True
        while were_letters_removed:
            were_letters_removed=False
            for each_key in self.__keymap: #each_key corresponds to cipher letter
                len_of_possible_letters = len(self.__keymap[each_key])
                if len_of_possible_letters==2:
                    solved_letter = self.__keymap[each_key][1]
                    if self.__remove_solved_letters(each_key,solved_letter):
                        were_letters_removed=True
            

    def __remove_solved_letters(self,cipher_letter,solved_letter):
        were_solved_letters_removed=False
        for each_key in self.__keymap:
            if cipher_letter is not each_key:
                if solved_letter in self.__keymap[each_key]:
                    self.__keymap[each_key].remove(solved_letter)
                    were_solved_letters_removed=True
        return were_solved_letters_removed

    def show_keys(self):
        for key in self.__keymap:
            print(f"{key} --> {self.__keymap[key]}")
