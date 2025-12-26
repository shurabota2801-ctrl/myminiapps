from notes.notes import ConsoleNotesApp
from weather.weather import ConsoleWeatherApp

class MiniApps():
    def run(self):
        while True:    
            print("\n=== ПРИЛОЖЕНИЯ ===")
            print("1. Погода")
            print("2. Заметки")
            print("3. Выход")

            choice = input("Выберите действие: ")

            match choice:
                case '1':
                    weather = ConsoleWeatherApp()
                    weather.get_weather()
                case '2':
                    note = ConsoleNotesApp()
                    note.run()
                case '3':
                    print("Закрытие программы...")
                    break
                
start_miniapps = MiniApps()
start_miniapps.run()