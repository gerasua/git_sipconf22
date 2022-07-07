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


class agregarUsuario(QDialog):
    def __init__(self, parent=None):
        super(agregarUsuario, self).__init__(parent, flags=Qt.WindowCloseButtonHint)
        loadUi('agregar_usuario.ui', self)
        logger.debug("Ventana agregar Usuario")
        self.DB_Connect()

        # BOTONES
        self.btnCancelar.clicked.connect(self.cancelar)
        self.btnAgregar.clicked.connect(self.agregar)

        # NIVELES DE USUARIO
        try:
            self.resultados = ["1", "2", "3"]
            for self.resultado in self.resultados:
                if int(self.resultado) == 1:
                    self.paraCombo = "Pesador"
                elif int(self.resultado) == 2:
                    self.paraCombo = "Supervisor"
                elif int(self.resultado) == 3:
                    self.paraCombo = "Administrador"
                else:
                    raise Exception("Error en comparacion")
                self.comboBoxNiveles.addItem(str(self.paraCombo), str(self.resultado))

        except Exception as e:
            logger.debug(f"Error en la lista: {e}")

    # Funciones

    def cancelar(self):
        logger.debug("Cancelar")
        self.close()

    def agregar(self):
        logger.debug("Agregar")

        self.nombreUsuario = self.lineEditUsuario.displayText()
        logger.debug("Nombre de usuario: {}".format(self.nombreUsuario))

        self.password = self.lineEditPassword.text()
        logger.debug(f"Password: {self.password}")

        self.password2 = self.lineEditPassword2.text()
        logger.debug(f"Password2: {self.password2}")

        self.nivel = self.comboBoxNiveles.itemData(self.comboBoxNiveles.currentIndex())
        logger.debug("Nivel de Usuario: {}".format(self.nivel))

        self.nombreCompleto = self.lineEditNombreCompleto.displayText()
        logger.debug("Nombre completo: {}".format(self.nombreCompleto))

        self.autenticado = 0

        if len(str(self.nombreUsuario)) <= 0:
            logger.debug("Esta vacio")
            QMessageBox.critical(self, "Mensaje", "El nombre de usuario no debe estar vacío.   ",
                                 QMessageBox.Ok)
            self.lineEditUsuario.setFocus()
            return

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
            try:
                query = "INSERT INTO `usuarios` (`id_usuario`, `usuario`, `password`, `nivel`, `autenticado`, `nombre_usuario`) VALUES (NULL, '{}', '{}', '{}', '{}', '{}')".format(
                    self.nombreUsuario, self.password, self.nivel, self.autenticado, self.nombreCompleto)
                logger.debug("Query: {}".format(query))
                self.cur.execute(query)
                self.conn.commit()
                QMessageBox.information(self, "Éxito", "Se agregó exitosamente", QMessageBox.Ok)
                self.hide()
                self.cur.close()
            except Exception as e:
                logger.debug("Error al insertar: {}".format(e))

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