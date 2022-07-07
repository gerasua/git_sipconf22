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


class updateCompany(QDialog):
    def __init__(self, parent=None):
        super(updateCompany, self).__init__(parent, flags=Qt.WindowCloseButtonHint)
        loadUi('update_company.ui', self)
        logger.debug("Ventana actualizar")
        self.DB_Connect()

        try:
            self.cur.execute("SELECT * FROM totalco_info_gral")
            self.row_authenticate = self.cur.fetchone()
            logger.debug("Company: {}".format(self.row_authenticate[2]))
            self.company = self.row_authenticate[2]
            self.lineUpdateCompany.setText(str(self.company))
            self.id = self.row_authenticate[0]

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
        self.itemUpdate = self.lineUpdateCompany.displayText()
        logger.debug("Nombre: {}".format(self.itemUpdate))

        if self.itemUpdate:
            logger.debug("No esta vacío")
            try:
                query = """ UPDATE totalco_info_gral SET empresa = %s WHERE id_info_gral = %s """
                data = (str(self.itemUpdate), self.id)
                self.cur.execute(query, data)
                self.conn.commit()
                QMessageBox.information(self, "Éxito", "Se agregó exitosamente", QMessageBox.Ok)
                self.hide()
                self.cur.close()
            except Exception as e:
                logger.debug("Error al insertar: {}".format(e))
        else:
            logger.debug("Vacio")
            QMessageBox.critical(self, "Mensaje", "Debes llenar el campo de Nombre.   ", QMessageBox.Ok)
            self.lineUpdateCompany.setFocus()

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
        except Exception as e:
            logger.exception("Error DB: {}".format(e))