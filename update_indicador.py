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
import sys
import glob
import serial

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


class updateDatosIndicador(QDialog):
    def __init__(self, parent=None):
        super(updateDatosIndicador, self).__init__(parent, flags=Qt.WindowCloseButtonHint)
        loadUi('update_indicador.ui', self)
        logger.debug("Ventana actualizar Datos del indicador")
        self.DB_Connect()

        # BOTONES
        self.btnCancelar.clicked.connect(self.cancelar)
        self.btnAgregar.clicked.connect(self.agregar)

        try:
            self.cur.execute("SELECT * FROM totalco_puertocomserial WHERE id_puerto = 1")
            self.row = self.cur.fetchone()

            self.id = self.row[0]

            self.puertobd = self.row[1]
            logger.debug(f"Puerto: {self.puertobd}")
            ################################################################################

            self.bitsxsec = self.row[2]
            logger.debug(f"Bits por segundo: {self.bitsxsec}")
            #################################################################################

            self.bitsdatos = self.row[3]
            logger.debug(f"Bits de datos: {self.bitsdatos}")
            if str(self.bitsdatos) == "serial.FOURBITS":
                self.bitsdatosasigna = 4

            elif str(self.bitsdatos) == "serial.FIVEBITS":
                self.bitsdatosasigna = 5

            elif str(self.bitsdatos) == "serial.SIXTBITS":
                self.bitsdatosasigna = 6

            elif str(self.bitsdatos) == "serial.SEVENBITS":
                self.bitsdatosasigna = 7

            elif str(self.bitsdatos) == "serial.EIGHTBITS":
                self.bitsdatosasigna = 8
            else:
                raise Exception("Ninguno de ellos")
            ##################################################################################

            self.paridad = self.row[4]
            logger.debug(f"Paridad: {self.paridad}")
            ##################################################################################

            self.bitsparada = self.row[5]
            logger.debug(f"Bits de parada: {self.bitsparada}")
            ##################################################################################

        except Exception as e:
            logger.debug(f"Error en el query: {e}")
        ####
        # PUERTOS
        ###
        try:
            if sys.platform.startswith('win'):
                self.ports = ['COM%s' % (i + 1) for i in range(256)]
            else:
                raise EnvironmentError('Unsupported platform')

            for self.port in self.ports:
                try:
                    ser = serial.Serial(self.port)
                    ser.close()
                    self.detectport = self.port
                    logger.debug(f"Puerto detectado: {self.detectport}")
                    if self.puertobd == self.detectport:
                        self.puertoBdDetectConfigurado = str(
                            self.port) + " (Detectado y configurado en la BD para el indicador)"
                        self.comboBoxPuerto.addItem(str(self.puertoBdDetectConfigurado), str(self.port))
                    elif self.detectport == self.port:
                        self.puertodetectado = str(self.port) + " (Puerto Detectado)"
                        self.comboBoxPuerto.addItem(str(self.puertodetectado), str(self.port))
                    elif self.puertobd != self.detectport and self.puertobd == self.port:
                        self.puertoBdConfigurado = str(self.port) + " (Puerto NO Detectado pero configurado en BD)"
                        self.comboBoxPuerto.addItem(str(self.puertoBdConfigurado), str(self.port))
                except (OSError, serial.SerialException):
                    pass
                    if self.puertobd == self.port:
                        self.puertoBdConfigurado = str(self.port) + " (Puerto NO Detectado pero configurado en BD)"
                        self.comboBoxPuerto.addItem(str(self.puertoBdConfigurado), str(self.port))
                    else:
                        self.comboBoxPuerto.addItem(str(self.port), str(self.port))
        except Exception as e:
            logger.debug("Error con los puertos seriales: {}".format(e))
        ####
        # FIN PUERTOS
        ###

        ####
        # BITS POR SEGUNDO
        ###
        try:
            self.bitsxsecInBd = str(self.bitsxsec) + " (Configurado en BD)"
            self.comboBox_bitsxsec.addItem(str(self.bitsxsecInBd), str(self.bitsxsec))

            self.resultados = ["1800", "2400", "4800", "7200", "9600", "14400", "19200", "38400", "57600", "115200"]
            for self.resultado in self.resultados:
                if self.resultado != self.bitsxsec:
                    logger.debug(f"Bits por segundo no configurados en BD: {self.resultado}")
                    self.comboBox_bitsxsec.addItem(str(self.resultado), str(self.resultado))
        except Exception as e:
            logger.debug(f"Error en los bits por segundo: {e}")

        ####
        # FIN BITS POR SEGUNDO
        ###

        ####
        # BITS DE DATOS
        ###
        try:
            if str(self.bitsdatos) == "serial.FOURBITS":
                logger.debug(f"Bits de datos cadena: {self.bitsdatos}")
                self.bitsdatosInBd = str(self.bitsdatosasigna) + " (Configurado en BD)"
                self.comboBox_bitsDatos.addItem(str(self.bitsdatosInBd), str(self.bitsdatosasigna))
            elif str(self.bitsdatos) == "serial.FIVEBITS":
                logger.debug(f"Bits de datos: {self.bitsdatos}")
                self.bitsdatosInBd = str(self.bitsdatosasigna) + " (Configurado en BD)"
                self.comboBox_bitsDatos.addItem(str(self.bitsdatosInBd), str(self.bitsdatosasigna))
            elif str(self.bitsdatos) == "serial.SIXBITS":
                logger.debug(f"Bits de datos: {self.bitsdatos}")
                self.bitsdatosInBd = str(self.bitsdatosasigna) + " (Configurado en BD)"
                self.comboBox_bitsDatos.addItem(str(self.bitsdatosInBd), str(self.bitsdatosasigna))
            elif str(self.bitsdatos) == "serial.SEVENBITS":
                logger.debug(f"Bits de datos: {self.bitsdatos}")
                self.bitsdatosInBd = str(self.bitsdatosasigna) + " (Configurado en BD)"
                self.comboBox_bitsDatos.addItem(str(self.bitsdatosInBd), str(self.bitsdatosasigna))
            elif str(self.bitsdatos) == "serial.EIGHTBITS":
                logger.debug(f"Bits de datos: {self.bitsdatos}")
                self.bitsdatosInBd = str(self.bitsdatosasigna) + " (Configurado en BD)"
                self.comboBox_bitsDatos.addItem(str(self.bitsdatosInBd), str(self.bitsdatosasigna))
            else:
                raise Exception("Error")
        except Exception as e:
            logger.debug(f"Error en ifs: {e}")

        try:
            self.resultados = ["4", "5", "6", "7", "8"]
            for self.resultado in self.resultados:
                if int(self.resultado) != int(self.bitsdatosasigna):
                    logger.debug(f"Bits de Datos no configurados en BD: {self.resultado}")
                    self.comboBox_bitsDatos.addItem(str(self.resultado), str(self.resultado))
        except Exception as e:
            logger.debug(f"Error en la lista: {e}")
        ####
        # FIN BITS DE DATOS
        ###

        ####
        # INICIO PARIDAD
        ###
        try:
            logger.debug("Inicia Paridad")
            if str(self.paridad) == "serial.PARITY_EVEN":
                self.paridadParaCombo = "Even"
                self.paridadParaComboString = "Even (Configurado en BD)"
                self.comboBox_Paridad.addItem(str(self.paridadParaComboString), str(self.paridadParaCombo))
            elif str(self.paridad) == "serial.PARITY_ODD":
                self.paridadParaCombo = "Odd"
                self.paridadParaComboString = "Odd (Configurado en BD)"
                self.comboBox_Paridad.addItem(str(self.paridadParaComboString), str(self.paridadParaCombo))
            elif str(self.paridad) == "serial.PARITY_NONE":
                self.paridadParaCombo = "None"
                self.paridadParaComboString = "None (Configurado en BD)"
                self.comboBox_Paridad.addItem(str(self.paridadParaComboString), str(self.paridadParaCombo))
            elif str(self.paridad) == "serial.PARITY_MARK":
                self.paridadParaCombo = "Mark"
                self.paridadParaComboString = "Mark (Configurado en BD)"
                self.comboBox_Paridad.addItem(str(self.paridadParaComboString), str(self.paridadParaCombo))
            elif str(self.paridad) == "serial.PARITY_SPACE":
                self.paridadParaCombo = "Space"
                self.paridadParaComboString = "Space (Configurado en BD)"
                self.comboBox_Paridad.addItem(str(self.paridadParaComboString), str(self.paridadParaCombo))
        except Exception as e:
            logger.debug(f"Error Paridad {e}")

        try:
            self.resultados = ["Even", "Odd", "None", "Mark", "Space"]
            for self.resultado in self.resultados:
                if str(self.resultado) != str(self.paridadParaCombo):
                    logger.debug(f"Paridad no configurados en BD: {self.resultado}")
                    self.comboBox_Paridad.addItem(str(self.resultado), str(self.resultado))
        except Exception as e:
            logger.debug(f"Error en la lista: {e}")

        ###
        # FIN PARIDAD
        ###

        ###
        # BITS DE PARADA
        ###
        try:
            logger.debug("Inicia Bits de parada")
            self.bitsdeparadaInBd = self.bitsparada + " (Configurado en BD)"
            self.comboBox_bitsDeParada.addItem(str(self.bitsdeparadaInBd), str(self.bitsparada))

            self.resultados = ["1", "1.5", "2"]
            for self.resultado in self.resultados:
                if self.resultado != self.bitsparada:
                    logger.debug(f"Bits de parada no configurados en BD: {self.resultado}")
                    self.comboBox_bitsDeParada.addItem(str(self.resultado), str(self.resultado))

        except Exception as e:
            logger.debug(f"Error en los bits de parada {e}")
        ###
        # FIN BITS DE PARADA
        ###

    def cancelar(self):
        logger.debug("Cancelar")
        self.close()

    def agregar(self):
        logger.debug("Agregar")
        self.capturaElPuerto = self.comboBoxPuerto.itemData(self.comboBoxPuerto.currentIndex())
        logger.debug("Puerto: {}".format(self.capturaElPuerto))

        self.capturbitsxsegundo = self.comboBox_bitsxsec.itemData(self.comboBox_bitsxsec.currentIndex())
        logger.debug("Bits por segundo: {}".format(self.capturbitsxsegundo))

        ####
        # BITS DE DATOS
        ###
        self.capturabitsdedatos1 = self.comboBox_bitsDatos.itemData(self.comboBox_bitsDatos.currentIndex())
        logger.debug(f"Bits de datos INDEX: {self.capturabitsdedatos1}")
        try:
            if int(self.capturabitsdedatos1) == 4:
                logger.debug(f"Valor de variable: {self.capturabitsdedatos1}")
                self.asignStringBitsDeDatos = "serial.FOURBITS"
                logger.debug(f"Valor en string: {self.asignStringBitsDeDatos}")

            elif int(self.capturabitsdedatos1) == 5:
                logger.debug(f"Valor de variable: {self.capturabitsdedatos1}")
                self.asignStringBitsDeDatos = "serial.FIVEBITS"
                logger.debug(f"Valor en string: {self.asignStringBitsDeDatos}")

            elif int(self.capturabitsdedatos1) == 6:
                logger.debug(f"Valor de variable: {self.capturabitsdedatos1}")
                self.asignStringBitsDeDatos = "serial.SIXBITS"
                logger.debug(f"Valor en string: {self.asignStringBitsDeDatos}")

            elif int(self.capturabitsdedatos1) == 7:
                logger.debug(f"Valor de variable: {self.capturabitsdedatos1}")
                self.asignStringBitsDeDatos = "serial.SEVENBITS"
                logger.debug(f"Valor en string: {self.asignStringBitsDeDatos}")

            elif int(self.capturabitsdedatos1) == 8:
                logger.debug(f"Valor de variable: {self.capturabitsdedatos1}")
                self.asignStringBitsDeDatos = "serial.EIGHTBITS"
                logger.debug(f"Valor en string: {self.asignStringBitsDeDatos}")

            else:
                raise Exception("Error")

        except Exception as e:
            logger.debug(f"Error {e}")
        ####
        # FIN BITS DE DATOS
        ###

        ###
        # PARIDAD
        ###
        self.capturaparidad = self.comboBox_Paridad.itemData(self.comboBox_Paridad.currentIndex())
        logger.debug("Bits paridad: {}".format(self.capturaparidad))
        try:
            if self.capturaparidad == "Even":
                self.capturaparidadForBD = "serial.PARITY_EVEN"
                logger.debug(f"Paridad para BD: {self.capturaparidadForBD}")
            elif self.capturaparidad == "Odd":
                self.capturaparidadForBD = "serial.PARITY_ODD"
                logger.debug(f"Paridad para BD: {self.capturaparidadForBD}")
            elif self.capturaparidad == "None":
                self.capturaparidadForBD = "serial.PARITY_NONE"
                logger.debug(f"Paridad para BD: {self.capturaparidadForBD}")
            elif self.capturaparidad == "Mark":
                self.capturaparidadForBD = "serial.PARITY_MARK"
                logger.debug(f"Paridad para BD: {self.capturaparidadForBD}")
            elif self.capturaparidad == "Space":
                self.capturaparidadForBD = "serial.PARITY_SPACE"
                logger.debug(f"Paridad para BD: {self.capturaparidadForBD}")
            else:
                raise Exception("Opcion no soportada")

        except Exception as e:
            logger.debug(f"Error em asignacion de paridad: {e}")
        ###
        # FIN DE PARIDAD
        ###

        ###
        # BITS DE PARADA
        ###
        self.capturabitsdeparada = self.comboBox_bitsDeParada.itemData(self.comboBox_bitsDeParada.currentIndex())
        logger.debug("Bits de Parada: {}".format(self.capturabitsdeparada))
        ###
        # FIN BITS DE PARADA
        ###

        try:
            query = """ UPDATE totalco_puertocomserial SET puerto = %s, baudrate = %s, bytesize = %s, parity = %s, timeout = %s WHERE id_puerto = %s """
            data = (str(self.capturaElPuerto), str(self.capturbitsxsegundo), str(self.asignStringBitsDeDatos), str(self.capturaparidadForBD), str(self.capturabitsdeparada), self.id)
            self.cur.execute(query, data)
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