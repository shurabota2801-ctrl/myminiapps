from random import choice

DIGITS = '0123456789'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
PUNCTUATION = '!#$%&*+-=?@^_'
AMBIGUOUS = 'il1Lo0O'

class Generator_Password():
    def params(self):
        questions = ["Включать ли цифры 0123456789", 
                     "Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                     "Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz",
                     "Включать ли символы !#$%&*+-=?@^_",
                     "Исключать ли неоднозначные символы il1Lo0O"]
        answers = [DIGITS, 
                   UPPER_LETTERS, 
                   LOWER_LETTERS, 
                   PUNCTUATION, 
                   AMBIGUOUS]
        
        length = int(input("Введите длину пароля: "))
        count_password = int(input("Количество таких паролей: "))
        print("Далее, для корректного ответа пишите 'да' или 'нет'")

        selected_chars = ''
        for i in range(len(questions)):
            answer = input(f"{questions[i]}: ").lower()            
            if answer == 'да':
                if i == 4:
                    for j in AMBIGUOUS:
                        selected_chars = selected_chars.replace(j, '')
                else:
                    selected_chars += answers[i]
        return selected_chars, length, count_password
    
    def generate_password(self, selected_chars, length, count_password):
        ls_password = []
        for i in range(count_password):
            password = ''
            for j in range(length):
                password += choice(selected_chars)
            ls_password.append(password)
        return ls_password

    def menu(self):
        print("Привет, я генератор паролей!")
        selected_chars, length, count_password = self.params()
        password = self.generate_password(selected_chars, length, count_password)
        print(*password, sep='\n')