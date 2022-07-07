from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
import logging
import mysql.connector as mdb
from mysql.connector import Error
from PyQt5.QtWidgets import (QApplication, QMessageBox)
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIntValidator

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


class actualizaContra(QDialog):
    def __init__(self, idItem, nombreItem, parent=None):
        super(actualizaContra, self).__init__(parent, flags=Qt.WindowCloseButtonHint)
        loadUi('actualiza_contra.ui', self)
        logger.debug("Actualizar contraseña de usuario")
        self.DB_Connect()
        logger.debug("Id: {}".format(idItem))
        self.id = idItem
        logger.debug("Nombre Item: {}".format(nombreItem))
        # BOTONES
        self.btnCancelar.clicked.connect(self.cancelar)
        self.btnAgregar.clicked.connect(self.agregar)

        try:
            self.cur.execute("SELECT * FROM usuarios WHERE id_usuario='" + idItem + "'")
            self.row = self.cur.fetchone()
            self.usuario = self.row[1]
            self.nivel = self.row[3]
            self.nombrecompleto = self.row[5]
        except Exception as e:
            logger.debug(f"Error de query: {e}")

        self.lineEditUsuario.setText(str(self.usuario))

        if int(self.nivel) == 1:
            self.niveldeusuario = "Pesador"
            self.lineNivel.setText(str(self.niveldeusuario))
        elif int(self.nivel) == 2:
            self.niveldeusuario = "Supervisor"
            self.lineNivel.setText(str(self.niveldeusuario))
        elif int(self.nivel) == 3:
            self.niveldeusuario = "Administrador"
            self.lineNivel.setText(str(self.niveldeusuario))
        else:
            raise Exception("Error en el nivel de usuario")

        self.lineEditNombreCompleto.setText(str(self.nombrecompleto))

    # Funciones

    def cancelar(self):
        logger.debug("Cancelar")
        self.close()

    def agregar(self):
        logger.debug("Actualizar")

        self.password = self.lineEditPassword.text()
        logger.debug(f"Password: {self.password}")

        self.password2 = self.lineEditPassword2.text()
        logger.debug(f"Password2: {self.password2}")

        if len(str(self.password)) <= 0:
            logger.debug("Esta vacio")
            QMessageBox.critical(self, "Mensaje", "El password no debe estar vacío.   ",
                                 QMessageBox.Ok)
            self.lineEditPassword.setFocus()
            return

        if len(str(self.password2)) <= 0:
            logger.debug("Esta vacio")
            QMessageBox.critical(self, "Mensaje", "Debes repetir el password.   ",
                                 QMessageBox.Ok)
            self.lineEditPassword.setFocus()
            return

        if self.password != self.password2:
            logger.debug("No son iguales")
            QMessageBox.critical(self, "Mensaje", "El password no coincide.   ",
                                 QMessageBox.Ok)
            self.lineEditPassword2.setFocus()

        else:
            logger.debug("Actualiza contraseña")
            try:
                query = """ UPDATE usuarios SET password = %s WHERE id_usuario = %s """
                data = (str(self.password), self.id)
                self.cur.execute(query, data)
                self.conn.commit()
                QMessageBox.information(self, "Éxito", "Se cambió exitosamente", QMessageBox.Ok)
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
        except Exception as e:
            logger.exception("Error DB: {}".format(e))