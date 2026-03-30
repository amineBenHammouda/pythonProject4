import openpyxl

def before_all(context):
    # Load the Excel file
    context.workbook = openpyxl.load_workbook("C:/Users/amine/Desktop/data.xlsx")
    context.sheet = context.workbook.active
    context.users = []
    headers = [cell.value for cell in context.sheet[1]]
    for row in context.sheet.iter_rows(min_row=2, values_only=True):
        user_data = dict(zip(headers, row))
        context.users.append(user_data)