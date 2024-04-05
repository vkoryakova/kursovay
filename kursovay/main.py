from PyQt6.QtWidgets import (QApplication,QMainWindow,QMessageBox, QListWidgetItem,
                             QMenu, QDialog, QVBoxLayout, QComboBox, QDateEdit, QLabel,  QPushButton)
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import QDate
from kurs import Ui_Form
from kurs3 import Ui_AdminWindow
from untitled import Ui_Registerclien
from kurs5 import Ui_ViewWindow
import datetime

import sqlite3
connection = sqlite3.connect("pc_book.db")
cursor = connection.cursor()

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.enter)

    def enter(self):
       login = self.ui.lineEdit.text()
       password = self.ui.lineEdit_2.text()
       if login == '':
           msg = QMessageBox()

           msg.setWindowTitle('Ошибка входа')
           msg.setText('Введите логин!')
           msg.setStyleSheet('color: black; background-color: violet ;')
           msg.exec()



       elif password == '':
           msg = QMessageBox()

           msg.setWindowTitle('Ошибка входа')
           msg.setText('Введите пароль!')
           msg.setStyleSheet('color: black; background-color: violet ;')
           msg.exec()

       else:
           statement = f"SELECT id from admin WHERE login='{login}' AND password = '{password}';"
           cursor.execute(statement)
           if not cursor.fetchone():  # Пустой результат принимает значение false
               st2 = f"SELECT id from admin WHERE login='{login}' AND password = '{password}';"
               cursor.execute(st2)
               if not cursor.fetchone():
                   msg = QMessageBox()

                   msg.setWindowTitle('Ошибка входа')
                   msg.setText('Неверно введены логин или пароль!!')
                   msg.setStyleSheet('color: black; background-color: violet ;')
                   msg.exec()
                   self.ui.lineEdit.setText('')
                   self.ui.lineEdit_2.setText('')

               else:
                   # Открытие нового окна после успешной авторизации
                   self.openMainWindow()
           else:
               self.openMainWindow()

    def openMainWindow(self):
        self.admin_window = admin()
        self.admin_window.show()

class admin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.hide)
        self.ui.comboBox_2.currentIndexChanged.connect(self.handleSelection)
        self.ui.comboBox.currentIndexChanged.connect(self.updateStatusLabels)
        current_date = datetime.datetime.now()
        self.ui.dateEdit.setDate(current_date.date())
        self.ui.dateEdit.setCalendarPopup(True)
        self.ui.dateEdit.dateChanged.connect(self.updateStatusLabels)
        self.populateTimeComboBox()


    def populateTimeComboBox(self):
        connect = sqlite3.connect('pc_book.db')
        cursor = connect.cursor()
        cursor.execute("SELECT name FROM time")
        time_slots = cursor.fetchall()
        for time_slot in time_slots:
            self.ui.comboBox.addItem(time_slot[0])
        connect.close()

    def updateStatusLabels(self):
        selected_date = self.ui.dateEdit.date().toString("dd-MM-yyyy")
        selected_time = self.ui.comboBox.currentText()
        status_labels = [self.ui.label_6, self.ui.label_7,
                         self.ui.label_8, self.ui.label_9]
        query = """
                    SELECT pc.name, IFNULL(status.name, 'Free') as status
                    FROM pc
                    LEFT JOIN booking ON pc.id = booking.id_pc 
                                     AND booking.date = ? 
                                     AND booking.id_time = 
                                         (SELECT id from time where name = ?)
                    LEFT JOIN status ON booking.id_status = status.id
                """
        connect = sqlite3.connect('pc_book.db')
        cursor = connect.cursor()
        cursor.execute(query, (selected_date, selected_time))
        results = cursor.fetchall()

        # обновление статуса на label
        for idx, (pc_name, status) in enumerate(results):
            if idx < len(status_labels):
                status_labels[idx].setText(f"{pc_name}: {status}")


        connect.close()


    def handleSelection(self, index):
        if index == 0:  # регистрация
            self.openRegisterClient()
        elif index == 1:  # просмотр
            self.openViewUserData()


    def openRegisterClient(self):
        self.register_window = registrasia()
        self.register_window.show()

    def openViewUserData(self):
        self.view_window = view()
        self.view_window.show()

class view(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ViewWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.hide)
        self.loadBookingData()
        self.ui.listWidget.itemDoubleClicked.connect(self.on_booking_double_clicked)

    def on_booking_double_clicked(self):
        try:
            booking_id = self.get_selected_booking_id()
            if booking_id:
                menu = QMenu(self)
                delete_action = menu.addAction("Удалить запись")

                edit_action = menu.addAction("Изменить запись")

                action = menu.exec(QCursor.pos())

                if action == delete_action:
                    self.delete_booking(booking_id)
                elif action == edit_action:
                    self.edit_booking(booking_id)
        except Exception as e:
            print("An error occurred:", e)

    def get_selected_booking_id(self):
        item = self.ui.listWidget.currentItem()
        if item:
            content = item.text()
            booking_id = content.split(",")[0].split(":")[1].strip()  # Предполагаем, что ID указан первым
            return int(booking_id)
        return None

    def delete_booking(self, id):
        message_box = QMessageBox(self)
        message_box.setWindowTitle('Удаление брони')
        message_box.setText('Вы уверены, что хотите удалить бронирование?')
        message_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        message_box.setDefaultButton(QMessageBox.StandardButton.No)
        message_box.setStyleSheet('color: black; background-color: violet ;')

        reply = message_box.exec()

        if reply == QMessageBox.StandardButton.Yes:
            connect = sqlite3.connect('pc_book.db')
            cursor = connect.cursor()

            try:
                cursor.execute('DELETE FROM booking WHERE id = ?', (id,))
                connect.commit()
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                connect.close()

            self.loadBookingData()

    def edit_booking(self, booking_id):
        # Создаем и показываем диалоговое окно редактирования
        edit_dialog = EditBookingDialog(booking_id, self)
        if edit_dialog.exec() == QDialog.DialogCode.Accepted:
            self.loadBookingData()  # Обновление данных после успешного редактирования

    def loadBookingData(self):
        connect = sqlite3.connect('pc_book.db')
        cursor = connect.cursor()

        cursor.execute('''
            SELECT booking.id, booking.fio, booking.phone, booking.email, pc.name, booking.date, time.name
            FROM booking
            JOIN pc ON booking.id_pc = pc.id
            JOIN time ON booking.id_time = time.id
        ''')
        bookings = cursor.fetchall()

        connect.close()

        self.ui.listWidget.clear()

        for booking in bookings:
            booking_info = (
                f"Booking ID: {booking[0]},\n"
                f"Name: {booking[1]}, Phone: {booking[2]},\n"
                f"Email: {booking[3]}, PC: {booking[4]},\n"
                f"Date: {booking[5]}, Time Slot: {booking[6]}"
            )
            self.ui.listWidget.addItem(QListWidgetItem(booking_info))

class EditBookingDialog(QDialog):
    def __init__(self, booking_id, parent=None):
        super().__init__(parent)
        self.booking_id = booking_id
        self.initUI()

        self.loadPcData()
        self.loadTimeData()
        self.loadCurrentBookingData()

    def initUI(self):
        self.setWindowTitle('Edit Booking')

        layout = QVBoxLayout(self)

        # создание Labels, ComboBoxes, and DateEdit
        self.pcLabel = QLabel('Computer:')
        self.pcLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.pcComboBox = QComboBox()
        self.pcComboBox.setStyleSheet("color: rgb(255, 255, 255);")

        self.timeLabel = QLabel('Time Slot:')
        self.timeLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.timeComboBox = QComboBox()
        self.timeComboBox.setStyleSheet("color: rgb(255, 255, 255);")

        self.dateLabel = QLabel('Date:')
        self.dateLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.dateEdit = QDateEdit()
        self.dateEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.dateEdit.setCalendarPopup(True)

        self.updateButton = QPushButton('Update')
        self.updateButton.clicked.connect(self.updateBooking)

        # Добавление виджетов в окно
        layout.addWidget(self.pcLabel)
        layout.addWidget(self.pcComboBox)
        layout.addWidget(self.timeLabel)
        layout.addWidget(self.timeComboBox)
        layout.addWidget(self.dateLabel)
        layout.addWidget(self.dateEdit)
        layout.addWidget(self.updateButton)

        self.setLayout(layout)

    def loadPcData(self):
        # Загрузка данных из таблицы pc
        connect = sqlite3.connect('pc_book.db')
        cursor = connect.cursor()
        cursor.execute('SELECT id, name FROM pc')
        pcs = cursor.fetchall()
        connect.close()

        for pc in pcs:
            self.pcComboBox.addItem(pc[1], pc[0])

    def loadTimeData(self):
        # Загрузка данных из таблицы time
        connect = sqlite3.connect('pc_book.db')
        cursor = connect.cursor()
        cursor.execute('SELECT id, name FROM time')
        times = cursor.fetchall()
        connect.close()

        for time_slot in times:
            self.timeComboBox.addItem(time_slot[1], time_slot[0])

    def loadCurrentBookingData(self):
        # Загрузка текущих данных о брони из таблицы booking
        connect = sqlite3.connect('pc_book.db')
        cursor = connect.cursor()
        cursor.execute('SELECT id, id_pc, id_time, date FROM booking WHERE id = ?', (self.booking_id,))
        booking = cursor.fetchone()
        connect.close()

        if booking:
            pc_index = self.pcComboBox.findData(booking[1])
            self.pcComboBox.setCurrentIndex(pc_index)

            time_index = self.timeComboBox.findData(booking[2])
            self.timeComboBox.setCurrentIndex(time_index)

            booking_date = QDate.fromString(booking[3], "dd-MM-yyyy")

            # Устанавливаем дату в виджет QDateEdit
            self.dateEdit.setDate(booking_date)

    def updateBooking(self):
        selected_pc_id = self.pcComboBox.currentData()
        selected_time_id = self.timeComboBox.currentData()
        selected_date = self.dateEdit.date().toString("dd-MM-yyyy")

        # Проверка наличия уже существующей брони в базе данных
        connect = sqlite3.connect('pc_book.db')
        cursor = connect.cursor()
        cursor.execute('''
            SELECT id FROM booking WHERE id_pc = ? AND id_time = ? AND date = ?
        ''', (selected_pc_id, selected_time_id, selected_date))
        existing_booking = cursor.fetchone()
        connect.close()

        if existing_booking is not None:
            msg1 = QMessageBox()
            msg1.setWindowTitle('Ошибка')
            msg1.setText('Этот компьютер уже забронирован на выбранную дату и время.')
            msg1.setStyleSheet("color: black; background-color: violet;")
            msg1.exec()
            # QMessageBox.critical(self, 'Ошибка', 'Этот компьютер уже забронирован на выбранную дату и время.')
        else:
            # Обновление данных о бронировании в таблице booking
            connect = sqlite3.connect('pc_book.db')
            cursor = connect.cursor()
            cursor.execute('''
                UPDATE booking SET
                    id_pc = ?,
                    id_time = ?,
                    date = ?
                WHERE id = ?
            ''', (selected_pc_id, selected_time_id, selected_date, self.booking_id))
            connect.commit()
            connect.close()
            self.accept()  # Закрыть диалоговое окно


class registrasia(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Registerclien()
        self.ui.setupUi(self)
        current_date = datetime.datetime.now()
        self.ui.dateEdit.setDate(current_date.date())
        self.ui.dateEdit.setCalendarPopup(True)

        self.loadTimeSlots()
        self.ui.pushButton.clicked.connect(self.registracia)
        self.ui.pushButton_2.clicked.connect(self.hide)

    def loadTimeSlots(self):
        cursor.execute('SELECT id, name FROM time')
        for time_id, time_name in cursor.fetchall():
            self.ui.comboBox.addItem(time_name, time_id)

    def registracia(self):
        fio = self.ui.lineEdit_3.text()
        phone = self.ui.lineEdit_4.text()
        email = self.ui.lineEdit_5.text()
        pc = self.ui.lineEdit_6.text()
        date = self.ui.dateEdit.date().toString('dd-MM-yyyy')
        id_time = self.ui.comboBox.currentData()
        busy_status_id = 2
        free_status_id = 1
        if not (fio and phone and email and pc and date):
            msg = QMessageBox()
            msg.setWindowTitle('Ошибка регистрации')
            msg.setText('Пожалуйста, заполните все поля!')
            msg.setStyleSheet("color: black; background-color: violet;")
            msg.exec()
            return

            # Проверка на существующее бронирование
        try:
            cursor.execute("SELECT COUNT(*) FROM booking WHERE date=? AND id_time=? AND id_pc=?",
                           (date, id_time, pc))
            booking_exists = cursor.fetchone()[0] > 0
            if booking_exists:
                msg = QMessageBox()
                msg.setWindowTitle('Ошибка регистрации')
                msg.setText('Выбранное время уже занято для данного компьютера.')
                msg.setStyleSheet("color: black; background-color: violet;")
                # QMessageBox().warning(self, 'Ошибка регистрации', 'Выбранное время уже занято для данного компьютера.')
                msg.exec()
                return

            # Проверяем статус компьютера
            cursor.execute("SELECT id_status FROM booking WHERE date=? AND id_pc=?", (date, pc))
            result = cursor.fetchone()
            pc_status = result[0] if result else free_status_id

            if pc_status == busy_status_id:
                msg = QMessageBox()
                msg.setWindowTitle('Ошибка регистрации')
                msg.setText('Компьютер уже занят.')
                msg.setStyleSheet("color: black; background-color: violet;")
                # QMessageBox.warning(self, 'Ошибка регистрации', 'Компьютер уже занят.')
                msg.exec()
                return

            # Вставка нового бронирования со статусом "занят"
            cursor.execute(
                "INSERT INTO booking (fio, phone, email, id_pc, date, id_time, id_status) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (fio, phone, email, pc, date, id_time, busy_status_id)
            )
            connection.commit()  # Сохраняем изменения в базе данных
            msg = QMessageBox()
            msg.setWindowTitle('Успешная регистрация')
            msg.setText('Регистрация успешно выполнена!')
            msg.setStyleSheet("color: black; background-color: violet;")
            msg.exec()
            # QMessageBox.information(self, 'Успешная регистрация', 'Регистрация успешно выполнена!')
            self.hide()
        except Exception as e:
            QMessageBox.warning(self, 'Ошибка регистрации', f'Ошибка при сохранении данных: {e}')


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    r_window = registrasia()
    v_window = view()
    a_window = admin()
    window.show()
    app.exec()
connection.commit()
connection.close()