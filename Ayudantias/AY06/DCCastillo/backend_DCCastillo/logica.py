from PyQt5.QtCore import QObject,pyqtSignal


class Logica(QObject):
    
    senal_ver_dormir = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        
    def ver_dormir(self,hora):
        separado = hora.split(":")
        if (int(separado[0]) >= 20) or ( int(separado[0]) <= 5 and int(separado[0]) >= 0 ):
            self.senal_ver_dormir.emit()
        else:
            print("No puedes dormir en este momento")