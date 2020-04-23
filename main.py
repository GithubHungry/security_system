import myconnutils
from tkinter import *
from tkinter import messagebox


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


def user_update():
    def update_userprofile():

        def update_confirm():
            up_fio = up_fio_entry.get()
            up_phone = up_phone_entry.get()
            up_email = up_email_entry.get()
            up_date_of_birth = up_date_of_birth_entry.get()
            up_uuid = up_uuid_entry.get()
            up_department_choice = up_departments_listbox.curselection()[0] + 1  # Возвращает индекс+1
            up_odd_choice = up_odds_listbox.curselection()[0] + 1  # Возвращает индекс+1

            connec = myconnutils.get_connection()
            sql_3 = "UPDATE diploma.employee SET fio='{0}',phone='{1}',email='{2}',date_of_birth='{3}',UUid='{4}'," \
                    "department_code={5},odd_code={6} WHERE employee.fio='{7}';".format(up_fio, up_phone, up_email,
                                                                                        up_date_of_birth, up_uuid,
                                                                                        up_department_choice,
                                                                                        up_odd_choice, user_fio)
            try:
                curs = connec.cursor()
                curs.execute(sql_3)
                connec.commit()
                messagebox.showinfo("Успех!", message='Пользователь успешно обновлен!')
            except:
                print('something wrong')
                connec.rollback()
            finally:

                connec.close()
            sub_sub_root.destroy()

        user_fio = update_entry.get()

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
            sub_sub_root.geometry('500x700')
            employee_info = ''

            connection = myconnutils.get_connection()
            sql = "Select * from diploma.employee where employee.fio='{}';".format(update_entry.get())
            sql_1 = "Select * from diploma.department;"
            sql_2 = "Select * from diploma.odds;"
            departments_list = []
            odds_list = []

            try:
                cursor = connection.cursor()
                cursor.execute(sql)
                for row in cursor:
                    employee_info = row
                cursor = connection.cursor()
                cursor.execute(sql_1)
                for row in cursor:
                    departments_list.append(row[1])
                cursor.execute(sql_2)
                for row in cursor:
                    odds_list.append(row[1])
            finally:
                # Закрыть соединение (Close connection).
                connection.close()

            up_fio_label = Label(sub_sub_root, text='Новое ФИО')
            up_fio_entry = Entry(sub_sub_root)
            up_fio_entry.insert(0, employee_info[1])

            up_phone_label = Label(sub_sub_root, text='Новый Телефон')
            up_phone_entry = Entry(sub_sub_root)
            up_phone_entry.insert(0, employee_info[2])

            up_email_label = Label(sub_sub_root, text='Новый Email')
            up_email_entry = Entry(sub_sub_root)
            up_email_entry.insert(0, employee_info[3])

            up_date_of_birth_label = Label(sub_sub_root, text='Новая Дата рождения')
            up_date_of_birth_entry = Entry(sub_sub_root)
            up_date_of_birth_entry.insert(0, employee_info[4])

            up_uuid_label = Label(sub_sub_root, text='UUiD')
            up_uuid_entry = Entry(sub_sub_root)
            up_uuid_entry.insert(0, employee_info[5])

            up_department_label = Label(sub_sub_root, text='Отдел')
            up_departments_listbox = Listbox(sub_sub_root, width=40, selectbackground='#228B22', exportselection=0)
            scrollbar = Scrollbar(sub_sub_root, command=up_departments_listbox.yview)
            scrollbar.pack(side=RIGHT, fill=Y)
            up_departments_listbox.config(yscrollcommand=scrollbar.set)
            for department in departments_list:
                up_departments_listbox.insert(END, department)

            up_odd_label = Label(sub_sub_root, text='Коэффициент надбавки')
            up_odds_listbox = Listbox(sub_sub_root, width=40, selectbackground='#228B22')
            for odd in odds_list:
                up_odds_listbox.insert(END, odd)

            up_btn_confirm = Button(sub_sub_root, text='Изменить пользователя', command=update_confirm)

            up_fio_label.pack()
            up_fio_entry.pack()

            up_phone_label.pack()
            up_phone_entry.pack()

            up_email_label.pack()
            up_email_entry.pack()

            up_date_of_birth_label.pack()
            up_date_of_birth_entry.pack()

            up_uuid_label.pack()
            up_uuid_entry.pack()

            up_department_label.pack()
            up_departments_listbox.pack()
            scrollbar.config(command=up_departments_listbox.yview)

            up_odd_label.pack()
            up_odds_listbox.pack()

            up_btn_confirm.pack()

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
            messagebox.showinfo("Успех!", message='Пользователь успешно создан!')
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

btn_update = Button(text='Изменение данных пользователя', command=user_update)
btn_update.pack()

root.mainloop()
