from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl
import json
import os
import time

class Gui(QWidget):

    def __init__(self):
        super().__init__()

        self.arx = '.test'
        self.cargando = 0
        self.setGeometry(0, 0, 1200, 750)

        # main window
        self.MainWindow = QMainWindow()
        self.centralwidget = QWidget(self.MainWindow)
        self.MainWindow.setCentralWidget(self.centralwidget)

        # reproductor
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()
        self.mediaPlayer.setVideoOutput(videowidget)

        openBtn = QPushButton('Load Video')
        openBtn.clicked.connect(self.open_file)

        # para busqueda en tiempo
        self.Tsearch = QLineEdit()
        self.Tsearch.setFixedWidth(100)
        TsearchBtn = QPushButton('Go to Time >>')
        TsearchBtn.setFixedWidth(100)
        TsearchBtn.clicked.connect(self.go_t)

        slowBtn = QPushButton('Slow')
        slowBtn.clicked.connect(self.slow_mode)
        normalBtn = QPushButton('Normal')
        normalBtn.clicked.connect(self.normal_mode)
        fastBtn = QPushButton('Fast')
        fastBtn.clicked.connect(self.fast_mode)

        h0 = QHBoxLayout()
        
        h0.addWidget(slowBtn)
        h0.addWidget(normalBtn)
        h0.addWidget(fastBtn)

        h2 = QHBoxLayout()

        h2.addWidget(openBtn)
        h2.addWidget(self.Tsearch)
        h2.addWidget(TsearchBtn)


        # Layout 1 --------------------------------
        vboxLayout1 = QVBoxLayout()
        vboxLayout1.addLayout(h0)
        vboxLayout1.addWidget(videowidget)
        
        vboxLayout1.addLayout(h2)

        # Layout 2 ------------------------------
        vboxLayout2 = QVBoxLayout()

        # equipos
        self.equipo1 = QLineEdit()
        self.equipo1.setFixedWidth(200)
        self.equipo1.setText('Team 1')

        self.equipo2 = QLineEdit()
        self.equipo2.setFixedWidth(200)
        self.equipo2.setText('Team 2')

        h1 = QVBoxLayout()
        h1.addWidget(self.equipo1)
        h1.addWidget(self.equipo2)

        vboxLayout2.addLayout(h1)

        # boton cargar nombre de equipos
        self.cargarEquiposBtn = QPushButton('Start')
        self.cargarEquiposBtn.clicked.connect(self.cargarEquipos)
        self.cargarEquiposBtn.setFixedWidth(200)
        vboxLayout2.addWidget(self.cargarEquiposBtn)

        # boton comenzar rally
        self.inicioRallyBtn1 = QPushButton('Service Team 1')
        self.inicioRallyBtn1.clicked.connect(self.inicioRally1)
        self.inicioRallyBtn1.setEnabled(False)
        self.inicioRallyBtn1.setFixedWidth(200)
        self.inicioRallyBtn1.setFixedHeight(50)
        vboxLayout2.addWidget(self.inicioRallyBtn1)

        # boton comenzar rally
        self.inicioRallyBtn2 = QPushButton('Service Team 2')
        self.inicioRallyBtn2.clicked.connect(self.inicioRally2)
        self.inicioRallyBtn2.setEnabled(False)
        self.inicioRallyBtn2.setFixedWidth(200)
        self.inicioRallyBtn2.setFixedHeight(50)
        vboxLayout2.addWidget(self.inicioRallyBtn2)

        # info text
        self.info0 = QLabel()
        font1 = self.info0.font()
        font1.setPointSize(20)
        self.info0.setFont(font1)
        self.info0.setText('')
        self.info0.setFixedWidth(200)
        self.info0.setFixedHeight(100)
        vboxLayout2.addWidget(self.info0)

        # remover ultimo evento cargado 
        self.removerEventoBtn = QPushButton('Remove last event')
        self.removerEventoBtn.clicked.connect(self.removerEvento)
        self.removerEventoBtn.setEnabled(False)
        self.removerEventoBtn.setFixedWidth(200)
        self.removerEventoBtn.setFixedHeight(50)
        vboxLayout2.addWidget(self.removerEventoBtn)

        # boton fin rally
        self.finRallyBtn1 = QPushButton('Point Team 1')
        self.finRallyBtn1.clicked.connect(self.finRally1)
        self.finRallyBtn1.setEnabled(False)
        self.finRallyBtn1.setFixedWidth(200)
        self.finRallyBtn1.setFixedHeight(50)
        vboxLayout2.addWidget(self.finRallyBtn1)

        self.finRallyBtn2 = QPushButton('Point Team 2')
        self.finRallyBtn2.clicked.connect(self.finRally2)
        self.finRallyBtn2.setEnabled(False)
        self.finRallyBtn2.setFixedWidth(200)
        self.finRallyBtn2.setFixedHeight(50)
        vboxLayout2.addWidget(self.finRallyBtn2)

        # main layout
        mainLayout = QHBoxLayout()
        mainLayout.addLayout(vboxLayout1)
        mainLayout.addLayout(vboxLayout2)
        self.setLayout(mainLayout)

    def cargarEquipos(self):
        self.eq1 = self.equipo1.text()
        self.eq2 = self.equipo2.text()

        self.inicioRallyBtn1.setText('Service %s' % self.eq1)
        self.inicioRallyBtn2.setText('Service %s' % self.eq2)

        self.inicioRallyBtn1.setEnabled(True)
        self.inicioRallyBtn2.setEnabled(True)

        self.finRallyBtn1.setText('Point %s' % self.eq1)
        self.finRallyBtn2.setText('Point %s' % self.eq2)

        self.cargarEquiposBtn.setEnabled(False)

    def inicioRally1(self):
        t0 = self.mediaPlayer.position()
        self.newRally = {'t0': t0, 'events': [], 'eq1': self.eq1, 'eq2': self.eq2, 'service': self.eq1}
        self.info0.setText("N = 0\nT = 0.0")
        self.finRallyBtn1.setEnabled(True)
        self.finRallyBtn2.setEnabled(True)
        self.removerEventoBtn.setEnabled(True)
        self.cargando = 1

    def inicioRally2(self):
        t0 = self.mediaPlayer.position()
        self.newRally = {'t0': t0, 'events': [], 'eq1': self.eq1, 'eq2': self.eq2, 'service': self.eq2}
        self.info0.setText("N = 0\nT = 0.0")
        self.finRallyBtn1.setEnabled(True)
        self.finRallyBtn2.setEnabled(True)
        self.removerEventoBtn.setEnabled(True)
        self.cargando = 1

    def cargarEvento(self):
        if self.cargando:
            t = self.mediaPlayer.position()
            self.newRally['events'].append(t)
            self.info0.setText("N = %d\nT = %.3f " % (len(self.newRally['events']), (self.newRally['events'][-1] - self.newRally['events'][0]) / 1000.))
        else:
            print("[ERROR] Before saving an event, you should initialize the rally")

    def removerEvento(self):
        self.newRally['events'].pop()
        self.info0.setText("N = %d\nT = %.3f " % (len(self.newRally['events']), (self.newRally['events'][-1] - self.newRally['events'][0]) / 1000.))

    def finRally1(self):
        self.newRally['win'] = self.eq1
        js = json.dumps(self.newRally)
        f = open(self.arx, "a")
        f.write(js)
        f.write('\n')
        f.close()
        self.info0.setText("")
        self.finRallyBtn1.setEnabled(False)
        self.finRallyBtn2.setEnabled(False)
        self.removerEventoBtn.setEnabled(False)
        self.cargando = 0

    def finRally2(self):
        self.newRally['win'] = self.eq2
        js = json.dumps(self.newRally)
        f = open(self.arx, "a")
        f.write(js)
        f.write('\n')
        f.close()
        self.info0.setText("")
        self.finRallyBtn1.setEnabled(False)
        self.finRallyBtn2.setEnabled(False)
        self.removerEventoBtn.setEnabled(False)
        self.cargando = 0

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Load Video")
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            print(self.mediaPlayer)
            self.arx = "data/%s_%d.dat" % (filename.split('/')[-1], time.time())
            # Create the file at the selected path
            f = open(self.arx, "w")
            f.close()
            print('[Arx salida] : %s' % self.arx)

    def keyPressEvent(self, event):
        key = event.text()
        if key == 's':
            if self.mediaPlayer.state() == 1:
                self.mediaPlayer.pause()
            else:
                self.mediaPlayer.play()
        elif key == 'd':
            pos = self.mediaPlayer.position()
            self.mediaPlayer.setPosition(pos + 2000)
        elif key == 'a':
            pos = self.mediaPlayer.position()
            if pos > 2000:
                self.mediaPlayer.setPosition(pos - 2000)
        elif key == 'c':
            pos = self.mediaPlayer.position()
            self.mediaPlayer.setPosition(pos + 60000)
        elif key == 'z':
            pos = self.mediaPlayer.position()
            if pos > 60000:
                self.mediaPlayer.setPosition(pos - 60000)
        elif key == 'e':
            pos = self.mediaPlayer.position()
            self.mediaPlayer.setPosition(pos + 30)
        elif key == 'q':
            pos = self.mediaPlayer.position()
            if pos > 60000:
                self.mediaPlayer.setPosition(pos - 30)
        elif key == 'j':
            self.cargarEvento()

    def go_t(self):
        t = int(self.Tsearch.text())
        T = self.mediaPlayer.duration()
        if t < T:
            self.mediaPlayer.setPosition(t)
        else:
            print("El video no es tan largo...")
            print("Duracion :", T)
            self.mediaPlayer.setPosition(T - 5000)
    
    def slow_mode(self):
        self.mediaPlayer.setPlaybackRate(0.5)

    def fast_mode(self):
        self.mediaPlayer.setPlaybackRate(2)

    def normal_mode(self):
        self.mediaPlayer.setPlaybackRate(1)

    def mousePressEvent(self, event):
        try:
            QApplication.focusWidget().clearFocus()
        except:
            None