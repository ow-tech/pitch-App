import unittest
from models import pitch

Pitch = pitch.Pitch

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the pitch class

    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Pitch("I recently graduated from college with a degree in communications. I worked on the college newspaper as a reporter, and eventually, as the editor of the arts section. I'm looking for a job that will put my skills as a journalist to work")


    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))


if __name__ == '__main__':
    unittest.main()