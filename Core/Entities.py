from datetime import datetime

class Guide():

    def __init__(self, title, text, imageBase64):
        self.guideId = None
        self.comments = []
        
        self.rating_total = 5.0
        self.rating_votes_count = 1

        self.title = title
        self.text = text
        self.imageBase64 = imageBase64

    def rate(self, rateValue):
        self.rating_total += rateValue
        self.rating_votes_count += 1

    def rating(self):
        return self.rating_total / self.rating_votes_count

    def add_comment(self, comment):
        self.comments.append(comment)

class Comment():
    def __init__(self, text):
        self.text = text
        self.date_commented = datetime.now()


