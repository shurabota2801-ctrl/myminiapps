from notes.notes import ConsoleNotesApp

class MiniApps():

    def run(self):
        print("\n=== ПРИЛОЖЕНИЯ ===")
        print("1. Погода")
        print("2. Заметки")
        print("3. Выход")

        choice = input("Выберите действие: ")

        match choice:
            case '1':
                pass
            case '2':
                note = ConsoleNotesApp()
                note.run()
