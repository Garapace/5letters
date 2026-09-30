ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
UNKNOWN_LETTERS = "_*.?- "


def get_conditions():

    need = input("введите буквы, которые есть в слове:\n").lower()
    while len(need) > 5 or any(letter not in ALPHABET for letter in need.lower()):
        need = input("только русские буквы, не больше 5-ти букв\n").lower()

    ban = input("введите буквы, которых нет в слове:\n").lower()
    while any(letter not in ALPHABET for letter in ban.lower()):
        ban = input("допускаются только буквы из русского алфавита\n").lower()
    
    pattern = input("введите шаблон слова (например с_о_о):\n").lower()
    while ((pattern and len(pattern) != 5) or any(letter not in ALPHABET + UNKNOWN_LETTERS for letter in pattern)):
        pattern = input("шаблон должен содержать 5 символов и только русские буквы, _, * или .:\n").lower()

    return need, ban, pattern


def find_word(need, ban, pattern):
    with open("words.txt", "r", encoding="UTF-8") as file:
        words = file.read().splitlines()
    
    good_words = []

    for word in words:

        valid = True
        for letter in need:
            if letter not in word:
                valid = False
        
        for letter in ban:
            if letter in word:
                valid = False
        
        for index, letter in enumerate(pattern):
            if letter not in UNKNOWN_LETTERS:
                if word[index] !=  letter:
                    valid = False

        if valid:
            good_words.append(word)

    return good_words


def main():

    for word in find_word(*get_conditions()):
        print(word)


if __name__ == "__main__":
    main()
