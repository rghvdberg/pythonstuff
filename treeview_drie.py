import sys
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file system view - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.model = QFileSystemModel()
        self.model.setRootPath('/home/rob/Muziek')
        filter = ["*.wav","*.ogg"]
        self.model.setNameFilters(filter)
        self.model.setNameFilterDisables(0)
        root = self.model.setRootPath('/home/rob/Muziek')
        #print(root)
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(root)
 
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
        self.tree.doubleClicked.connect(self.test)
            
        self.tree.setWindowTitle("Dir View")
        self.tree.resize(640, 480)
        
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.tree)
        self.setLayout(windowLayout)
        
        self.show()
        
    def test(self, signal):
        print (signal)
        file_path=self.model().filePath(signal)
        print(file_path)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
