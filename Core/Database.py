import shelve, re

from .Entities import *

class Database():
	guides_table = 'test_guides.db'
	GUIDES = 'guides'

	def __init__(self):
		self.ensureDbData()

	def populateWithTemplate(self):

		img64 = open("img", "r").read()
		g_b = Guide("Title best Guide", """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse ac lacus tincidunt, rutrum eros vel, faucibus lacus. Vestibulum commodo, mi nec hendrerit vulputate, magna eros ultricies urna, a faucibus risus turpis non diam. Cras tincidunt felis a vehicula finibus. Aliquam pretium vestibulum purus. Etiam pellentesque aliquet neque, et finibus elit fringilla vitae. Cras semper est et ipsum consectetur pretium. Nam elementum accumsan nibh a posuere.\n\nSed sit amet diam scelerisque, viverra nunc sollicitudin, mattis justo. Cras nec tempus justo, ut semper magna. Quisque hendrerit vulputate nibh et feugiat. Nulla sed vehicula lorem. Phasellus efficitur sed lectus et viverra. Nam pretium magna eu rutrum tincidunt. Praesent velit nunc, imperdiet pharetra sapien in, tristique facilisis ex. Morbi lorem nibh, eleifend in elit eu, fringilla tristique magna. Sed purus sem, auctor maximus nulla at, tempor tempus lectus. Integer quis tellus at risus egestas lacinia gravida ac sem.\n\nPraesent congue ligula molestie nulla viverra, vitae commodo ligula suscipit. Donec magna ipsum, condimentum eget eleifend lobortis, vestibulum ut lorem. In feugiat massa est, et dictum orci aliquet auctor. Pellentesque quis lorem eleifend, euismod risus a, faucibus nibh. Integer rutrum sodales tincidunt. Maecenas sit amet iaculis ante, vitae accumsan lacus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae;""", img64)
		g_b.comments = [Comment("Great"), Comment("Pretty  good"), Comment("Pretty  good"), Comment("Pretty  good"), Comment("Pretty  good"), Comment("Pretty  good"), Comment("Pretty  good")]


		g_w = Guide("Worst guide", "The worst", img64)
		g_w.rating_total = 1.0
		g_w.comments = [Comment("WOrts"), Comment("the worst")]

		for x in [g_b, g_w]:
			self.addOrUpdateGuide(x)


	def ensureDbData(self):
		with shelve.open(Database.guides_table) as db:
			if Database.GUIDES not in db:
				db[Database.GUIDES] = {}
			else:
				print('db exists')
				return

		print('db doesnt exist, seeding')
		self.populateWithTemplate()

	def getNextFreeSequenceId(self):
		with shelve.open(Database.guides_table) as db:
			return max((int(s) for s in db[Database.GUIDES].keys()), default = 0) + 1

	def getAllGuides(self):
		with shelve.open(Database.guides_table) as db:
			return db[Database.GUIDES].values()

	def getGuideById(self, guideId):
		with shelve.open(Database.guides_table) as db:
			return db[Database.GUIDES].get(guideId)

	def addOrUpdateGuide(self, guide):
		exitstingGuide = self.getGuideById(guide.guideId)
		if exitstingGuide is None:
			guide.guideId = self.getNextFreeSequenceId()

		with shelve.open(Database.guides_table, writeback=True) as db:
			db[Database.GUIDES][guide.guideId] = guide
