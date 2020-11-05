samples = {
    'biały':'bʲjawɨ',
    'ziemia':'ʑɛmʲja',
    'robi': 'rɔbʲi',
    'więdnie': 'vʲj ̃ɛ̃w dɲɛ',
    'powie': 'pɔvʲjɛ',
    'kwiatki': 'kfʲjatkʲi',
    'wiewiórka': 'vʲjɛvʲjurka',
    'kibitki': 'kʲibʲitkʲi',
    'wiwisekcja': 'vʲivʲisɛktsja',
    'kitki': 'kʲitkʲi',
    'operetki': 'ɔpɛrɛtkʲi',
    'papier':'papʲjɛr',
    'kolie':'kɔlʲjɛ'
}

from  ipa_transcribe_polish import transcribe

for sample in samples:
    print(sample, '-', transcribe(sample), '-', samples[sample])