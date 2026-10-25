
# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''
====================================================================================
Desarrollado Por: Cristian M. Veliz Cano
Versión del Soft: V-05
Nombre del Soft: "Visor de Imágenes Múltiple"
Tipo: Módulo para Sistema de Vigilancia
Distribución: Gratuito --> OPEN-SOURCE / FREE-CODE <--
Licencia: MIT License
Framework: Python + PyQt5
Procesamiento de Imágenes: OpenCV + Imutils
Integración: Sistema_de_Vigilancia_Profesional_v5.py
====================================================================================

VISOR DE IMÁGENES MÚLTIPLE
Módulo de Visualización de Capturas para Sistema de Vigilancia

DESCRIPCIÓN GENERAL:

Visor de Imágenes Múltiple es un componente gráfico desarrollado en Python
con PyQt5, diseñado para visualizar, organizar y recorrer colecciones de
imágenes desde una interfaz integrada en un sistema de vigilancia.

El módulo permite seleccionar imágenes manualmente o cargar automáticamente
las capturas almacenadas en una carpeta determinada. Las imágenes se presentan
en una cuadrícula de miniaturas, organizadas en páginas para facilitar la
consulta de colecciones numerosas.

La interfaz incluye controles de navegación, un contador de imágenes y un
visor individual que permite ampliar la consulta de las imágenes seleccionadas.
También incorpora funciones para recorrer imágenes de una misma carpeta y
abrirlas mediante OpenCV en una ventana independiente.

El componente está preparado para integrarse con una aplicación principal
de vigilancia mediante señales de PyQt5 y métodos públicos para recargar
capturas y establecer una carpeta de almacenamiento personalizada.

CARACTERÍSTICAS PRINCIPALES:

- Interfaz gráfica desarrollada con PyQt5.
- Diseño oscuro con detalles visuales inspirados en sistemas de vigilancia.
- Presentación de imágenes mediante miniaturas organizadas en cuadrículas.
- Distribución de hasta 20 imágenes por página en una cuadrícula de 4 × 5.
- Carga manual de imágenes mediante un cuadro de diálogo.
- Carga automática de imágenes desde la carpeta de capturas.
- Ordenación de las capturas por fecha de modificación, de más recientes
  a más antiguas.
- Contador del número de imágenes disponibles.
- Navegación entre páginas mediante botones.
- Acceso directo a la primera página.
- Botones para avanzar y retroceder entre páginas.
- Visualización del número de página actual.
- Apertura de imágenes individuales en una ventana de diálogo.
- Navegación entre imágenes mediante controles anterior y siguiente.
- Presentación del nombre del archivo en el botón inferior del visor.
- Adaptación del título cuando el nombre del archivo es demasiado largo.
- Apertura de imágenes mediante una ventana de OpenCV en Windows.
- Señales para comunicar eventos a otros componentes de la aplicación.
- Métodos públicos para recargar capturas y configurar carpetas.
- Administración de iconos y recursos externos.
- Preparación para localizar recursos en aplicaciones empaquetadas
  mediante PyInstaller.

FORMATOS DE IMAGEN CONTEMPLADOS:

El módulo incluye filtros y búsquedas para los siguientes formatos:

- PNG
- JPG
- JPEG
- BMP
- GIF
- WEBP
- TIFF
- ICO

La visualización y el procesamiento de cada archivo dependen de las
capacidades de las bibliotecas utilizadas y del formato de la imagen.

ORGANIZACIÓN Y NAVEGACIÓN:

1. CARGA DE IMÁGENES:
   Permite seleccionar archivos desde el sistema de archivos o recuperar
   automáticamente las imágenes guardadas en la carpeta de capturas.

2. GENERACIÓN DE MINIATURAS:
   Cada imagen se presenta en un contenedor con su miniatura y nombre
   de archivo para facilitar su identificación.

3. PAGINACIÓN:
   Las imágenes se distribuyen en páginas de hasta 20 elementos, evitando
   presentar toda la colección en una única cuadrícula.

4. NAVEGACIÓN:
   Los controles Inicio, Anterior y Siguiente permiten recorrer las páginas
   disponibles mediante una interfaz sencilla.

5. VISOR INDIVIDUAL:
   Al seleccionar una miniatura, se abre una ventana de consulta con la
   imagen correspondiente y controles para recorrer otras imágenes.

6. ACTUALIZACIÓN DE CAPTURAS:
   El módulo permite volver a cargar el contenido de la carpeta configurada.

INTEGRACIÓN CON EL SISTEMA DE VIGILANCIA:

El componente está concebido para trabajar como módulo independiente
o incorporarse a una aplicación principal de vigilancia.

Señales disponibles:

- clicked(QWidget): comunica la selección mediante un evento de clic.
- request_close(QWidget): solicita el cierre del componente.
- image_opened(str): comunica la ruta de una imagen abierta.

Métodos públicos de integración:

- reload(): recarga las imágenes de la carpeta de capturas.
- set_captures_folder(folder_path): establece una carpeta de capturas.
- get_current_image(): proporciona una ruta de imagen según el estado
  de navegación del componente.

Estas interfaces facilitan la comunicación con otros componentes de
PyQt5 y la integración en una arquitectura modular.

ADMINISTRACIÓN DE RECURSOS:

La clase Path permite obtener rutas para los recursos de la aplicación.

Entre los recursos contemplados se encuentran:

- Iconos de la interfaz.
- Carpeta de capturas.
- Imágenes utilizadas durante la ejecución.

El administrador contempla tanto la ejecución desde el código fuente
como la búsqueda de recursos en el directorio temporal utilizado por
PyInstaller.

TECNOLOGÍAS UTILIZADAS:

- Python 3: lenguaje de programación principal.
- PyQt5: interfaz gráfica, ventanas, controles y señales.
- OpenCV (cv2): apertura y visualización de imágenes.
- Imutils: biblioteca auxiliar para operaciones de procesamiento de imágenes.
- QPixmap: carga y presentación gráfica de imágenes.
- QLabel: presentación de miniaturas, nombres y contenido visual.
- QScrollArea: área desplazable para el contenido.
- QStackedWidget: organización de las páginas de imágenes.
- QGridLayout: distribución de miniaturas en cuadrícula.
- QDialog: ventana individual de visualización.
- QTimer: carga inicial diferida de las capturas.
- QIcon: administración de iconos.
- PyInstaller: compatibilidad prevista con aplicaciones empaquetadas.

APLICACIONES Y USOS:

- Consulta visual de capturas de un sistema de vigilancia.
- Organización de colecciones de imágenes.
- Revisión de capturas recientes.
- Navegación por grandes conjuntos de imágenes.
- Visualización ampliada de imágenes seleccionadas.
- Integración de visores gráficos en aplicaciones PyQt5.
- Creación de herramientas de consulta y revisión de imágenes.
- Aprendizaje práctico de interfaces gráficas y procesamiento visual.

DISTRIBUCIÓN Y FILOSOFÍA DEL PROYECTO:

Visor de Imágenes Múltiple está concebido como un componente reutilizable
para facilitar la consulta de imágenes en aplicaciones de escritorio.

Su diseño modular permite utilizarlo de forma independiente o integrarlo
en un sistema de vigilancia, manteniendo separadas las funciones de
visualización y las responsabilidades de la aplicación principal.

El proyecto está orientado al uso gratuito, educativo y práctico, y puede
adaptarse a diferentes necesidades de organización y consulta de imágenes,
respetando los términos de la licencia que acompañe a su distribución.

ENLACE DE DISTRIBUCIÓN:

MEGA:
https://mega.nz/file/TpMQDARB#JVIKriSSwUD_JKYaW8XtYxjqodutvb1fQAdPtlzVNFw

====================================================================================
Desarrollado por: Cristian M. Veliz Cano
Software gratuito y de código abierto (Open-Source).
====================================================================================
'''

import sys
import os
import cv2
import imutils

from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QScrollArea, QDialog, QMessageBox,
    QPushButton, QLabel, QFileDialog, QStackedWidget,
    QSizePolicy, QApplication, QGridLayout, QFrame
)
from PyQt5.QtGui import QPixmap, QFont, QIcon, QPalette
from PyQt5.QtCore import Qt, pyqtSignal, QTimer

##====================================================================================
# --- Clase para manejo de rutas ---
##====================================================================================
class Path:
    @staticmethod
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    @staticmethod
    def resource_path_app():
        try:
            return getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))
        except Exception:
            return os.path.abspath(".")

##====================================================================================
# --- WIDGET PRINCIPAL: Visor de Imágenes ---
##====================================================================================
class ImageViewerWidget(QWidget):
    # Señales para integración con MainWindow
    clicked = pyqtSignal(QWidget)
    request_close = pyqtSignal(QWidget)
    image_opened = pyqtSignal(str)  # Emitir ruta de imagen abierta

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("🔥 Visor de Imagenes Multiple-v5 🔥")
        self.center_on_screen()

        self.image_paths = []
        self.current_page = 0
        self.carpeta_capturas = Path.resource_path("capturas")

        # Icono
        icon_path = Path.resource_path("Ico\\1.ico")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        
        # Asegurar que existe la carpeta
        os.makedirs(self.carpeta_capturas, exist_ok=True)

        self._create_ui()
        self._apply_styles()
        
        # Cargar imágenes automáticamente al iniciar
        QTimer.singleShot(100, self.load_captures_folder)

    def _create_ui(self):
        """Crea la interfaz del visor de imágenes"""
        
        # Layout principal
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(10)

        # Header con título
        self.header = QWidget()
        header_layout = QHBoxLayout(self.header)
        header_layout.setContentsMargins(0, 0, 0, 0)
        
        self.title_label = QLabel("📷 VISOR DE IMÁGENES")
        self.title_label.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.title_label.setStyleSheet("color: #00c3ff;")
        
        header_layout.addWidget(self.title_label)
        header_layout.addStretch()
        
        # Contador de imágenes
        self.counter_label = QLabel("0 imágenes")
        self.counter_label.setStyleSheet("color: #aaaaaa;")
        header_layout.addWidget(self.counter_label)
        
        self.main_layout.addWidget(self.header)

        # Área de contenido con scroll
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                border: 1px solid #333333;
                border-radius: 5px;
                background-color: #1a1a1a;
            }
        """)
        
        # Contenedor del stacked widget
        self.container = QWidget()
        self.container_layout = QVBoxLayout(self.container)
        self.container_layout.setContentsMargins(5, 5, 5, 5)
        self.container_layout.setSpacing(0)
        
        # Stacked widget para páginas
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setStyleSheet('background-color: #1a1a1a;')
        
        self.container_layout.addWidget(self.stacked_widget)
        self.scroll_area.setWidget(self.container)
        
        self.main_layout.addWidget(self.scroll_area, stretch=1)

        # Panel de controles inferior
        self.controls_panel = QWidget()
        controls_layout = QHBoxLayout(self.controls_panel)
        controls_layout.setContentsMargins(0, 0, 0, 0)
        controls_layout.setSpacing(3)

        # Botón Abrir Archivos
        self.open_button = QPushButton('📂 Abrir Archivos')
        self.open_button.setToolTip("Seleccionar imágenes para visualizar")
        self.open_button.setFixedWidth(125)
        self.open_button.setFixedHeight(60)
        self.open_button.clicked.connect(self.open_files)
        controls_layout.addWidget(self.open_button)

        # Botón Carpeta Capturas
        self.captures_button = QPushButton('📁 Capturas')
        self.captures_button.setToolTip("Abrir carpeta de capturas del sistema")
        self.captures_button.setFixedWidth(125)
        self.captures_button.setFixedHeight(60)
        self.captures_button.clicked.connect(self.load_captures_folder)
        self.captures_button.hide()
        controls_layout.addWidget(self.captures_button)

        controls_layout.addStretch()

        # Navegación
        self.home_button = QPushButton('🏠 Inicio')
        self.home_button.setToolTip("Ir a la primera página")
        self.home_button.setFixedWidth(95)
        self.home_button.setFixedHeight(60)
        self.home_button.clicked.connect(self.go_to_home)
        
        self.prev_button = QPushButton('⏪ Anterior')
        self.prev_button.setToolTip("Página anterior")
        self.prev_button.setFixedWidth(95)
        self.prev_button.setFixedHeight(60)
        self.prev_button.clicked.connect(self.prev_page)
        
        self.page_label = QLabel("Página 1 / 1")
        self.page_label.setStyleSheet("color: white; padding: 0 10px;")
        
        self.next_button = QPushButton('⏩ Siguiente')
        self.next_button.setToolTip("Página siguiente")
        self.next_button.setFixedWidth(95)
        self.next_button.setFixedHeight(60)
        self.next_button.clicked.connect(self.next_page)

        # Botón Cerrar
        self.close_button = QPushButton('❌ Clean Select')
        self.close_button.setToolTip("Cerrar visor de imágenes")
        self.close_button.setFixedWidth(125)
        self.close_button.setFixedHeight(60)
        self.close_button.clicked.connect(self._clear_stack)

        controls_layout.addWidget(self.home_button)
        controls_layout.addWidget(self.prev_button)
        controls_layout.addWidget(self.page_label)
        controls_layout.addWidget(self.next_button)
        controls_layout.addWidget(self.close_button)

        self.main_layout.addWidget(self.controls_panel)

        # Estado inicial de botones
        self._update_navigation_buttons()
        self.message()

    def _apply_styles(self):
        """Aplica estilos oscuros del sistema de vigilancia"""
        self.setStyleSheet("""
            ImageViewerWidget {
                background-color: #1a1a2e;
            }
            QPushButton {
                background-color: #1f1f2e;
                color: #ffffff;
                border: 2px solid #0f3460;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 11px;
                font-weight: bold;
                min-height: 35px;
            }
            QPushButton:hover {
                background-color: #00c3ff;
                color: #000000;
                border-color: #00c3ff;
            }
            QPushButton:pressed {
                background-color: #0099cc;
            }
            QPushButton:disabled {
                background-color: #333333;
                color: #666666;
                border-color: #333333;
            }
            QLabel {
                color: #ffffff;
            }
            QScrollArea {
                border: none;
            }
        """)

    ##====================================================================================
    # MÉNSAJE DE BIENVENIDA AL SOF...
    ##====================================================================================
    def message(self):

        MSN = """
        ═════════════════════════════════════════
        🔥 Visor de Imágenes Múltiple - MÓDULO PARA SISTEMA DE VIGILANCIA 🔥
        Versión           : v-05
        Framework    : PyQt5
        Integración    : Sistema_de_Vigilancia_Profesional_v5.py

        Desarrollado por: Cristian M. Veliz Cano
        ═════════════════════════════════════════ 
        """

        QMessageBox.information(self, "INFORMACIÓN:", F"{MSN}")

    # =========================
    # 🎵 Centrar App
    # =========================
    def center_on_screen(self):

        screen = QApplication.primaryScreen().availableGeometry()
        w, h = 1000, 700
        x = (screen.width() - w) // 2
        y = (screen.height() - h) // 2 + 10
        self.setGeometry(x, y, w, h)

    ##====================================================================================
    # MÉTODOS DE CARGA DE IMÁGENES
    ##====================================================================================
    
    def open_files(self):
        """Abre diálogo para seleccionar imágenes"""
        self._clear_stack()
        
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        
        files, _ = QFileDialog.getOpenFileNames(
            self, 
            "Seleccionar Imágenes", 
            "", 
            "Archivos de Imagen (*.png *.jpg *.jpeg *.bmp *.gif *.webp *.tiff *.ico);;Todos los archivos (*)",
            options=options
        )
        
        if files:
            
            self.image_paths = files
            self._create_pages()
            self._update_counter()

    def load_captures_folder(self):
        """Carga automáticamente las imágenes de la carpeta de capturas"""
        self._clear_stack()
        
        if not os.path.exists(self.carpeta_capturas):
            self.counter_label.setText("Carpeta no encontrada")
            return
        
        # Buscar imágenes en la carpeta
        image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp', '.tiff', '.ico')
        self.image_paths = [
            os.path.join(self.carpeta_capturas, f) 
            for f in os.listdir(self.carpeta_capturas)
            if f.lower().endswith(image_extensions)
        ]
        
        # Ordenar por fecha de modificación (más recientes primero)
        self.image_paths.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        
        if self.image_paths:
            self._create_pages()
            self._update_counter()
        else:
            self.counter_label.setText("0 imágenes en capturas")

    def _update_counter(self):
        """Actualiza el contador de imágenes"""
        total = len(self.image_paths)
        self.counter_label.setText(f"{total} imagen{'es' if total != 1 else ''}")

    ##====================================================================================
    # CREACIÓN DE PÁGINAS (GRID DE IMÁGENES)
    ##====================================================================================
    
    def _create_pages(self):
        """Crea las páginas con grid de imágenes"""
        if not self.image_paths:
            return
        
        # Calcular número de páginas (20 imágenes por página = 4x5)
        images_per_page = 20
        num_pages = (len(self.image_paths) + images_per_page - 1) // images_per_page
        
        for page_num in range(num_pages):
            page = QWidget()
            page_layout = QGridLayout(page)
            page_layout.setContentsMargins(10, 10, 10, 10)
            page_layout.setSpacing(10)
            
            # Crear grid de 4x5
            for i in range(images_per_page):
                index = page_num * images_per_page + i
                if index >= len(self.image_paths):
                    break
                
                image_path = self.image_paths[index]
                row = i // 5
                col = i % 5
                
                # Crear widget contenedor para la imagen
                image_container = self._create_image_widget(image_path)
                page_layout.addWidget(image_container, row, col)
            
            self.stacked_widget.addWidget(page)
        
        self.current_page = 0
        self.stacked_widget.setCurrentIndex(0)
        self._update_navigation_buttons()
        self._update_page_label()

    def _create_image_widget(self, image_path):
        """Crea un widget para mostrar una imagen con su nombre"""
        container = QFrame()
        container.setFrameShape(QFrame.StyledPanel)
        container.setStyleSheet("""
            QFrame {
                background-color: #252525;
                border: 2px solid #333333;
                border-radius: 5px;
            }
            QFrame:hover {
                border: 2px solid #00c3ff;
            }
        """)
        
        layout = QVBoxLayout(container)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(3)
        
        # Imagen
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            # Escalar manteniendo proporción
            scaled_pixmap = pixmap.scaled(
                180, 180, 
                Qt.KeepAspectRatio, 
                Qt.SmoothTransformation
            )
            
            img_label = QLabel()
            img_label.setPixmap(scaled_pixmap)
            img_label.setAlignment(Qt.AlignCenter)
            img_label.setCursor(Qt.PointingHandCursor)
            
            # Click para abrir
            img_label.mousePressEvent = lambda e, path=image_path: self._open_image(path)
            
            layout.addWidget(img_label)
        
        # Nombre del archivo
        name = os.path.splitext(os.path.basename(image_path))[0]
        # Truncar nombre si es muy largo
        if len(name) > 20:
            name = name[:17] + "..."
        
        name_label = QLabel(name)
        name_label.setFont(QFont('Segoe UI', 8))
        name_label.setStyleSheet("color: #aaaaaa;")
        name_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(name_label)
        
        return container

    ##====================================================================================
    # NAVEGACIÓN
    ##====================================================================================
    
    def go_to_home(self):
        """Va a la primera página"""
        self.current_page = 0
        self.stacked_widget.setCurrentIndex(self.current_page)
        self._update_navigation_buttons()
        self._update_page_label()

    def prev_page(self):
        """Página anterior"""
        if self.current_page > 0:
            self.current_page -= 1
            self.stacked_widget.setCurrentIndex(self.current_page)
            self._update_navigation_buttons()
            self._update_page_label()

    def next_page(self):
        """Página siguiente"""
        if self.current_page < self.stacked_widget.count() - 1:
            self.current_page += 1
            self.stacked_widget.setCurrentIndex(self.current_page)
            self._update_navigation_buttons()
            self._update_page_label()

    def _update_page_label(self):
        """Actualiza el label de página"""
        total = self.stacked_widget.count()
        if total > 0:
            self.page_label.setText(f"Página {self.current_page + 1} / {total}")
        else:
            self.page_label.setText("Página 1 / 1")

    def _update_navigation_buttons(self):
        """Actualiza el estado de los botones de navegación"""
        total_pages = self.stacked_widget.count()
        
        self.home_button.setEnabled(total_pages > 1 and self.current_page > 0)
        self.prev_button.setEnabled(self.current_page > 0)
        self.next_button.setEnabled(self.current_page < total_pages - 1)

    ##====================================================================================
    # ACCIONES
    ##====================================================================================
    
    def _open_image(self, image_path):
        '''Abre una imagen con el visor predeterminado de la Aplicación sin Necesitar la del Sistema'''

        try:

            self.image_opened.emit(image_path)

            dialog_i = Image_Viuwer(image_path, self)
            dialog_i.exec_()

        except Exception as e:
            print('Error 8')
            print(e)

    def _clear_stack(self):
        """Limpia todas las páginas del stacked widget"""
        for i in reversed(range(self.stacked_widget.count())):
            widget = self.stacked_widget.widget(i)
            self.stacked_widget.removeWidget(widget)
            widget.deleteLater()
        
        self.current_page = 0
        self.image_paths = []

    def _request_close(self):
        """Solicita cerrar el widget"""
        self.request_close.emit(self)

    ##====================================================================================
    # MÉTODOS PÚBLICOS PARA INTEGRACIÓN
    ##====================================================================================
    
    def reload(self):
        """Recarga las imágenes de la carpeta de capturas"""
        self.load_captures_folder()

    def set_captures_folder(self, folder_path):
        """Establece una carpeta de capturas personalizada"""
        self.carpeta_capturas = folder_path
        os.makedirs(self.carpeta_capturas, exist_ok=True)

    def get_current_image(self):
        """Retorna la ruta de la imagen actual (si hay alguna seleccionada)"""
        if self.image_paths and self.current_page >= 0:
            return self.image_paths[self.current_page]
        return None

    ##====================================================================================
    # EVENTOS
    ##====================================================================================
    
    def mousePressEvent(self, event):
        """Detecta clicks en el widget"""
        self.clicked.emit(self)
        super().mousePressEvent(event)

    def keyPressEvent(self, event):
        """Manejo de teclas"""
        if event.key() == Qt.Key_Escape:
            self._request_close()
        elif event.key() == Qt.Key_Left:
            self.prev_page()
        elif event.key() == Qt.Key_Right:
            self.next_page()
        elif event.key() == Qt.Key_Home:
            self.go_to_home()
        else:
            super().keyPressEvent(event)

##====================================================================================
# DIÁLOGO DE DEFINICION F1
##====================================================================================
class Image_Viuwer(QDialog):

    def __init__(self, image, parent=None):
        super().__init__(parent)

        self.setWindowTitle("→ Image Viuwer")
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setFixedSize(700, 600)
        self.setModal(True)

        self.image_path = image
        self.image_paths_S = []
        self.Indice_Im = 0
        
        self.setStyleSheet("""
            QDialog {
                background-color: #000000;
            }
            QTextEdit {
                background-color: #0a0a0a;
                color: #00c3ff;
                border: 2px solid #00ff41;
                font-family: 'Consolas', monospace;
                font-size: 16px;
            }
            QPushButton {
                background-color: #0d1117;
                color: #00ff41;
                border: 2px solid #00ff41;
                padding: 0px;
                font-weight: bold;
                min-width:1em; padding:3px;
            }
            QPushButton:hover {
                background-color: #00ff41;
                color: #000000;
            }
        """)
        
        layout = QVBoxLayout(self)

        self.label = QLabel()
        #self.label.setFixedWidth(450)
        self.label.setFixedHeight(540)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: #00c3ff; font-size: 18px; font-weight: bold;")
        layout.addWidget(self.label)

        self.left_button = QPushButton('<', self)
        self.left_button.setStyleSheet("background-color: rgba(0, 0, 0, 50); color: white;")
        self.left_button.setFont(QFont('Arial', 20))
        self.left_button.clicked.connect(self.previous_image)
        self.left_button.setFixedSize(50, 50)
        self.left_button.move(25, self.height() // 2 - 25)
        #layout.addWidget(self.left_button)

        self.right_button = QPushButton('>', self)
        self.right_button.setStyleSheet("background-color: rgba(0, 0, 0, 50); color: white;")
        self.right_button.setFont(QFont('Arial', 20))
        self.right_button.clicked.connect(self.next_image)
        self.right_button.setFixedSize(50, 50)
        self.right_button.move(self.width() - 75, self.height() // 2 - 25)
        #layout.addWidget(self.right_button)
        
        self.btn = QPushButton()
        self.btn.setFixedHeight(45)
        self.btn.clicked.connect(self.close)
        layout.addWidget(self.btn)

        self.contando_im()
        self.Viewer_im()

## Metodo para Acortar el Titulo si este fuera muy Largo (Alternativo)
    def acortando_title(self, text, length=60):

        name, ext = os.path.splitext(text)

        if text:

            if len(text) <= length:
                return text

            else:
                return f"{' '.join(text[:length+1].split(' ')[0:-1])} ....{ext}"

## Metodo para Colocar en el Titulo Lo Que Deseemos que Hira, en este Caso el Titulo del Video
    def Actualizando_Title(self):

        if self.image_path == "":
            pass

        else:

            fpath, fname = os.path.split(self.image_path)
            title = Image_Viuwer.acortando_title(self, fname)
            print(title)

            self.btn.setText(f"{title}")

    def Viewer_im(self):
        """Abre una imagen con el visor predeterminado del sistema"""
        
        if sys.platform == 'win32':

            self.Actualizando_Title()            

            pix = QPixmap(self.image_path).scaled(600, 650, Qt.KeepAspectRatio)
            self.label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            self.label.setStyleSheet("""QLabel{background:black; border:1px solid #80ff00;}""")
            self.label.setPixmap(pix)
            self.label.setScaledContents(True)

                        # Click para abrir
            self.label.mousePressEvent = lambda e, path=self.image_path: self._open_image_CV2(path)

        else:
            import subprocess
            subprocess.call(['xdg-open', image_path])

    def contando_im(self):

        fpath, fname = os.path.split(self.image_path)
        self.directory = f"{fpath}/"
        print(fpath)

        # Buscar imágenes en la carpeta
        image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp', '.tiff', '.ico')
        self.image_paths_S = [
            os.path.join(self.directory, f"{dirpath}/{f}") 
            for dirpath, dirnames, filenames in os.walk(self.directory)
            for f in filenames
            if f.lower().endswith(image_extensions)
        ]

        ## print(self.image_paths_S)

        ##==========================================================================
        ##==========================================================================

    def next_image(self):

        if self.image_paths_S:

            self.Indice_Im = (self.Indice_Im + 1) % len(self.image_paths_S)
            print(f"Siguiente Imagen:  {self.image_paths_S[self.Indice_Im]}")
            self.update_image()

    def previous_image(self):

        if self.image_paths_S:

            self.Indice_Im = (self.Indice_Im - 1) % len(self.image_paths_S)
            self.Indice_Im = self.Indice_Im
            print(f"Anterior Imagen:  {self.image_paths_S[self.Indice_Im]}")
            self.update_image()

    def update_image(self):

        if self.image_paths_S:

            self.image_path = self.image_paths_S[self.Indice_Im]
            Image_Viuwer.Actualizando_Title(self)

            pixmap = QPixmap(self.image_paths_S[self.Indice_Im]).scaledToWidth(1000)
            pixmap = pixmap.scaledToHeight(500)
            
            self.label.setPixmap(pixmap)
            self.label.adjustSize()

            # Click para abrir
            self.label.mousePressEvent = lambda e, path=self.image_path: self._open_image_CV2(path)

        else:

            self.current_index = 0
            self.update_image()

    def _open_image_CV2(self, image_path):
        """Abre una imagen con el visor predeterminado del sistema"""
        
        if sys.platform == 'win32':

            try:

                fpath, fname = os.path.split(image_path)
                if fname.endswith(".gif") or fname.endswith(".GIF"):
                    return

                image = cv2.imread(r'{}'.format(image_path))
                image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
                cv2.namedWindow(f"{fname}",cv2.WINDOW_NORMAL)

                # Para Ver la Imagen dentro de la Ventana Emergente Image de CV2
                cv2.imshow(f"{fname}", image)
                cv2.waitKey(0)

            except Exception as e:
                print(e)
                QMessageBox.critical(self, "Error al Cargar", f"Se ha disparado un Error, el Error es:\
                    \n{e}\nNo Se Podra Cargar tu Imagen Intenta con Otra\nMuchas, Gracias...")

        else:
            import subprocess
            subprocess.call(['xdg-open', image_path])

        ##==========================================================================
        ##==========================================================================

    def resizeEvent(self, event):

        super().resizeEvent(event)
        self.left_button.move(25, self.height() // 2 - 25)
        self.right_button.move(self.width() - 75, self.height() // 2 - 25)

##====================================================================================
# EJEMPLO DE USO DIRECTO
##====================================================================================
if __name__ == '__main__':
    from PyQt5.QtCore import QTimer
    
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    
    # Crear widget de prueba
    widget = ImageViewerWidget()
    #widget.resize(1000, 700)
    widget.show()
    
    sys.exit(app.exec_())

##====================================================================================
##====================================================================================