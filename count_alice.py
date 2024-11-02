#   This program will find the word that appears the most in Alice's Adventures in Wonderland



def main_count_Alice():
    alice_text = read_Alice_text()
    clean_alice_text = clean_Alice(alice_text)

    def read_Alice_text(text_path):
            content = open(text_path)
            content = open(text_path)
            return content.read()
    

    def clean_Alice():
        pass
    
    splitted_text = read_Alice_text("/home/oron/github/BI-Python/BI-Python/alice_in_wonderland.txt")

    print(splitted_text)


    

