#   This program will find the word that appears the most in Alice's Adventures in Wonderland


def read_Alice_text(file_path):
            #file = open(file_path, "r", encoding='UTF8')
            #file_content = file.read()
            #return file_content
            print('read Alice')
    

def clean_Alice():
        #clean_a()
        #clean_b()
        print('clean Alice')

def count_words_in_Alice():
        print('count Alice')
    
   

#print(read_Alice_text("D:/OneDrive/studies/Bar-Ilan/pyton/BI-Python/alice_in_wonderland.txt"))



Alice_Path = "D:/OneDrive/studies/Bar-Ilan/pyton/BI-Python/alice_in_wonderland.txt"

def main_count_Alice():
    Alice_text = read_Alice_text(Alice_Path)
    Alice_words = clean_Alice(Alice_text)
    (words_dict, max_word_count) = count_words_in_Alice(Alice_words)


    main_count_Alice()




    





