import random, sys
from time import sleep


random_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', 
 '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '/', '?', '~', '`', ' ']

def match_text(text1, text2):
    text1_list = [letter for letter in text1]
    text2_list = [letter for letter in text2]
    equal_indices = []
    for i in range(len(text1_list)):
        if(text1_list[i] == text2_list[i]):
            equal_indices.append(i)
    return equal_indices

def random_generator(size):
    fake_text = []
    for i in range(size):
        fake_text.append(random.choice(random_letters))
    return fake_text
    
def change_text(text_list, change_indices):
    for i in range(len(text_list)):
        if i not in change_indices:
            text_list[i] = random.choice(random_letters)
    return text_list

def main():
    if len(sys.argv) == 1:
        text = "Try writing a custom text after python glitch.py!"
    else:
        text = sys.argv[1]

    # Converting string to list
    letter_list = [letter for letter in text]
    fake_list = random_generator(len(letter_list))
    correct_indices = []

    while letter_list != fake_list:
        
        print(''.join(fake_list), end='\r')
        correct_index = match_text(letter_list, fake_list)
        if correct_index:
            correct_indices.extend(correct_index)
        if(len(correct_indices) <= 0):
            fake_list = random_generator(len(letter_list))
        else:
            fake_list = change_text(fake_list, correct_indices)
        sleep(0.01)

    print(''.join(letter_list))
    
    
if __name__ == "__main__":
    main()