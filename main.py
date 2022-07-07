################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
## This project can be used freely for all uses, as long as they maintain the
## respective credits only in the Python scripts, any information in the visual
## interface (GUI) can be modified without any implication.
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
##
################################################################################

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile, QIODevice
from PySide2 import QtUiTools
import mysql.connector as mdb
from mysql.connector import Error
import logging

#Logging and console
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

# GUI FILE
from app_modules import *

import ctypes
myappid = 'settings.sipcasmo.systemversion.01'# arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class Window2(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.DB_Connect()

        ## EVENT ==> BOTONES
        try:
            # BOTONES EMPRESA SUCURSAL
            self.ui.btn_datos_empresa.clicked.connect(self.datosEmpresa)
            self.ui.btn_datos_sucursal.clicked.connect(self.datosSucursal)

            # BOTONES CAMARAS
            self.ui.btn_camaras_conf.clicked.connect(self.camaras_conf)
            self.ui.btn_back_camaras.clicked.connect(self.camaras_menu)
            ## ACTIVAR DESACTIVAR CAMARAS
            self.ui.btn_camarasad.clicked.connect(self.camaras_ad)
            ### CAMARAS
            self.ui.btn_camera1.clicked.connect(self.camera1)
            self.ui.btn_camera2.clicked.connect(self.camera2)
            self.ui.btn_camera3.clicked.connect(self.camera3)
            self.ui.btn_camera4.clicked.connect(self.camera4)

            # BOTONES DATOS DE BASCULA
            self.ui.btn_Bascula.clicked.connect(self.datosBascula)

            # BOTONES TIPO DE PESADA
            self.ui.btn_pesada.clicked.connect(self.tipoDePesada)

            # BOTONES DE CONFIGURACION DE PUERTOS INDICADOR E IMPRESORA
            self.ui.btn_serialindicador.clicked.connect(self.confIndicador)
            self.ui.btn_serialimpresora.clicked.connect(self.confImpresora)

            # BOTONES PARA AGREGAR USUARIOS Y CAMBIAR LA CONTRASEÑA
            self.ui.btnBuscarUsuario.clicked.connect(self.buscaUsuario)
            self.ui.btnAgregarUsuario.clicked.connect(self.agregaUsuario)
            self.ui.btnContraUsuario.clicked.connect(self.cambiaContraUsuario)
            self.ui.btnActualizarTablaUsuarios.clicked.connect(self.actualizaTablaUsuarios)
            self.ui.buscarUsuarios.returnPressed.connect(self.buscaUsuario)

        except Exception as e:
            logger.debug(e)

        ## ==> END ##

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('SIPCASMO')
        ## ==> END ##

        ## ==> BRAND
        try:
            self.cur.execute("SELECT * FROM totalco_info_gral")
            self.row_authenticate = self.cur.fetchone()
            logger.debug("User: {}".format(self.row_authenticate[2]))
            UIFunctions.labelTitle(self, '{}'.format(self.row_authenticate[2]))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))
        ## ==> END ##

        ## ==> USER
        try:
            self.cur.execute("SELECT * FROM usuarios WHERE autenticado='1'")
            self.row_authenticate = self.cur.fetchone()
            logger.debug("User: {}".format(self.row_authenticate[5]))
            UIFunctions.labelDescription(self, 'Usuario: {}'.format(self.row_authenticate[5]))
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

        ## ==> END ##

        # System
        self.sistema = platform.system()
        self.version = platform.release()
        self.ui.label_credits.setText(self.sistema + ' ' + self.version)


        #UIFunctions.labelDescription(self, 'User')
        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "EMPRESA", "btn_empresa", "url(:/24x24/icons/24x24/ct-enterprise2.png)", True)
        UIFunctions.addNewMenu(self, "BASCULA", "btn_bascula", "url(:/24x24/icons/24x24/ct-romana3.png)", True)
        UIFunctions.addNewMenu(self, "CAMARAS", "btn_camaras", "url(:/24x24/icons/24x24/ct-camara.png)", True)
        UIFunctions.addNewMenu(self, "TIPO DE PESADA", "btn_tipo_pesada", "url(:/24x24/icons/24x24/ct-romana5.png)", True)
        UIFunctions.addNewMenu(self, "PUERTOS", "btn_puertos", "url(:/24x24/icons/24x24/ct-serial.png)", True)
        UIFunctions.addNewMenu(self, "USUARIOS", "btn_usuarios", "url(:/24x24/icons/24x24/cil-user.png)", True)
        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "page_empresa")
        ## ==> END ##

        ## ==> START PAGE
        ## ==> CHANGE TO REPORTS
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_empresa)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, " ", "", True)
        ## ==> END ##

        ###

        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################




        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################



        ## ==> QTableWidget RARAMETERS
        ########################################################################
        # self.ui.tableWidget_2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        ## ==> END ##



        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## DATABASE CONECCT
    def DB_Connect(self):
        try:
            self.conn = mdb.connect(host="localhost", user="root", password="P4ssw0rd", database="gcasmo")
            self.cur = self.conn.cursor()
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    ## ==> END ##

    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE EMPRESA
        if btnWidget.objectName() == "btn_empresa":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_empresa)
            UIFunctions.resetStyle(self, "page_empresa")
            UIFunctions.labelPage(self, "Empresa")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE BASCULA
        if btnWidget.objectName() == "btn_bascula":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_bascula)
            UIFunctions.resetStyle(self, "page_bascula")
            UIFunctions.labelPage(self, "Bascula")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE CAMARAS
        if btnWidget.objectName() == "btn_camaras":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_camaras)
            UIFunctions.resetStyle(self, "page_camaras")
            UIFunctions.labelPage(self, "Camaras")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE TIPO DE PESADA
        if btnWidget.objectName() == "btn_tipo_pesada":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_tipo_pesada)
            UIFunctions.resetStyle(self, "btn_tipo_pesada")
            UIFunctions.labelPage(self, "TIPO DE PESADA")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE TIPO DE PESADA
        if btnWidget.objectName() == "btn_puertos":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_puertos)
            UIFunctions.resetStyle(self, "btn_puertos")
            UIFunctions.labelPage(self, "PUERTOS SERIALES")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE USUARIOS
        if btnWidget.objectName() == "btn_usuarios":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_usuarios)
            UIFunctions.resetStyle(self, "page_usuarios")
            UIFunctions.labelPage(self, "Usuarios")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            try:
                self.cur.execute("SELECT id_usuario, usuario, nivel FROM `usuarios` ORDER BY `nivel` ASC")
                self.resultados = self.cur.fetchall()
                self.ui.table_usuarios.clearContents()
                logger.debug("Tabla de usuarios")
                try:
                    fila = 0
                    for resultado in self.resultados:
                        self.ui.table_usuarios.setRowCount(fila + 1)
                        self.ui.table_usuarios.setColumnHidden(0, True)
                        self.ui.table_usuarios.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                        self.ui.table_usuarios.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                        if int(resultado[2]) == 1:
                            self.niveldeusuario = "Pesador"
                            self.ui.table_usuarios.setItem(fila, 2, QTableWidgetItem(str(self.niveldeusuario)))
                        elif int(resultado[2]) == 2:
                            self.niveldeusuario = "Supervisor"
                            self.ui.table_usuarios.setItem(fila, 2, QTableWidgetItem(str(self.niveldeusuario)))
                        elif int(resultado[2]) == 3:
                            self.niveldeusuario = "Administrador"
                            self.ui.table_usuarios.setItem(fila, 2, QTableWidgetItem(str(self.niveldeusuario)))
                        else:
                            raise Exception("Error en el nivel de usuario")
                        fila += 1
                except Exception as e:
                    logger.debug(f"Error al llenar la tabla {e}")

            except Exception as e:
                logger.debug(f"Error en la tabla de usuarios {e}")


    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> CAMARAS

    def camaras_conf(self):
        logger.debug("Ir a la configuracion de cada camara")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_camaras_conf)
        UIFunctions.labelPage(self, "Menú Configuracion de camaras")

    def camaras_menu(self):
        logger.debug("Menu Camaras)")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_camaras)
        UIFunctions.labelPage(self, "Menu Cámaras")

    def camaras_ad(self):
        logger.debug("Activar Desactivar las cámaras")
        from update_camaras import updateCamaraAD
        goto = updateCamaraAD()
        goto.exec_()

    def camera1(self):
        logger.debug("Camera 1")
        from conf_camera1 import updateCamera1
        goto = updateCamera1()
        goto.exec_()

    def camera2(self):
        logger.debug("Camera 2")
        from conf_camera2 import updateCamera2
        goto = updateCamera2()
        goto.exec_()

    def camera3(self):
        logger.debug("Camera 3")
        from conf_camera3 import updateCamera3
        goto = updateCamera3()
        goto.exec_()

    def camera4(self):
        logger.debug("Camera 4")
        from conf_camera4 import updateCamera4
        goto = updateCamera4()
        goto.exec_()

    ## ==> END ##

    ## EVENT ==> EMPRESA Y SUCURSAL

    def datosEmpresa(self):
        logger.debug("Funcion para actualizar datos de la empresa")
        from update_company import updateCompany
        goto = updateCompany()
        goto.exec_()

    def datosSucursal(self):
        logger.debug("Funcion para actualizar la sucursal")
        from update_sucursal import updateSucursal
        goto = updateSucursal()
        goto.exec_()

    ## ==> END ##

    ## EVENT ==> DATOS DE LA BASCULA

    def datosBascula(self):
        logger.debug("Funcion para actualizar datos de la bascula")
        from update_datosbascula import createDatosBascula
        goto = createDatosBascula()
        goto.exec_()

    ## ==> END ##

    ## EVENT ==> PESADA MANUAL O AUTOMATICA

    def tipoDePesada(self):
        logger.debug("Funcion para actualizar el tipo de pesada")
        from update_pesada import updatePesada
        goto = updatePesada()
        goto.exec_()

    ## ==> END ##

    ## EVENT ==> CONFIGURACION DE PUERTOS DE INDICADOR E IMPRESORA

    def confIndicador(self):
        logger.debug("Funcion para configurar el indicador")
        from update_indicador import updateDatosIndicador
        goto = updateDatosIndicador()
        goto.exec_()

    def confImpresora(self):
        logger.debug("Funcion para configurar la impresora")
        from update_impresora import updateDatosImpresora
        goto = updateDatosImpresora()
        goto.exec_()

    ## ==> END ##

    ## EVENT ==> USUARIOS Y CONTRASEÑAS
    def buscaUsuario(self):
        logger.debug("Buscar Usuarios")
        self.textoBuscar = self.ui.buscarUsuarios.text()
        logger.debug("Texto a buscar: {}".format(self.textoBuscar))
        if self.textoBuscar:
            try:
                self.cur.execute("SELECT * FROM usuarios WHERE usuario LIKE '%" + self.textoBuscar + "%'")
                self.resultados = self.cur.fetchall()
                self.ui.table_usuarios.clearContents()
                if self.resultados:
                    try:
                        fila = 0
                        for resultado in self.resultados:
                            self.ui.table_usuarios.setRowCount(fila + 1)
                            self.ui.table_usuarios.setColumnHidden(0, True)
                            self.ui.table_usuarios.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                            self.ui.table_usuarios.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))

                            if int(resultado[3]) == 1:
                                self.niveldeusuario = "Pesador"
                                self.ui.table_usuarios.setItem(fila, 2, QTableWidgetItem(str(self.niveldeusuario)))
                            elif int(resultado[3]) == 2:
                                self.niveldeusuario = "Supervisor"
                                self.ui.table_usuarios.setItem(fila, 2, QTableWidgetItem(str(self.niveldeusuario)))
                            elif int(resultado[3]) == 3:
                                self.niveldeusuario = "Administrador"
                                self.ui.table_usuarios.setItem(fila, 2, QTableWidgetItem(str(self.niveldeusuario)))
                            else:
                                raise Exception("Error en el nivel de usuario")
                            fila += 1
                    except Exception as e:
                        logger.exception("Error For: {}".format(e))
                else:
                    QMessageBox.information(self, "Sin Resultados", "No se encontro ningun resultado .   ", QMessageBox.Ok)
                    try:
                        self.cur.execute("SELECT id_usuario, usuario, nivel FROM `usuarios` ORDER BY `nivel` ASC")
                        self.resultados = self.cur.fetchall()
                        self.ui.table_usuarios.clearContents()
                        try:
                            fila = 0
                            for resultado in self.resultados:
                                self.ui.table_usuarios.setRowCount(fila + 1)
                                self.ui.table_usuarios.setColumnHidden(0, True)
                                self.ui.table_usuarios.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                                self.ui.table_usuarios.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                                if int(resultado[2]) == 1:
                                    self.niveldeusuario = "Pesador"
                                    self.ui.table_usuarios.setItem(fila, 2, QTableWidgetItem(str(self.niveldeusuario)))
                                elif int(resultado[2]) == 2:
                                    self.niveldeusuario = "Supervisor"
                                    self.ui.table_usuarios.setItem(fila, 2, QTableWidgetItem(str(self.niveldeusuario)))
                                elif int(resultado[2]) == 3:
                                    self.niveldeusuario = "Administrador"
                                    self.ui.table_usuarios.setItem(fila, 2, QTableWidgetItem(str(self.niveldeusuario)))
                                else:
                                    raise Exception("Error en el nivel de usuario")
                                # self.ui.table_usuarios.setItem(fila, 2, QTableWidgetItem(str(resultado[2])))
                                fila += 1
                        except Exception as e:
                            logger.exception("Error For: {}".format(e))
                    except Exception as e:
                        logger.exception("Error DB: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))
        else:
            logger.debug("Vacio")
            try:
                self.cur.execute("SELECT id_usuario, usuario, nivel FROM `usuarios` ORDER BY `nivel` ASC")
                self.resultados = self.cur.fetchall()
                self.ui.table_usuarios.clearContents()
                try:
                    fila = 0
                    for resultado in self.resultados:
                        self.ui.table_usuarios.setRowCount(fila + 1)
                        self.ui.table_usuarios.setColumnHidden(0, True)
                        self.ui.table_usuarios.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                        self.ui.table_usuarios.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                        if int(resultado[2]) == 1:
                            self.niveldeusuario = "Pesador"
                            self.ui.table_usuarios.setItem(fila, 2, QTableWidgetItem(str(self.niveldeusuario)))
                        elif int(resultado[2]) == 2:
                            self.niveldeusuario = "Supervisor"
                            self.ui.table_usuarios.setItem(fila, 2, QTableWidgetItem(str(self.niveldeusuario)))
                        elif int(resultado[2]) == 3:
                            self.niveldeusuario = "Administrador"
                            self.ui.table_usuarios.setItem(fila, 2, QTableWidgetItem(str(self.niveldeusuario)))
                        else:
                            raise Exception("Error en el nivel de usuario")
                        fila += 1
                except Exception as e:
                    logger.exception("Error For: {}".format(e))
            except Exception as e:
                logger.exception("Error DB: {}".format(e))

    def agregaUsuario(self):
        logger.debug("Agregar usuarios")
        from agregar_usuario import agregarUsuario
        goto = agregarUsuario()
        goto.exec_()

    def cambiaContraUsuario(self):
        logger.debug("Actualiza contraseña")
        self.filaSeleccionada = self.ui.table_usuarios.selectedItems()
        try:
            if self.filaSeleccionada:
                indiceFila = self.filaSeleccionada[0].row()
                idItem = self.ui.table_usuarios.item(indiceFila, 0).text()
                nombreItem = self.ui.table_usuarios.item(indiceFila, 1).text()
                logger.debug("Id en la tabla: {}".format(idItem))
                logger.debug("Usuario: {}".format(nombreItem))

                from actualiza_contra import actualizaContra
                goto = actualizaContra(idItem, nombreItem)
                goto.exec_()

            else:
                QMessageBox.critical(self, "Actualizar", "Primero seleccione una fila.   ",
                                     QMessageBox.Ok)
        except Exception as e:
            logger.debug("Error al actualizar la fila {}".format(e))


    def actualizaTablaUsuarios(self):
        logger.debug("Actualizar tabla de usuarios")
        logger.debug("Refrescar info")
        try:
            self.cur.execute("SELECT id_usuario, usuario, nivel FROM `usuarios` ORDER BY `nivel` ASC")
            self.resultados = self.cur.fetchall()
            self.ui.table_usuarios.clearContents()
            try:
                fila = 0
                for resultado in self.resultados:
                    self.ui.table_usuarios.setRowCount(fila + 1)
                    self.ui.table_usuarios.setColumnHidden(0, True)
                    self.ui.table_usuarios.setItem(fila, 0, QTableWidgetItem(str(resultado[0])))
                    self.ui.table_usuarios.setItem(fila, 1, QTableWidgetItem(str(resultado[1])))
                    if int(resultado[2]) == 1:
                        self.niveldeusuario = "Pesador"
                        self.ui.table_usuarios.setItem(fila, 2, QTableWidgetItem(str(self.niveldeusuario)))
                    elif int(resultado[2]) == 2:
                        self.niveldeusuario = "Supervisor"
                        self.ui.table_usuarios.setItem(fila, 2, QTableWidgetItem(str(self.niveldeusuario)))
                    elif int(resultado[2]) == 3:
                        self.niveldeusuario = "Administrador"
                        self.ui.table_usuarios.setItem(fila, 2, QTableWidgetItem(str(self.niveldeusuario)))
                    else:
                        raise Exception("Error en el nivel de usuario")
                    fila += 1
            except Exception as e:
                logger.debug("ERROR: {}".format(e))
        except Exception as e:
            logger.debug("ERROR: {}".format(e))
    ##

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
        if event.key() == Qt.Key_Escape:
            logger.debug("Key Scape")
            self.close()
    ## ==> END ##

    ## Close window
    def closeEvent(self, event):

        reply = QMessageBox.question(
            self, "Mensaje",
            "Estas seguro de salir?",
            QMessageBox.Close | QMessageBox.Cancel)

        if reply == QMessageBox.Close:
            logger.debug("Close")
            # Identify User
            try:
                self.cur.execute("SELECT * FROM usuarios WHERE autenticado='1'")
                self.row_authenticate = self.cur.fetchone()
                if self.row_authenticate is None:
                    logger.debug("No hay usuario en el sistema")
                else:
                    logger.debug("Identifica")
                    sql = """ UPDATE usuarios SET autenticado = %s WHERE id_usuario = %s """
                    row = (0, self.row_authenticate[0])
                    self.cur.execute(sql, row)
                    self.conn.commit()
            except Exception as e:
                logger.exception("Error DB: {}".format(e))
            # Authenticate Update
        else:
            logger.debug("Cancel")
            event.ignore()

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(Window2, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################

class MainWindow(QMainWindow):

    def __init__(self, ui_file, parent=None):
        super(MainWindow, self).__init__(parent)
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()

        #Buttons and Fields
        btn = self.window.findChild(QPushButton, 'ButtonLogin')
        btn.clicked.connect(self.window2)
        field_pass = self.window.findChild(QLineEdit, 'password')
        field_pass.returnPressed.connect(self.window2)
        self.window.show()
        self.DB_Connect()

    def DB_Connect(self):
        try:
            self.conn = mdb.connect(host="localhost", user="root", password="P4ssw0rd", database="gcasmo")
            self.cur = self.conn.cursor()
        except Exception as e:
            logger.exception("Error DB: {}".format(e))

    def window2(self):
        logger.debug("Login Button")
        get_user = self.window.findChild(QLineEdit, 'user')
        username = get_user.text()
        logger.debug("Usuario: {}".format(str(username)))
        get_password = self.window.findChild(QLineEdit, 'password')
        password = get_password.text()
        logger.debug("Password: {}".format(password))

        # Inicia login
        try:
            self.cur.execute("SELECT * FROM usuarios WHERE autenticado='1'")
            self.row_authenticate = self.cur.fetchone()
            logger.debug("Query: {}".format(self.cur))
            logger.debug("Result row_authenticate: {}".format(self.row_authenticate))
            logger.debug("Result 4: {}".format(self.row_authenticate))
            if self.row_authenticate is None:
                try:
                    self.cur.execute(
                        "SELECT * FROM usuarios WHERE usuario='" + username + "' AND password='" + password + "'")
                    self.row = self.cur.fetchone()
                    logger.debug("Query: {}".format(self.cur))
                    logger.debug("Result: {}".format(self.row))
                except Exception as e:
                    logger.exception("Error Query Usuario: {}".format(e))

                if self.row is not None:
                    logger.debug("User level: {}".format(self.row[3]))

                    def level1():
                        logger.debug("Hi level 1")

                    def level2():
                        logger.debug("Hi level 2")

                    def level3():
                        logger.debug("Hi level 3")
                        sql = """ UPDATE usuarios SET autenticado = %s WHERE id_usuario = %s """
                        row = (1, self.row[0])
                        self.cur.execute(sql, row)
                        self.conn.commit()
                        self.Administrador()

                    # Python switch
                    level = self.row[3]
                    options = {1: level1,
                               2: level2,
                               3: level3,
                               }
                    options[level]()
                else:
                    logger.debug("Usuario o password incorrecto/vacio")
                    Q = QMessageBox()
                    Q = QMessageBox.information(Q, 'Error',
                                                'Usuario o password incorrecto/vacio.',
                                                QMessageBox.Ok)
            else:
                logger.debug("Hay un usuario en el sistema")
                Q = QMessageBox()
                Q = QMessageBox.information(Q, 'Error',
                                            'El sistema ya esta siendo utilizado.',
                                            QMessageBox.Ok)
        except Exception as e:
            logger.exception("Error Query Usuario: {}".format(e))

    def Administrador(self):
        logger.debug("Administrador")
        self.w = Window2()
        self.w.show()
        # self.window.hide()
        self.window.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_icon = QtGui.QIcon()
    app_icon.addFile('icons/company/settings.png', QtCore.QSize(256, 256))
    app.setWindowIcon(app_icon)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow('login.ui')
    sys.exit(app.exec_())