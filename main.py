
def main():
    with open("/Users/joshua/workspace/github.com/username/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        
        def word_count(text):
            count = 0
            for i in words:
                count += 1
            return count
        count_of_words = word_count(words)
        
        word_dict = dict()
        letter_list = []
            
        #adds only letters of the alphabet to a new word list.
        for word in words:
            for letter in word:
                if letter.isalpha():
                    letter_list.append(letter.lower())
                    


        #add letters to dictionary and incrament if not found          
        for letter in letter_list:
            if letter in word_dict:
                word_dict[letter] += 1
            else:
                word_dict[letter] = 1

        output_list = word_dict.items()
                
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count_of_words} words found in the document")
        for key, value in sorted(output_list):
            print(f"The '{key}' character was found {value} times")

            
main()