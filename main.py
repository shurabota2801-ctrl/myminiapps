from notes.apps import ConsoleNotesApp
from weather.apps import ConsoleWeatherApp
from magic_ball.apps import Magic_Answer
from generator_password.apps import Generator_Password

class MiniApps():
    def run(self):
        while True:    
            print("\n=== ПРИЛОЖЕНИЯ ===")
            print("1. Погода")
            print("2. Заметки")
            print("3. Магический шар")
            print("4. Генерация пароля")
            print("5. Выход")

            choice = input("Выберите действие: ")

            match choice:
                case '1':
                    weather = ConsoleWeatherApp()
                    weather.get_weather()
                case '2':
                    notes = ConsoleNotesApp()
                    notes.run()
                case '3':
                    prediction = Magic_Answer()
                    prediction.answer_menu()
                case '4':
                    generate_password = Generator_Password()
                    generate_password.menu()
                case '5':
                    print("Закрытие программы...")
                    break
                
start_miniapps = MiniApps()
start_miniapps.run()