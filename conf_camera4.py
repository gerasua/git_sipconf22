from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
import logging
import mysql.connector as mdb
from mysql.connector import Error
from PyQt5.QtWidgets import (QApplication, QMessageBox)

# Logging and console
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(funcName)s:%(message)s')
file_handler = logging.FileHandler('error.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class updateCamera4(QDialog):
    def __init__(self, parent=None):
        super(updateCamera4, self).__init__(parent, flags=Qt.WindowCloseButtonHint)
        loadUi('conf_camera4.ui', self)
        logger.debug("Ventana actualizar Camera 4")
        self.DB_Connect()

        try:
            self.cur.execute("SELECT * FROM totalco_camaras WHERE id_camara = 4")
            self.row_authenticate = self.cur.fetchone()

            self.id = self.row_authenticate[0]

            logger.debug(f"Id: {self.id}")
            logger.debug("Usuario: {}".format(self.row_authenticate[1]))
            logger.debug(f"Password: {self.row_authenticate[2]}")
            logger.debug(f"IP: {self.row_authenticate[3]}")
            logger.debug(f"Canal: {self.row_authenticate[4]}")

            self.usuario = self.row_authenticate[1]
            self.lineUpdateUsuario.setText(str(self.usuario))

            self.password = self.row_authenticate[2]
            self.lineUpdatePassword.setText(str(self.password))

            self.ip = self.row_authenticate[3]
            self.lineUpdateIp.setText(str(self.ip))

            self.canal = self.row_authenticate[4]
            self.lineUpdateCanal.setText(str(self.canal))

        except Exception as e:
            logger.exception("Error DB: {}".format(e))

        # BOTONES
        self.btnCancelCompany.clicked.connect(self.cancelar)
        self.btnUpdateCompany.clicked.connect(self.actualizar)

    # Funciones

    def cancelar(self):
        logger.debug("Cancelar")
        self.close()

    def actualizar(self):
        logger.debug("Actualizar")
        logger.debug(f"Id: {self.id}")

        self.usuario = self.lineUpdateUsuario.displayText()
        logger.debug("Usuario: {}".format(self.usuario))

        self.password = self.lineUpdatePassword.text()
        logger.debug("Password: {}".format(self.password))

        self.ip = self.lineUpdateIp.displayText()
        logger.debug("IP: {}".format(self.ip))

        self.canal = self.lineUpdateCanal.displayText()
        logger.debug("Canal: {}".format(self.canal))

        if len(str(self.usuario)) <= 0:
            logger.debug("Esta vacio")
            QMessageBox.critical(self, "Mensaje", "El usuario no debe estar vacío.   ",
                                 QMessageBox.Ok)
            self.lineUpdateUsuario.setFocus()
            return

        if len(str(self.password)) <= 0:
            logger.debug("Esta vacio")
            QMessageBox.critical(self, "Mensaje", "El password no debe estar vacío.   ",
                                 QMessageBox.Ok)
            self.lineUpdatePassword.setFocus()
            return

        if len(str(self.ip)) <= 0:
            logger.debug("Esta vacio")
            QMessageBox.critical(self, "Mensaje", "La IP no debe estar vacío.   ",
                                 QMessageBox.Ok)
            self.lineUpdateIp.setFocus()
            return

        if len(str(self.canal)) <= 0:
            logger.debug("Esta vacio")
            QMessageBox.critical(self, "Mensaje", "El Canal no debe estar vacío.   ",
                                 QMessageBox.Ok)
            self.lineUpdateCanal.setFocus()
            return

        try:
            query = """ UPDATE totalco_camaras SET usuario = %s, Password = %s, ip= %s, canal= %s WHERE id_camara = %s """
            data = (str(self.usuario), str(self.password), str(self.ip), str(self.canal), self.id)
            self.cur.execute(query, data)
            self.conn.commit()
            QMessageBox.information(self, "Éxito", "Se agregó exitosamente", QMessageBox.Ok)
            self.hide()
            self.cur.close()
        except Exception as e:
            logger.debug("Error al actualizar: {}".format(e))


    def closeEvent(self, event):

        reply = QMessageBox.question(
            self, "Mensaje",
            "Estas seguro de cancelar?",
            QMessageBox.Close | QMessageBox.Cancel)

        if reply == QMessageBox.Close:
            logger.debug("Close")
            self.close()
        else:
            logger.debug("Cancel")
            event.ignore()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            logger.debug("Key Scape")
            self.close()

    ## DATABASE CONECCT
    def DB_Connect(self):
        try:
            self.conn = mdb.connect(host="localhost", user="root", password="P4ssw0rd", database="gcasmo")
            self.cur = self.conn.cursor()
            # self.cur = self.conn.cursor(buffered=True)
        except Exception as e:
            logger.exception("Error DB: {}".format(e))