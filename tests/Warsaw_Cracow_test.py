import unittest
from Warsaw_vs_Cracow import transcribe_words_Cracow
from Warsaw_vs_Cracow import transcribe_words_Warsaw

class TestInterLexProcesses(unittest.TestCase):

    def test_prevocalic_Cracow(self):
        self.assertEqual(transcribe_words_Cracow('Niech żyje Janusz jak najdłużej!'), 'ɲɛɣ ʐɨjɛ januʐ jaɡ najdwuʐɛj!')
        self.assertEqual(transcribe_words_Cracow('Chłop jak ja.'), 'xwɔb jaɡ ja.')
        self.assertEqual(transcribe_words_Cracow('racz nie przeszkadzać'), 'radʐ ɲɛ pʂɛʂkadzatɕ')

    def test_prevocalic_Warsaw(self):
        self.assertEqual(transcribe_words_Warsaw('Niech żyje Janusz jak najdłużej!'), 'ɲɛɣ ʐɨjɛ januʂ jak najdwuʐɛj!')
        self.assertEqual(transcribe_words_Warsaw('Chłop jak ja.'), 'xwɔp jak ja.')
        self.assertEqual(transcribe_words_Warsaw('racz nie przeszkadzać'), 'ratʂ ɲɛ pʂɛʂkadzatɕ')

if __name__ == '__main__':
    unittest.main()