import unittest
from ipa_transcribe_polish import transcribe

class TestNotationalConventions(unittest.TestCase):

    def test_clusters(self):
        self.assertEqual(transcribe('cienki'), 'tɕɛŋkʲi')
        self.assertEqual(transcribe('poczochrać'), 'pɔtʂɔxratɕ')
        self.assertEqual(transcribe('poszarzeni'), 'pɔʂaʐɛɲi')
        self.assertEqual(transcribe('udźwig'), 'udʑvʲik')

    def test_i_deletion(self):
        self.assertEqual(transcribe('wyziębiony'), 'vɨʑɛmbʲjɔnɨ')
        self.assertEqual(transcribe('podziało'), 'pɔdʑawɔ')
        self.assertEqual(transcribe('ciecierzyca'), 'tɕɛtɕɛʐɨtsa')
        self.assertEqual(transcribe('nasiusiała'), 'naɕuɕawa')

    def test_i_replacement(self):
        self.assertEqual(transcribe('pięknie'), 'pʲjɛŋkɲɛ')
        self.assertEqual(transcribe('babia'), 'babʲja')
        self.assertEqual(transcribe('liliana'), 'lʲilʲjana')
        self.assertEqual(transcribe('wywiad'), 'vɨvʲjat')


if __name__ == "__main__":
    unittest.main()