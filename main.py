import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pyqtgraph import *
from parse.xmlParse import *
from parse.graph import *

audits_path = "F:\\networkCourse\\audits"
filenames = os.listdir(audits_path)


class MainWindow(QMainWindow):

    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi("mainwindow.ui", self)
        self.title = 'Network Audit'
        self.audits_path = "F:\\networkCourse\\audits"
        os.chdir(audits_path)
        self.filenames = os.listdir(audits_path)
        self.scan_button.clicked.connect(self.scan_network)
        self.graphs.clicked.connect(make_plot)
        self.wmi_save.clicked.connect(self.save_wmi_credentials)
        self.ssh_save.clicked.connect(self.save_ssh_credentials)

    def scan_network(self):
        if len(self.device_list) != 0:
            self.device_list.clear()
        for f in self.filenames:
            item = QListWidgetItem(f.split("-")[0])
            self.device_list.addItem(item)
            self.device_list.itemClicked.connect(self.show_device_info)

        values = make_data()

        self.os.clear()
        self.proc.clear()
        self.videocard.clear()
        self.soundcard.clear()

        self.os.insertPlainText(get_stats_str(values[0]))
        self.proc.insertPlainText(get_stats_str(values[1]))
        self.videocard.insertPlainText(get_stats_str(values[2]))
        self.soundcard.insertPlainText(get_stats_str(values[3]))

        pixmap = QPixmap("F:\\networkCourse\stats.png")
        pixmap.scaledToWidth(800)
        pixmap.scaledToHeight(600)
        self.label.setPixmap(pixmap)
        self.resize(self.width() + pixmap.width() // 2, self.height())
        self.main_tab.resize(self.width() + pixmap.width() // 2, self.height())
        self.label.resize(800, 600)
        self.show()

    def show_device_info(self, item, files=filenames, files_path=audits_path):
        for f in files:
            if f.split('-')[0] == item.text():
                sys_data, processor_data, memory_data, \
                    motherboard_data, sound_data, video_card_data, network_data = \
                    parse_client_response(files_path + '\\' + f)

                self.system_info.clear()
                self.processor_info.clear()
                self.memory_info.clear()
                self.sound_info.clear()
                self.graphics_info.clear()

                self.system_info.insertPlainText(sys_data)
                self.processor_info.insertPlainText(processor_data)
                self.memory_info.insertPlainText(memory_data)
                self.sound_info.insertPlainText(sound_data)
                self.graphics_info.insertPlainText(video_card_data)

    def save_ssh_credentials(self):
        mode = 'w'
        if(os.path.exists("F:\\networkCourse\\credentials.txt")):
            mode = 'a+'
        credentialsFile = open("F:\\networkCourse\\credentials.txt", mode)
        login = self.ssh_login.toPlainText()
        password = self.ssh_password.toPlainText()
        credentialsFile.write("ssh\n" + login + '\n' + password + '\n')
        self.ssh_login.clear()
        self.ssh.password.clear()
        credentialsFile.close()

    def save_wmi_credentials(self):
        mode = 'w'
        if(os.path.exists("F:\\networkCourse\\credentials.txt")):
            mode = 'a+'
        credentialsFile = open("F:\\networkCourse\\credentials.txt", mode)
        login = self.wmi_login.toPlainText()
        password = self.wmi_password.toPlainText()
        credentialsFile.write("wmi\n" + login + '\n' + password + '\n')
        self.wmi_login.clear()
        self.wmi_password.clear()
        credentialsFile.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())