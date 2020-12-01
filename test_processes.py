import unittest
from ipa_transcribe_polish import transcribe


class TestProcesses(unittest.TestCase):

    def test_final_devoicing(self):
        self.assertEqual(transcribe('standard'), 'standart')
        self.assertEqual(transcribe('wąż'), 'vɔ̃w̃ʂ')
        self.assertEqual(transcribe('bug'), 'buk')

    def test_denasalise_nasal_assimilation(self):
        self.assertEqual(transcribe('mąka'), 'mɔŋka')
        self.assertEqual(transcribe('gęsty'), 'ɡɛ̃w̃stɨ')
        self.assertEqual(transcribe('rąbać'), 'rɔmbatɕ')
        self.assertEqual(transcribe('podjęli'), 'pɔdʲjɛlʲi')
        self.assertEqual(transcribe('stanął'), 'stanɔw')
        self.assertEqual(transcribe('pieniądz'), 'pʲjɛɲɔɳts')
        self.assertEqual(transcribe('pędzić'), 'pɛɲdʑitɕ')
        self.assertEqual(transcribe('pójdą'), 'pujdɔ̃w̃')
        self.assertEqual(transcribe('kręty'), 'krɛntɨ')
        self.assertEqual(transcribe('pójdę'), 'pujdɛ')

    def test_progressive_voicing_morphological(self):
        self.assertEqual(transcribe('jakże'), 'jaɡʐɛ')
        self.assertEqual(transcribe('wszakżeż'), 'fʂaɡʐɛʂ')
        self.assertEqual(transcribe('paśże'), 'paʑʐɛ')

    def test_progressive_devoicing(self):
        self.assertEqual(transcribe('świat'), 'ɕfʲjat')
        self.assertEqual(transcribe('przetrzyma'), 'pʂɛtʂɨma')
        self.assertEqual(transcribe('wycwanić'), 'vɨtsfaɲitɕ')

    def test_progressive_voicing(self):
        self.assertEqual(transcribe('poczdam'), 'pɔdʐdam')
        self.assertEqual(transcribe('prośba'), 'prɔʑba')

    def test_regressive_devoicing(self):
        self.assertEqual(transcribe('babka'), 'bapka')
        self.assertEqual(transcribe('rozpacz'), 'rɔspatʂ')

    def surface_palatalisation(self):
        self.assertEqual(transcribe('kibitki'), 'kʲibʲitkʲi')
        self.assertEqual(transcribe('kwiatki'), 'kfʲjatkʲi')
        self.assertEqual(transcribe('kolie'), 'kɔlʲjɛ')
        self.assertEqual(transcribe('robi'), 'rɔbʲi')

if __name__ == '__main__':
    unittest.main()