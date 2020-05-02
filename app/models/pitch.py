class Pitch:
    """
    Pitch class to define Pitch objects
    """
    all_pitches = []

    def __init__ (self, your_pitch):
        self.your_pitch = your_pitch

    def save_pitch(self):
        Pitch.all_pitches.append(self)

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()