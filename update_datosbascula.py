from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
import logging
import mysql.connector as mdb
from mysql.connector import Error
from PyQt5.QtWidgets import (QApplication, QMessageBox)
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIntValidator
import datetime
from datetime import datetime

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


class createDatosBascula(QDialog):
    def __init__(self, parent=None):
        super(createDatosBascula, self).__init__(parent, flags=Qt.WindowCloseButtonHint)
        loadUi('update_datosbascula.ui', self)
        logger.debug("Ventana agregar Datos Bascula")
        self.DB_Connect()

        # BOTONES
        self.btnCancelar.clicked.connect(self.cancelar)
        self.btnAgregar.clicked.connect(self.agregar)

        try:
            self.cur.execute("SELECT * FROM totalco_bascula ORDER BY id_bascula DESC limit 1")
            self.row = self.cur.fetchone()
            logger.debug("Query Last ID: {}".format(self.row))
            self.ultimo = self.row[0]
            logger.debug("Ultimo registro: {}".format(self.ultimo))
        except Exception as e:
            logger.debug("Error ULTIMO BASCULA: {}".format(e))

        try:
            self.cur.execute("SELECT * FROM totalco_bascula WHERE id_bascula ='" + str(self.ultimo) + "'")
            self.row = self.cur.fetchone()
            logger.debug("Query Bascula: {}".format(self.row))

            self.marca = self.row[1]
            self.aline_Marca.setText(str(self.marca))
            self.line_Marca.setText(str(self.marca))
            logger.debug("Marca: {}".format(self.marca))

            self.numeroSerie = self.row[2]
            self.aline_Serie.setText(str(self.numeroSerie))
            self.line_Serie.setText(str(self.numeroSerie))
            logger.debug("Numero de Serie: {}".format(self.numeroSerie))

            self.modInstrumento = self.row[3]
            self.aline_Instrumento.setText(str(self.modInstrumento))
            self.line_Instrumento.setText(str(self.modInstrumento))
            logger.debug("Mod Instrumento: {}".format(self.modInstrumento))

            self.aprobModelo = self.row[4]
            self.aline_Modelo.setText(str(self.aprobModelo))
            self.line_Modelo.setText(str(self.aprobModelo))
            logger.debug("Aprob Modelo: {}".format(self.aprobModelo))

            self.hologramaVerificacion = self.row[5]
            self.aline_Holograma.setText(str(self.hologramaVerificacion))
            logger.debug("Holograma: {}".format(self.hologramaVerificacion))

            self.certificadoCalidad = self.row[6]
            self.aline_Certificado.setText(str(self.certificadoCalidad))
            logger.debug("Certificado de Calidad: {}".format(self.certificadoCalidad))

            self.vigencia = self.row[7]
            # Obtener el año para mostrarlo
            formato = "%Y-%m-%d"
            # vigencia = "2023-06-18"
            fecha = datetime.strptime(str(self.vigencia), formato)
            logger.debug(fecha)
            self.aniovigencia = fecha.year
            self.aline_Anio.setText(str(self.aniovigencia))


            self.periododel = self.row[8]
            self.aline_pinial.setText(str(self.periododel))
            logger.debug("Periodo del: {}".format(self.periododel))

            self.periodoal = self.row[9]
            self.aline_pfinal.setText(str(self.periodoal))
            logger.debug("Periodo al: {}".format(self.periodoal))

        except Error as e:
            logger.debug("Error BASCULA: {}".format(e))

        e1 = self.line_Anio
        e1.objectName()
        e1.setValidator(QIntValidator())

        e2 = self.line_inidia
        e2.objectName()
        e2.setValidator(QIntValidator())

        e3 = self.line_inimes
        e3.objectName()
        e3.setValidator(QIntValidator())

        e4 = self.line_inianio
        e4.objectName()
        e4.setValidator(QIntValidator())

        e5 = self.line_findia
        e5.objectName()
        e5.setValidator(QIntValidator())

        e6 = self.line_finmes
        e6.objectName()
        e6.setValidator(QIntValidator())

        e7 = self.line_finanio
        e7.objectName()
        e7.setValidator(QIntValidator())

    # Funciones

    def cancelar(self):
        logger.debug("Cancelar")
        self.close()

    def agregar(self):
        logger.debug("Agregar")

        self.marca = self.line_Marca.displayText()
        logger.debug("Marca: {}".format(self.marca))

        self.numeroSerie = self.line_Serie.displayText()
        logger.debug("Numero de Serie: {}".format(self.numeroSerie))

        self.modInstrumento = self.line_Instrumento.displayText()
        logger.debug("Mod Instrumento: {}".format(self.modInstrumento))

        self.aprobModelo = self.line_Modelo.displayText()
        logger.debug("Mod Instrumento: {}".format(self.aprobModelo))

        self.hologramaVerificacion = self.line_Holograma.displayText()
        logger.debug("Mod Instrumento: {}".format(self.hologramaVerificacion))

        if len(str(self.hologramaVerificacion)) <= 0:
            logger.debug("Esta vacio")
            QMessageBox.critical(self, "Mensaje", "El holograma no debe estar vacío.   ",
                                 QMessageBox.Ok)
            self.line_Holograma.setFocus()
            return

        self.certificadoCalidad = self.line_Certificado.displayText()
        logger.debug("Mod Instrumento: {}".format(self.certificadoCalidad))

        if len(str(self.certificadoCalidad)) <= 0:
            logger.debug("Esta vacio")
            QMessageBox.critical(self, "Mensaje", "El certificado no debe estar vacío.   ",
                                 QMessageBox.Ok)
            self.line_Certificado.setFocus()
            return

        self.anio = self.line_Anio.displayText()
        logger.debug(f"Año: {self.anio}")

        if len(str(self.anio)) < 4:
            logger.debug("No son cuatro digitos")
            QMessageBox.critical(self, "Mensaje", "El formato es con cuatro digitos yyyy(2021, 2022, etc).   ", QMessageBox.Ok)
            self.line_Anio.setFocus()
            return

        elif int(self.anio) <= 2000:
            logger.debug("Menor o igual a 2000")
            QMessageBox.critical(self, "Mensaje", "No debe ser igual o menor a 2000.   ", QMessageBox.Ok)
            self.line_Anio.setFocus()
            return

        self.aniocertificado = self.anio + "-01-" + "01"
        logger.debug(f"Año completo: {self.aniocertificado}")

        self.inidia = self.line_inidia.displayText()
        logger.debug(f"Dia Inicial: {self.inidia}")

        if len(str(self.inidia)) < 2:
            logger.debug("No son dos digitos")
            QMessageBox.critical(self, "Mensaje", "El formato es con dos digitos dd(01, 02, etc).   ", QMessageBox.Ok)
            self.line_inidia.setFocus()
            return

        elif int(self.inidia) > 31:
            logger.debug("Mayor a 31")
            QMessageBox.critical(self, "Mensaje", "No debe ser mayor a 31.   ", QMessageBox.Ok)
            self.line_inidia.setFocus()
            return

        elif int(self.inidia) <= 0:
            logger.debug("Menor o igual a 0")
            QMessageBox.critical(self, "Mensaje", "No debe ser igual o menor a 0.   ", QMessageBox.Ok)
            self.line_inidia.setFocus()
            return

        self.inimes = self.line_inimes.displayText()
        logger.debug(f"Mes Inicial: {self.inimes}")

        if len(str(self.inimes)) < 2:
            logger.debug("No son dos digitos")
            QMessageBox.critical(self, "Mensaje", "El formato es con dos digitos mm(01, 02, etc).   ", QMessageBox.Ok)
            self.line_inimes.setFocus()
            return

        elif int(self.inimes) > 12:
            logger.debug("Mayor a 12")
            QMessageBox.critical(self, "Mensaje", "No debe ser mayor a 12.   ", QMessageBox.Ok)
            self.line_inimes.setFocus()
            return

        elif int(self.inimes) <= 0:
            logger.debug("Menor o igual a 0")
            QMessageBox.critical(self, "Mensaje", "No debe ser igual o menor a 0.   ", QMessageBox.Ok)
            self.line_inimes.setFocus()
            return

        self.inianio = self.line_inianio.displayText()
        logger.debug(f"Año Inicial: {self.inianio}")

        if len(str(self.inianio)) < 4:
            logger.debug("No son cuatro digitos")
            QMessageBox.critical(self, "Mensaje", "El formato es con cuatro digitos yyyy(2021, 2022, etc).   ", QMessageBox.Ok)
            self.line_inianio.setFocus()
            return

        elif int(self.inianio) <= 2000:
            logger.debug("Menor o igual a 2000")
            QMessageBox.critical(self, "Mensaje", "No debe ser igual o menor a 2000.   ", QMessageBox.Ok)
            self.line_inianio.setFocus()
            return

        self.findia = self.line_findia.displayText()
        logger.debug(f"Dia Final: {self.findia}")

        if len(str(self.findia)) < 2:
            logger.debug("No son dos digitos")
            QMessageBox.critical(self, "Mensaje", "El formato es con dos digitos dd(01, 02, etc).   ", QMessageBox.Ok)
            self.line_findia.setFocus()
            return

        elif int(self.findia) > 31:
            logger.debug("Mayor a 31")
            QMessageBox.critical(self, "Mensaje", "No debe ser mayor a 31.   ", QMessageBox.Ok)
            self.line_findia.setFocus()
            return

        elif int(self.findia) <= 0:
            logger.debug("Menor o igual a 0")
            QMessageBox.critical(self, "Mensaje", "No debe ser igual o menor a 0.   ", QMessageBox.Ok)
            self.line_findia.setFocus()
            return

        self.finmes = self.line_finmes.displayText()
        logger.debug(f"Mes Final: {self.finmes}")

        if len(str(self.finmes)) < 2:
            logger.debug("No son dos digitos")
            QMessageBox.critical(self, "Mensaje", "El formato es con dos digitos mm(01, 02, etc).   ", QMessageBox.Ok)
            self.line_finmes.setFocus()
            return

        elif int(self.finmes) > 12:
            logger.debug("Mayor a 12")
            QMessageBox.critical(self, "Mensaje", "No debe ser mayor a 12.   ", QMessageBox.Ok)
            self.line_finmes.setFocus()
            return

        elif int(self.finmes) <= 0:
            logger.debug("Menor o igual a 0")
            QMessageBox.critical(self, "Mensaje", "No debe ser igual o menor a 0.   ", QMessageBox.Ok)
            self.line_finmes.setFocus()
            return

        self.finanio = self.line_finanio.displayText()
        logger.debug(f"Año Final: {self.finanio}")

        if len(str(self.finanio)) < 4:
            logger.debug("No son cuatro digitos")
            QMessageBox.critical(self, "Mensaje", "El formato es con cuatro digitos yyyy(2021, 2022, etc).   ", QMessageBox.Ok)
            self.line_finanio.setFocus()
            return

        elif int(self.finanio) <= 2000:
            logger.debug("Menor o igual a 2000")
            QMessageBox.critical(self, "Mensaje", "No debe ser igual o menor a 2000.   ", QMessageBox.Ok)
            self.line_finanio.setFocus()
            return

        try:
            self.fecha1 = datetime(int(self.inianio), int(self.inimes), int(self.inidia))
            self.fecha2 = datetime(int(self.finanio), int(self.finmes), int(self.findia))
        except Exception as e:
            logger.debug(f"Error en la asignacion de fecha: {e}")

        try:
            if self.fecha2 <= self.fecha1:
                QMessageBox.critical(self, "Mensaje", "El periódo final no debe ser menor o igual al periódo inical.   ", QMessageBox.Ok)
                self.line_findia.setFocus()
                return
        except Error as e:
            logger.debug(f"Error en if antes del insert: {e}")

        try:
            logger.debug(f"{self.fecha1}")
            logger.debug(f"{self.fecha2}")

            self.inicial_date = self.inianio + "-" + self.inimes + "-" + self.inidia
            self.end_date = self.finanio + "-" + self.finmes + "-" + self.findia

            logger.debug(f"{self.inicial_date}")
            logger.debug(f"{self.end_date}")
        except Exception as e:
            logger.debug(f"Error en la asignacion de fechas {e}")

        self.ubicacion = 1
        self.empresa = 1

        try:
            query = "INSERT INTO `totalco_bascula` (`marca`, `num_serie`, `mod_instrumento`, `apro_modelo`, `holograma_verifi`, `certificado_cal`, `anio`, `periodo_del`, `periodo_al`, `ubicacion`, `empresa`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                self.marca, self.numeroSerie, self.modInstrumento, self.aprobModelo, self.hologramaVerificacion,
                self.certificadoCalidad, self.aniocertificado, self.inicial_date, self.end_date, self.ubicacion, self.empresa)
            logger.debug("Query: {}".format(query))
            self.cur.execute(query)
            self.conn.commit()
            QMessageBox.information(self, "Éxito", "Se actualizó exitosamente", QMessageBox.Ok)
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