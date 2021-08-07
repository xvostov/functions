import openpyxl

# Функция записывает строку в конец таблицы
def write_to_xlsx(file_path, data):
    """Функция принимает два параметра: 1 - путь к файлу, 2 - что записать в виде списка объектов"""

    wb = openpyxl.load_workbook(file_path)
    sh = wb.active
    sh.append(data)
    wb.save(file_path)
    wb.close()