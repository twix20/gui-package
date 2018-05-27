import sys, base64, io, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QDateTime
from PyQt5 import QtCore, QtGui, QtWidgets

from GUI.MainFrameUI import Ui_Dialog as MainFrameUI
from GUI.CreateNewGuideUI import Ui_Dialog as CreateNewGuideUI
from Core.Database import *

class GuideDialog(QDialog):
	def __init__(self, parent = None, guide = None):
		super(GuideDialog, self).__init__(parent)
		self.ui = CreateNewGuideUI()
		self.ui.setupUi(self)

		self.setWindowTitle("Create new Guide" if guide is None else f"Edit guide {guide.guideId}")

		self.ui.buttonBox.accepted.connect(self.accept)
		self.ui.buttonBox.rejected.connect(self.reject)
		self.ui.btnChooseAvatar.clicked.connect(self.chooseAvatarFile)

		self.beingProcessedGuide = Guide("", "", "")

		if guide is not None:
			self.beingProcessedGuide = guide
			self.ui.txtBoxGuideTitle.setText(self.beingProcessedGuide.title)
			self.ui.txtAreaGuideText.setText(self.beingProcessedGuide.text)
	
	def chooseAvatarFile(self):
		fname, d = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd(),"Image files (*.jpg *.png)")

		if not fname:
			return

		img = QtGui.QImage(fname)
		ba = QtCore.QByteArray()
		buffer = QtCore.QBuffer(ba)
		buffer.open(QtCore.QIODevice.WriteOnly)
		img.save(buffer, 'PNG')
		base64_data = ba.toBase64().data()

		self.ui.btnChooseAvatar.setText('Choosen avatar file: ' + os.path.basename(fname))
		self.beingProcessedGuide.imageBase64 = base64_data

	def getCreatedGuide(self):
		self.beingProcessedGuide.title = self.ui.txtBoxGuideTitle.text()
		self.beingProcessedGuide.text = self.ui.txtAreaGuideText.toPlainText()

		return self.beingProcessedGuide

	# static method to create the dialog and return (guide, accepted)
	@staticmethod
	def getGuide(parent = None, guide = None):
		dialog = GuideDialog(parent, guide)
		result = dialog.exec_()
		newGuide = dialog.getCreatedGuide()
		return (newGuide, result == QDialog.Accepted)


class MainFrame(QDialog):
	def __init__(self, parent=None):
		super(MainFrame, self).__init__(parent=parent)
		self.ui = MainFrameUI()
		self.ui.setupUi(self)

		self.db = Database()

		#Events
		self.ui.btnRateGuide.clicked.connect(self.rate_guide_clicked)
		self.ui.btnAddComment.clicked.connect(self.add_comment_clicked)
		self.ui.btnCreateNewGuide.clicked.connect(self.create_new_guide_clicked)
		self.ui.btnEditGuide.clicked.connect(self.edit_current_guide_clicked)

		self.ui.cbxGuides.currentIndexChanged.connect(self.cbx_guides_changed)

		#Rating combobox
		for i in range(1, 6):
			self.ui.cbxRating.addItem(str(i), i)

		self.update_guides_GUI()

		self.cbx_guides_changed()
		self.update_current_guide_GUI()

	def cbx_guides_changed(self):
		self.set_current_guide(self.ui.cbxGuides.currentData())

		if self.currentGuide is not None:
			self.update_current_guide_GUI()

	def rate_guide_clicked(self):
		selectedVoteValue = self.ui.cbxRating.currentData()
		self.currentGuide.rate(selectedVoteValue)

		self.db.addOrUpdateGuide(self.currentGuide)
		self.update_current_guide_GUI()
	
	def add_comment_clicked(self):
		commentText = self.ui.leComment.text().strip()
		if not commentText:
			return

		self.currentGuide.add_comment(Comment(commentText))
		self.ui.leComment.setText("")

		self.db.addOrUpdateGuide(self.currentGuide)
		self.update_current_guide_GUI()
	
	def create_new_guide_clicked(self):
		newGuide, ok = GuideDialog.getGuide()

		if ok:
			self.db.addOrUpdateGuide(newGuide)
			self.update_guides_GUI()
	
	def edit_current_guide_clicked(self):
		editedGuide, ok = GuideDialog.getGuide(None, self.currentGuide)

		if ok:
			self.db.addOrUpdateGuide(editedGuide)
			self.update_guides_GUI()

	def update_guides_GUI(self):
		self.ui.cbxGuides.clear()
		for g in self.db.getAllGuides():
			self.ui.cbxGuides.addItem(g.title, g)
		
		self.set_current_guide(self.ui.cbxGuides.currentData())

	def update_current_guide_GUI(self):
		g = self.currentGuide
		self.ui.txtEditGuideText.setText(g.text)
		self.ui.lblGuideRating.setText("{:.2f}".format(g.rating()))
		self.ui.txtEditComments.setText("{}\n".format("-"*39).join('{:15} Date: {:%d %b %Y %H:%M}\n{}\n'.format("Comment:", c.date_commented, c.text) for c in g.comments))

		img = QtGui.QImage()
		img.loadFromData(base64.b64decode(g.imageBase64) , 'PNG')
		img = img.scaled(110, 110, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation) 

		self.ui.lblGuideAvatar.setPixmap(QtGui.QPixmap.fromImage(img))

	def set_current_guide(self, guide):
		if guide is None:
			return

		self.currentGuide = guide
		self.update_current_guide_GUI()
		

if __name__ == "__main__":
	app = QApplication(sys.argv)
	mainFrame = MainFrame()
	mainFrame.show()
	sys.exit(app.exec_())
