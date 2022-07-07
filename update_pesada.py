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


class updatePesada(QDialog):
    def __init__(self, parent=None):
        super(updatePesada, self).__init__(parent, flags=Qt.WindowCloseButtonHint)
        loadUi('update_pesada.ui', self)
        logger.debug("Ventana elegir el tipo de pesada")
        self.DB_Connect()

        try:
            self.cur.execute("SELECT * FROM totalco_pesada_manual")
            self.row_tipoPesada = self.cur.fetchone()
            logger.debug("Valor en la BD de camaras_activas: {}".format(self.row_tipoPesada[0]))
            self.pesada = self.row_tipoPesada[0]
            if self.pesada == 0:
                logger.debug("Pesada Automatica")
                logger.debug("Valor en la BD: {}".format(self.pesada))
                self.status = "Pesada Automatica Activada"
                self.lineStatusPesada.setText(str(self.status))
                self.operacion = "Activar Pesada Manual"
                self.operacionAD = 1
                self.btn_pesadaAD.setStyleSheet('QPushButton {'
                                                 'border-color: rgb(27, 29, 35);font: 75 18pt "MS Shell Dlg 2";	'
                                                 'color: rgb(255, 0, 0);background-color: rgb(27, 29, 35);'
                                                 'border: 0px solid;border-radius: 10px;}'
                                                 'QPushButton:hover {'
                                                 'background-color:rgb(44, 49, 60);'
                                                 'border-color: rgb(27, 29, 35);'
                                                 'border: 2px solid;}'
                                                 )
                self.btn_pesadaAD.setText(str(self.operacion))
            elif self.pesada == 1:
                logger.debug("Pesada manual")
                logger.debug("Valor en la BD: {}".format(self.pesada))
                self.status = "Pesada Manual Activada"
                self.lineStatusPesada.setText(str(self.status))
                self.operacion = "Desactivar Pesada Manual"
                self.operacionAD = 0
                self.btn_pesadaAD.setStyleSheet('QPushButton {'
                                                 'border-color: rgb(27, 29, 35);font: 75 18pt "MS Shell Dlg 2";	'
                                                 'color: rgb(0, 255, 0);background-color: rgb(27, 29, 35);'
                                                 'border: 0px solid;border-radius: 10px;}'
                                                 'QPushButton:hover {'
                                                 'background-color:rgb(44, 49, 60);'
                                                 'border-color: rgb(27, 29, 35);'
                                                 'border: 2px solid;}'
                                                 )
                self.btn_pesadaAD.setText(str(self.operacion))

        except Exception as e:
            logger.exception("Error DB: {}".format(e))

        # BOTONES
        self.btnCancelCamera.clicked.connect(self.cancelar)
        self.btn_pesadaAD.clicked.connect(self.actualizar)

    # Funciones

    def cancelar(self):
        logger.debug("Cancelar")
        self.close()

    def actualizar(self):
        logger.debug("Actualizar")
        logger.debug("Valor en la BD del tipo de pesada: {}".format(self.pesada))
        logger.debug(f"Valor de self.operacionAD: {self.operacionAD}")
        try:
            query = """ UPDATE totalco_pesada_manual SET tipo_pesada = %s """
            data = (self.operacionAD, )
            self.cur.execute(query, data)
            self.conn.commit()
            QMessageBox.information(self, "Éxito", "Operación exitosa", QMessageBox.Ok)
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