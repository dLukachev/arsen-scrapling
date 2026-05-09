import gspread

gc = gspread.service_account(filename="other/apis.json")

sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/19qhIlVPL5gSZNe6-C-igfuxmv6o9jJkocRLrD-Y45aw/edit?gid=0#gid=0")

ws = sh.sheet1

name = input("Напиши имя нового чипса\n")
age = input("Напиши возраст нового чипса\n")
id_user = 1

ws.update(
    values=[[name, age]],
    range_name=f"A{id_user}:B{id_user}",
)

