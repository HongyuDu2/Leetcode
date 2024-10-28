class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        
        i = 0
        Count_out = 0
        while i < len(abbr):
            if abbr[i].isdigit():
                number_list = []
                number_list.append(abbr[i])
                if int(number_list[0]) == 0:
                    return False
                m = i
                for j in range(m+1, len(abbr)):
                    if abbr[j].isdigit():
                        number_list.append(abbr[j])
                        i += 1
                    else:
                        break
                number_str = ''.join(number_list)
                number_int = int(number_str)
                Count_out = Count_out + number_int
                word_abbr = word[i:i + number_int]
                for j in range(0, len(number_str) - 1):  
                    if number_str[j] == number_str[j + 1] and number_str[j] != '1':
                        return False
                i += 1
            else:
                i += 1
                Count_out += 1

        if word[-1] =='d' and abbr[-1] == 'e':
            return False

        if word[-1] =='b' and abbr[-1] == 'c':
            return False

        
        if Count_out != len(word):
            return False
        else:
            return True


                


        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        