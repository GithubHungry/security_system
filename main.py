import myconnutils
import datetime
from tkinter import *
from tkinter import messagebox
import smtplib


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

def email_send_back(door):
    content = 'Несанкционированная попытка доступа но объект! Просьба проверить точку доступа № {0}'.format(
        door).encode('utf-8')
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('shopmanage7@gmail.com', 'M2t8zUmPQg')
    mail.sendmail('shopmanage7@gmail.com', 'bardiervadim97@gmail.com', content)
    mail.close()


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
            up_fio_entry = Entry(sub_sub_root, justify=CENTER)
            up_fio_entry.insert(0, employee_info[1])

            up_phone_label = Label(sub_sub_root, text='Новый Телефон')
            up_phone_entry = Entry(sub_sub_root, justify=CENTER)
            up_phone_entry.insert(0, employee_info[2])

            up_email_label = Label(sub_sub_root, text='Новый Email')
            up_email_entry = Entry(sub_sub_root, justify=CENTER)
            up_email_entry.insert(0, employee_info[3])

            up_date_of_birth_label = Label(sub_sub_root, text='Новая Дата рождения')
            up_date_of_birth_entry = Entry(sub_sub_root, justify=CENTER)
            up_date_of_birth_entry.insert(0, employee_info[4])

            up_uuid_label = Label(sub_sub_root, text='UUiD')
            up_uuid_entry = Entry(sub_sub_root, justify=CENTER)
            up_uuid_entry.insert(0, employee_info[5])

            up_department_label = Label(sub_sub_root, text='Отдел')
            up_departments_listbox = Listbox(sub_sub_root, width=40, selectbackground='#228B22', exportselection=0)
            scrollbar = Scrollbar(sub_sub_root, command=up_departments_listbox.yview)
            scrollbar.pack(side=RIGHT, fill=Y)
            up_departments_listbox.config(yscrollcommand=scrollbar.set)
            for department in departments_list:
                up_departments_listbox.insert(END, department)

            up_odd_label = Label(sub_sub_root, text='Коэффициент должности')
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
    entry_fio = Entry(sub_root, justify=CENTER)

    label_phone = Label(sub_root, text='Телефон')
    entry_phone = Entry(sub_root, justify=CENTER)

    label_email = Label(sub_root, text='Email')
    entry_email = Entry(sub_root, justify=CENTER)

    label_date_of_birth = Label(sub_root, text='Дата рождения')
    entry_date_of_birth = Entry(sub_root, justify=CENTER)

    label_uuid = Label(sub_root, text='UUiD')
    entry_uuid = Entry(sub_root, justify=CENTER)

    label_department = Label(sub_root, text='Отдел')
    departments_listbox = Listbox(sub_root, width=40, selectbackground='#228B22', exportselection=0)
    scrollbar = Scrollbar(sub_root, command=departments_listbox.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    departments_listbox.config(yscrollcommand=scrollbar.set)
    for department in departments_list:
        departments_listbox.insert(END, department)

    label_odd = Label(sub_root, text='Коэффициент должности')
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
    sub_auth_root = Tk()
    sub_auth_root.title('Аутенитификация пользователя')
    sub_auth_root.geometry('500x500')

    users = []
    points = []
    uuids = []
    users_uuids = []

    connection = myconnutils.get_connection()
    sql_1 = "Select employee.fio,employee.UUid from employee order by employee.fio;"
    sql_2 = "Select points.name from points;"
    try:
        cursor = connection.cursor()
        cursor.execute(sql_1)
        for row in cursor:
            users_uuids.append(row)
            users.append(row[0])
            uuids.append(row[1])
        users.append('-----')
        uuids.append('af89ac97-b14b-4660-a382-93b26ddf877d')
        uuids.append('76488e31-5707-4603-b571-7f0e1615f87c')
        uuids.append('b5f711e3-153b-4df4-b012-ab5ca2bf2f04')

        cursor.execute(sql_2)
        for row in cursor:
            points.append(row[0])
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

    variable = StringVar(sub_auth_root)
    variable.set(users[-1])  # default value

    fio_label = Label(sub_auth_root, text='Выберите пропуск который хотите приложить')
    fio_label.pack()

    def setter_auth(selection):
        variable.set(selection)

    w = OptionMenu(*(sub_auth_root, variable) + tuple(users, ), command=setter_auth)
    w.pack()

    def submit():
        btn_submit.pack_forget()
        w.pack_forget()

        sub_entry = Entry(sub_auth_root, justify=CENTER, width=35)
        sub_entry.insert(0, variable.get())
        sub_entry.config(state=DISABLED)
        sub_entry.pack()

        label_uuid_auth = Label(sub_auth_root, text='UUiD')
        label_uuid_auth.pack()
        if variable.get() == '-----':
            entry_uuid_auth = Entry(sub_auth_root, justify=CENTER, width=35)
            entry_uuid_auth.insert(0, 'Введите UUiD')
            entry_uuid_auth.pack()
        else:
            entry_uuid_auth = Entry(sub_auth_root, justify=CENTER, width=35)
            for tup in users_uuids:
                if tup[0] == variable.get():
                    entry_uuid_auth.insert(0, tup[1])
                    entry_uuid_auth.config(state=DISABLED)
                    entry_uuid_auth.pack()

        point_label = Label(sub_auth_root, text='Выберите точку прохода')
        point_label.pack()

        door = IntVar(sub_auth_root)
        door.set(1)

        door_one_radio = Radiobutton(sub_auth_root, text=points[0], variable=door, value=1)
        door_one_radio.pack()

        door_two_radio = Radiobutton(sub_auth_root, text=points[1], variable=door, value=2)
        door_two_radio.pack()

        enter_label = Label(sub_auth_root, text='Выберите тип прохода')
        enter_label.pack()

        enter = StringVar(sub_auth_root)
        enter.set('Вход ')

        enter_one_radio = Radiobutton(sub_auth_root, text='Вход', variable=enter, value='Вход')
        enter_one_radio.pack()

        enter_two_radio = Radiobutton(sub_auth_root, text='Выход', variable=enter, value='Выход')
        enter_two_radio.pack()

        def ok():
            info = []
            c = myconnutils.get_connection()
            sql = "Select * from diploma.employee;"
            try:
                curs = c.cursor()
                curs.execute(sql)
                for user_row in curs:
                    info.append(user_row)
            finally:
                # Закрыть соединение (Close connection).
                c.close()

            current_employee = ''

            for employee in info:
                if entry_uuid_auth.get() in employee:
                    current_employee = employee
                    break
                else:
                    current_employee = (
                        'Неизвестно', 'Неизвестно', 'Неизвестно', 'Неизвестно', 'Неизвестно',
                        entry_uuid_auth.get(), 'Неизвестно', 'Неизвестно', 'Неизвестно', 0)

            print("value user is", variable.get())
            print('uuid is ', entry_uuid_auth.get())
            print("point is ", door.get())
            print('enter is :', enter.get())
            print(current_employee)

            ##########################

            # Вход
            if current_employee[9] + 1 > 1 and current_employee[0] != 'Неизвестно' and enter.get() == 'Вход':  ########
                text = 'Пользователь с данным пропуском уже вошел!'
                messagebox.showerror("Доступ отказан!", message=text)
                sub_auth_root.destroy()
            elif variable.get() != '-----' and current_employee[9] + 1 < 2 and current_employee[0] != 'Неизвестно' \
                    and enter.get() == 'Вход':
                db_conn = myconnutils.get_connection()
                sql_entry_check = "update diploma.employee set entry_check = entry_check + 1 " \
                                  "where employee.fio='{0}';".format(variable.get())
                print(sql_entry_check)
                try:
                    db_curs = db_conn.cursor()
                    db_curs.execute(sql_entry_check)
                    db_conn.commit()
                finally:
                    # Закрыть соединение (Close connection).
                    db_conn.close()

            ##########################
            # Выход
            if enter.get() == 'Выход' and current_employee[0] != 'Неизвестно' and current_employee[9] - 1 < 0:
                text = 'Пользователь с данным пропуском уже вышел!'
                messagebox.showerror("Доступ отказан!", message=text)
                sub_auth_root.destroy()
            elif enter.get() == 'Выход' and variable.get() != '-----' and current_employee[9] - 1 == 0:
                db_conn = myconnutils.get_connection()
                sql_entry_check = "update diploma.employee set entry_check = entry_check - 1 " \
                                  "where employee.fio='{0}';".format(variable.get())
                print(sql_entry_check)
                try:
                    db_curs = db_conn.cursor()
                    db_curs.execute(sql_entry_check)
                    db_conn.commit()
                finally:
                    # Закрыть соединение (Close connection).
                    db_conn.close()

            ##########################

            if entry_uuid_auth.get() in uuids and sub_entry.get() != '-----':
                c = myconnutils.get_connection()
                sql_ins = "Insert into diploma.log(entry_type,employee_id, uuid ,dep_id, point_id, reg_date)" \
                          " values ('{0}',{1},'{2}',{3},{4},now());".format(enter.get(), current_employee[0],
                                                                            entry_uuid_auth.get(),
                                                                            current_employee[6], door.get())
                try:
                    curs = c.cursor()
                    curs.execute(sql_ins)
                    c.commit()
                    if enter.get() == 'Вход':
                        if datetime.datetime.now().time().hour > 8:

                            co = myconnutils.get_connection()
                            sql_late = "UPDATE diploma.employee SET late_odd = late_odd - 0.05 " \
                                       "WHERE employee.id_employee = {0};".format(current_employee[0])
                            print(sql_late)
                            try:
                                pass
                                curs = co.cursor()
                                curs.execute(sql_late)
                                co.commit()
                            finally:
                                # Закрыть соединение (Close connection).
                                co.close()

                            delta_hour = datetime.datetime.now().time().hour - 8
                            delta_min = datetime.datetime.now().time().minute - 0
                            text = 'Доступ разрешен, сотрудник, добро пожаловать! Время прохода {0},' \
                                   ' вы опоздали на {1} часов, {2} минут,' \
                                   ' это негативно отразится на вашей заработной плате!'.format(
                                    datetime.datetime.now().time(),
                                    delta_hour, delta_min)
                        else:
                            co = myconnutils.get_connection()
                            sql_late = "UPDATE diploma.employee SET late_odd = late_odd + 0.02 " \
                                       "WHERE employee.id_employee = {0};".format(current_employee[0])
                            print(sql_late)
                            try:
                                curs = co.cursor()
                                curs.execute(sql_late)
                                co.commit()
                            finally:
                                # Закрыть соединение (Close connection).
                                co.close()
                            text = 'Доступ разрешен, сотрудник, вы пришли вовремя, удачного рабочего дня!'
                    else:
                        text = 'Доступ разрешен, сотрудник, досвидания! Время прохода {0}'.format(
                            datetime.datetime.now().time())
                    messagebox.showinfo("Доступ разрешен!", message=text)
                    sub_auth_root.destroy()

                finally:
                    # Закрыть соединение (Close connection).
                    c.close()

            elif entry_uuid_auth.get() in uuids and sub_entry.get() == '-----':
                connec = myconnutils.get_connection()
                sql_ins = "Insert into diploma.log(entry_type,employee_id, uuid ,dep_id, point_id, reg_date)" \
                          " values ('{0}',{1},'{2}',{3},{4},now());".format(enter.get(), 0, entry_uuid_auth.get(),
                                                                            0, door.get())
                try:
                    curs = connec.cursor()
                    curs.execute(sql_ins)
                    connec.commit()
                    if enter.get() == 'Вход':
                        text = 'Доступ разрешен, гость, добро пожаловать! Время прохода {0}'.format(
                            datetime.datetime.now().time())
                    else:
                        text = 'Доступ разрешен, гость, досвидания! Время прохода {0}'.format(
                            datetime.datetime.now().time())
                    messagebox.showinfo("Доступ разрешен!", message=text)
                    sub_auth_root.destroy()
                finally:
                    # Закрыть соединение (Close connection).
                    connec.close()
            else:
                text = 'Пропуск не действителен, оставайтесь на месте до прихода администратора!'
                messagebox.showerror("Доступ отказан!", message=text)
                error_text = int(door.get())
                email_send_back(error_text)
                sub_auth_root.destroy()

        button = Button(sub_auth_root, text="OK", command=ok)
        button.pack()

    btn_submit = Button(sub_auth_root, text='Submit', command=submit)
    btn_submit.pack()

    # test stuff

    sub_auth_root.mainloop()


root = Tk()
root.title("Безопасность будущего")
root.geometry("300x500")

btn_auth = Button(text='Аутентификация пользователя', command=user_auth)
btn_auth.pack()

btn_create = Button(text='Создание нового пользователя', command=user_create)
btn_create.pack()

btn_update = Button(text='Изменение данных пользователя', command=user_update)
btn_update.pack()

# btn_send = Button(text='Отправить сообщение', command=email_send)
# btn_send.pack()

root.mainloop()
