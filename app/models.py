class Pitch:
    """
    Pitch class to define Pitch objects
    """
    all_pitches = []

    def __init__ (self,author, your_pitch, date_posted):
        self.your_pitch = your_pitch
        self.author = author
        self.date_posted = date_posted

    def save_pitch(self):
        Pitch.all_pitches.append(self)


    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()

class