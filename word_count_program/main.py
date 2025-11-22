class WordCounter:

    
    def user_interface(self):
        """The function communicates with the user and links all the logic and functions together."""

        print(f" {'*' * 30} \n Welcome In Word Counter Program \n {'*' * 30} ")


        text = input("Please enter the full text my dear : ").strip().lower()
        words_count = self.get_words_count(text)

        print(f" {'-' * 30} \n I'm finished! The number of words in the text is : {words_count} \n {'-' * 30}")

        
    def get_words_count(self, text: str):
        """A function to iterate through each letter in the text and count the number of words in the text."""

        words_count = 0
        in_word = False

        for l in text:
            
            if l.isalpha():
                if not in_word:
                    in_word = True
                    words_count += 1

            else:
                in_word = False
            
        
        return words_count



if __name__ == "__main__":
    counter = WordCounter()
    counter.user_interface()
