samples = {
    'mąka':'mɔŋka',
    'męka':'mɛŋka',
    'gęsty': 'g ̃ɛ̃w stɨ',
    'podążmy': 'pɔd ̃ɔ̃w ʐmɨ',
    'węchu': 'v ̃ɛ̃w xu',
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
    'trąd': 'trɔnt'
}

from  ipa_transcribe_polish import transcribe

for sample in samples:
    print(sample, '-', transcribe(sample), '-', samples[sample])