import sqlite3
import openpyxl

class ConsoleNotesApp():
    def __init__(self):
        self.conn = sqlite3.connect('notes.db')
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        '''Создание базы данных в директории проекта. Если бд создана, то не повторно создаваться не будет'''
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                done BOOLEAN DEFAULT False,
                created_at TIMESTAMP DEFAULT (datetime('now', 'localtime')),
                updated_at TIMESTAMP
            )
            ''')
        self.conn.commit()

    def get_all_notes(self):
        '''Выводит все заметки с базы данных'''
        self.cursor.execute('''
            SELECT id, title, content, done, created_at, updated_at
            FROM notes
                            ''')
        notes = self.cursor.fetchall()

        print("\n==== Все заметки ====")
        for note in notes:
            print(f"\nID: {note[0]}")
            print(f"Заголовок: {note[1]}")
            print(f"Содержание: {note[2]}")
            print(f"Выполнено: {'Да' if note[3] else 'Нет'}")
            print(f"Создано: {note[4]}")
            print(f"Обновлено: {note[5] if note[5] is not None else 'Не обновлялась'}")

    def get_one_note(self, id):
        '''Проверка на существование заметки'''    
        self.cursor.execute('''
            SELECT id, title, content, done
            FROM notes
            WHERE id = ?
                            ''',
            (id,))
        result = self.cursor.fetchone()
        return result

    def add_note(self, title, content):
        '''Добавление заметки'''
        self.cursor.execute('''
            INSERT INTO notes (title, content)
            VALUES (?, ?)
                            ''',
            (title, content))
        self.conn.commit()
        print(f"Заметка '{title}' успешно сохранена!")

    def update_note(self, id):
        if id:
            try:
                result = self.get_one_note(id)
                if result:
                    note_id, old_title, old_content, old_done = result
                    print(f"\n==== Обновление заметки с ID: {note_id} ====")
                    print(f"Текущий заголовок: {old_title[:40] + '...' if len(old_title) > 40 else old_title}")
                    print(f"Текущее содержимое: {old_content[:40] + '...' if len(old_content) > 40 else old_content}")
                    print(f"Выполнено: {'Да' if old_done == True else  'Нет'}")
                    print('Введите новые данные (оставьте поле пустым, чтобы сохранить текущее значение):')
                    new_title = input("Новый заголок: ").strip()
                    if not new_title:
                        new_title = old_title
                    new_content = input("Новое содержание: ").strip()
                    if not new_content:
                        new_content = old_content
                    new_done = input("Заметка выполнена: ").strip().lower()
                    if not new_done:
                        new_done = old_done
                    if new_done == 'да':
                        new_done = True
                    else:
                        new_done = False


                    confirm = input("Подтвердите обновление (y/n): ").strip()
                    if confirm == 'y' or confirm == 'д':
                        self.cursor.execute('''
                            UPDATE notes
                            SET title = ?, content = ?, done = ?, updated_at = datetime('now', 'localtime')
                            WHERE id = ?
                                            ''',
                            (new_title, new_content, new_done, note_id))
                        self.conn.commit()
                        print('Заметка успешно обновлена!')
                    else:
                        print('Обновление отменено!')
                else:
                    print(f'Заметка с ID: {id} не найдена!')
            except Exception as e:
                print(f"Ошибка: {e}")



    def delete_note(self, id):
        '''Удаление заметки'''
        if id:
            try:
                result = self.get_one_note(id)
                if result:
                    note_id, title, content, done = result
                    print(f"Вы точно хотите удалить заметку: '{title}'?")
                    confirm = input("Подтвердите, 'y/n': ")
                    if confirm == 'y' or confirm == 'д':
                        self.cursor.execute('''
                            DELETE 
                            FROM notes
                            WHERE id = ?
                                            ''',
                            (note_id,))
                        self.conn.commit()
                        print("Заметка успешно удалена!")
                    else:
                        print("Удаление отменено!")
                else:
                    print(f'Заметка с ID: {id} не найдена!')
            except sqlite3.Error as e:
                print(f"Ошибка базы данных: {e}")
            except Exception as e:
                print(f"Ошибка: {e}")
                

    def search_note(self, context):
        '''Поиск по заголовку и содеранию'''
        search_context = f"%{context}%"
        self.cursor.execute('''
            SELECT id, title, content, done, created_at, updated_at
            FROM notes
            WHERE title LIKE ? OR content LIKE ?
                            ''',
            (search_context, search_context))
        
        result = self.cursor.fetchall()
        if result:
            print("\n==== Вот что нашлось ====")
            for note in result:
                print(f"\nID: {note[0]}")
                print(f"Заголовок: {note[1]}")
                print(f"Содержание: {note[2]}")
                print(f"Выполнено: {'Да' if note[3] else 'Нет'}")
                print(f"Создано: {note[4]}")
                print(f"Обновлено: {note[5] if note[5] is not None else 'Не обновлялась'}")
        else:
            print("Ничего не найдено!")

    def close(self):
        '''Закрывает соединение с базой данных'''
        self.conn.close()
    
    def other(self):
        while True:
            print("\n=== ДРУГОЕ ===")
            print("1. Показать погоду")
            print("2. Назад к заметкам")

            choice = input("Выберите действие: ")
            if choice == '1':
                print("Еще в разработке")
            
            elif choice == '2':
                return


    def run(self):
        '''Запуск меню приложения'''
        while True:
            print("\n=== МЕНЕДЖЕР ЗАМЕТОК ===")
            print("1. Показать все заметки")
            print("2. Добавить заметку")
            print("3. Обновить заметку")
            print("4. Удалить заметку")
            print("5. Поиск заметок")
            print("6. Экпортировать заметки в excel")
            print("7. Другое")
            print("8. Назад")
            print("9. Выход")

            choice = input('Выберите действие: ').strip()
            if choice == '1':
                self.get_all_notes()

            elif choice == '2':
                title = input('Введите заголовок заметки: ').strip()
                content = input('Введите содержание заметки: ').strip()
                self.add_note(title,content)

            elif choice == '3':
                id = input('Введите ID заметки, которую хотите обновить: ').strip()
                self.update_note(id)

            elif choice == '4':
                id = input('Введите ID заметки, которую хотите удалить: ').strip()
                self.delete_note(id)

            elif choice == '5':
                context = input("Введите то, что ищете: ").strip().lower()
                self.search_note(context)

            elif choice == '6':
                self.export_to_excel()

            elif choice == '7':
                self.other()

            elif choice == '8':
                return
            elif choice == '9':
                self.close()
                print("Выход из программы...")
                break

            elif choice == 'скрипт':
                self.cursor.execute('''
                INSERT INTO notes (title, content, done) 
                VALUES 
                    ('Заголовок заметки', 'Это мое первое тестовое содержание', 0),
                    ('И вот еще одна', 'Содержимое второй заметки', 1),
                    ('Заметочка', 'Еще одна тестовая запись', 0),
                    ('Нужно быстро', 'Проверка работы базы данных', 0),
                    ('Все', 'Финальная тестовая запись', 1);
                                    ''')
                self.conn.commit()
                print('Скрипт выполнен, данные добавлены!')

    def export_to_excel(self, filename = 'notes.xlsx'):
        '''Экспорт заметок в excel файл'''

        self.cursor.execute('''
            SELECT id, title, content, done, created_at, updated_at
            FROM notes
            ORDER BY id
                            ''')
        result = self.cursor.fetchall()

        if not result:
            print('Нет заметок для экспорта!')
            return
            
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(['ID', 'Заголовок', 'Содержание', 'Выполнено', 'Создано', 'Обновлено'])
        for note in result:
            ws.append(note)
        wb.save(filename)
        print(f"Данные добавлены в {filename}")

if __name__ == "__main__":
    app = ConsoleNotesApp()
    try:
        app.run()
    except KeyboardInterrupt:
        print("\n\nПрограмма завершена пользователем.")
        app.close()
