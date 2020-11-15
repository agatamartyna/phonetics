samples = {
    'mąka':'mɔŋka',
    'męka':'mɛŋka',
    'gęsty': 'g̃ɛ̃wstɨ',
    'podążmy': 'pɔd̃ɔ̃wʐmɨ',
    'węchu': 'ṽɛ̃wxu',
    'rąbać': 'rɔmbatɕ',
    'ząb':'zɔmp',
    'tępy': 'tɛmpɨ',
    'wziął': 'vʑɔw',
    'podjęli': 'pɔdʲjɛlʲi',
    'pączek': 'pɔɳtʂɛk',
    'księdza': 'kɕɛɳdza',
    'pieniądz': 'pʲjɛɲɔɳts',
    'tęcza': 'tɛɳtʂa',
    'bęc': 'bɛɳts',
    'ręce':'rɛɳtsɛ',
    'pędzić': 'pɛɲdʑitɕ',
    'mącić': 'mɔɲtɕitɕ',
    'kręć':'krɛɲtɕ',
    'robię': 'rɔbʲjɛ',
    'kręty': 'krɛntɨ',
    'trąd': 'trɔnt',
    'pójdę': 'pujdɛ',
    'pójdą': 'pujd̃ɔ̃̃w'
}

from  ipa_transcribe_polish import transcribe

for sample in samples:
    print(sample, '-', transcribe(sample), '-', samples[sample])