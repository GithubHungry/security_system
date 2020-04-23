import myconnutils
import datetime

# connection = myconnutils.get_connection()
# sql = "describe Employee;"
# try:
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     for row in cursor:
#         print(row)
#         # for elem in row:
#         #     print(str(elem).title())
# finally:
#     # Закрыть соединение (Close connection).
#     connection.close()

from tkinter import *


def user_update():
    def update_userprofile():

        user_fio = update_entry.get()
        print(user_fio)
        if user_fio == '':
            sub_sub_root = Tk()
            sub_sub_root.title('Ошибка пользователя')
            sub_sub_root.geometry('200x200')

            up_label = Label(sub_sub_root, text='Введите корректное ФИО')
            up_btn = Button(sub_sub_root, text='OK', command=sub_sub_root.destroy)
            up_label.pack()
            up_btn.pack()

            sub_sub_root.mainloop()
        else:
            sub_sub_root = Tk()
            sub_sub_root.title('Изменение пользователя: {}'.format(user_fio))
            sub_sub_root.geometry('500x500')

            up_label = Label(sub_sub_root, text=update_entry.get())
            up_label.pack()

            sub_root.destroy()
            sub_sub_root.mainloop()

    sub_root = Tk()
    sub_root.title('Изменение существующего пользователя')
    sub_root.geometry('250x150')

    update_label = Label(sub_root, text='Введите ФИО пользователя')
    update_entry = Entry(sub_root)
    update_btn = Button(sub_root, text='Поиск пользователя', command=update_userprofile)

    update_label.pack()
    update_entry.pack()
    update_btn.pack()

    sub_root.mainloop()


def user_create():
    connection = myconnutils.get_connection()
    sql_1 = "Select * from diploma.department;"
    sql_2 = "Select * from diploma.odds;"
    departments_list = []
    odds_list = []
    try:
        cursor = connection.cursor()
        cursor.execute(sql_1)
        for row in cursor:
            departments_list.append(row[1])
        cursor.execute(sql_2)
        for row in cursor:
            odds_list.append(row[1])
    finally:
        connection.close()

    def accept_create():
        fio = entry_fio.get()
        phone = entry_phone.get()
        email = entry_email.get()
        date_of_birth = entry_date_of_birth.get()
        uuid = entry_uuid.get()
        department_choice = departments_listbox.curselection()[0] + 1  # Возвращает индекс+1
        odd_choice = odds_listbox.curselection()[0] + 1  # Возвращает индекс+1
        conn = myconnutils.get_connection()
        sql = "Insert Employee(fio,phone,email,date_of_birth,UUid,department_code,odd_code,reg_date) values ('{0}'," \
              "'{1}','{2}','{3}','{4}',{5},{6},now());".format(fio, phone, email, date_of_birth, uuid,
                                                               department_choice + 1, odd_choice + 1)
        try:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
        except:
            print('something wrong')
            conn.rollback()
        finally:
            conn.close()
        sub_root.destroy()

    sub_root = Tk()
    sub_root.title('Создание новго пользователя')
    sub_root.geometry('500x700')

    label_fio = Label(sub_root, text='Фамилия имя отчество')
    entry_fio = Entry(sub_root)

    label_phone = Label(sub_root, text='Телефон')
    entry_phone = Entry(sub_root)

    label_email = Label(sub_root, text='Email')
    entry_email = Entry(sub_root)

    label_date_of_birth = Label(sub_root, text='Дата рождения')
    entry_date_of_birth = Entry(sub_root)

    label_uuid = Label(sub_root, text='UUiD')
    entry_uuid = Entry(sub_root)

    label_department = Label(sub_root, text='Отдел')
    departments_listbox = Listbox(sub_root, width=40, selectbackground='#228B22', exportselection=0)
    scrollbar = Scrollbar(sub_root, command=departments_listbox.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    departments_listbox.config(yscrollcommand=scrollbar.set)
    for department in departments_list:
        departments_listbox.insert(END, department)

    label_odd = Label(sub_root, text='Коэффициент надбавки')
    odds_listbox = Listbox(sub_root, width=40, selectbackground='#228B22')
    for odd in odds_list:
        odds_listbox.insert(END, odd)

    btn_accept_create = Button(sub_root, text='Создать', command=accept_create)

    label_fio.pack()
    entry_fio.pack()

    label_phone.pack()
    entry_phone.pack()

    label_email.pack()
    entry_email.pack()

    label_date_of_birth.pack()
    entry_date_of_birth.pack()

    label_uuid.pack()
    entry_uuid.pack()

    label_department.pack()
    departments_listbox.pack()
    scrollbar.config(command=departments_listbox.yview)

    label_odd.pack()
    odds_listbox.pack()

    btn_accept_create.pack()

    sub_root.mainloop()


def user_auth():
    sub_root = Tk()
    sub_root.title('Аутенитификация пользователя')
    sub_root.geometry('500x500')
    btn_2 = Button(sub_root, text='test')
    btn_2.pack()
    sub_root.mainloop()


root = Tk()
root.title("Безопасность будущего")
root.geometry("300x500")

btn_auth = Button(text='Аутентификация пользователя', command=user_auth)
btn_auth.pack()

btn_create = Button(text='Создание нового пользователя', command=user_create)
btn_create.pack()

btn_update = Button(text='Изменение нового пользователя', command=user_update)
btn_update.pack()

root.mainloop()
