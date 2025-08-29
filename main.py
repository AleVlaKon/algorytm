import win32com.client as win32

def excel_to_word_with_formatting(excel_path, sheet_name, word_path):
    # Запуск Excela
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    excel.Visible = False  # Скрыть Excel (для отладки можно поставить True)
    wb = excel.Workbooks.Open(excel_path)
    sheet = wb.Sheets(sheet_name)
    
    # Выделить таблицу (можно задать диапазон вручную, например "A1:D10")
    used_range = sheet.UsedRange
    used_range.Copy()  # Копирование в буфер обмена
    
    # Запуск Word и вставка
    word = win32.gencache.EnsureDispatch('Word.Application')
    word.Visible = False  # Скрыть Word
    doc = word.Documents.Add()
    word.Selection.PasteExcelTable(False, False, False)  # Вставка с форматированием
    
    # Сохранение и закрытие
    excel.CutCopyMode = False  # Очищает буфер обмена Excel
    doc.SaveAs(word_path)
    doc.Close()
    wb.Close()
    
    excel.Quit()
    word.Quit()
    print(f"Таблица скопирована в Word с сохранением форматирования: {word_path}")

# Пример использования
excel_path = r"D:\Users\av.kontikov\Downloads\PortableGit\algorytm/Смета.xlsx"  # Полный путь к Excel
sheet_name = "Ресурсная смета 14 граф"           # Название листа
word_path = r"D:\Users\av.kontikov\Downloads\PortableGit\algorytm/output.docx"   # Куда сохранить Word


def get_last_cell(file_path):
    # Запускаем Excel
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    
    try:
        # Открываем книгу
        workbook = excel.Workbooks.Open(file_path)
        sheet = workbook.ActiveSheet
        
        # Получаем последнюю используемую ячейку
        last_cell = sheet.UsedRange.SpecialCells(11)  # 11 = xlCellTypeLastCell
        
        # Возвращаем адрес и значение последней ячейки
        address = last_cell.Address
        value = last_cell.Value
        
        return {
            'address': address,
            'value': value,
            'row': last_cell.Row,
            'column': last_cell.Column
        }
        
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        # Закрываем книгу и Excel
        workbook.Close(False)
        excel.Quit()

file_path = r'D:\Users\av.kontikov\Downloads\PortableGit\algorytm/Смета.xlsx'
# last_cell_info = get_last_cell(file_path)
excel_to_word_with_formatting(excel_path, sheet_name, word_path)
# print(f"Последняя ячейка: {last_cell_info['address']}")
# print(f"Значение: {last_cell_info['value']}")