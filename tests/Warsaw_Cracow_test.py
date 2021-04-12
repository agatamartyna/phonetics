import unittest
from phonetics.Warsaw_vs_Cracow import transcribe_text_Cracow
from phonetics.Warsaw_vs_Cracow import transcribe_text_Warsaw

class TestInterLexProcesses(unittest.TestCase):

    def test_prevocalic_Cracow(self):
        self.assertEqual(transcribe_text_Cracow('Niech żyje Janusz jak najdłużej!'), 'ɲɛɣ ʐɨjɛ januʐ jaɡ najdwuʐɛj!')
        self.assertEqual(transcribe_text_Cracow('Chłop jak ja.'), 'xwɔb jaɡ ja.')
        self.assertEqual(transcribe_text_Cracow('racz nie przeszkadzać'), 'radʐ ɲɛ pʂɛʂkadzatɕ')
        self.assertEqual(transcribe_text_Cracow('Paś owce'), 'paʑ ɔftsɛ')

    def test_prevocalic_Warsaw(self):
        self.assertEqual(transcribe_text_Warsaw('Niech żyje Janusz jak najdłużej!'), 'ɲɛɣ ʐɨjɛ januʂ jak najdwuʐɛj!')
        self.assertEqual(transcribe_text_Warsaw('Chłop jak ja.'), 'xwɔp jak ja.')
        self.assertEqual(transcribe_text_Warsaw('racz nie przeszkadzać'), 'ratʂ ɲɛ pʂɛʂkadzatɕ')
        self.assertEqual(transcribe_text_Warsaw('Paś owce'), 'paɕ ɔftsɛ')

if __name__ == '__main__':
    unittest.main()