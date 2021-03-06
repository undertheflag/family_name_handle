#encoding:utf-8

# map (final) constanant+tone to tone+constanan
mapConstTone2ToneConst = {'n1':  '1n',
                          'n2':  '2n',
                          'n3':  '3n',
                          'n4':  '4n',
                          'ng1': '1ng',
                          'ng2': '2ng',
                          'ng3': '3ng',
                          'ng4': '4ng',
                          'r1':  '1r',
                          'r2':  '2r',
                          'r3':  '3r',
                          'r4':  '4r'}

# map vowel+vowel+tone to vowel+tone+vowel
mapVowelVowelTone2VowelToneVowel = {'ai1': 'a1i',
                                    'ai2': 'a2i',
                                    'ai3': 'a3i',
                                    'ai4': 'a4i',
                                    'ao1': 'a1o',
                                    'ao2': 'a2o',
                                    'ao3': 'a3o',
                                    'ao4': 'a4o',
                                    'ei1': 'e1i',
                                    'ei2': 'e2i',
                                    'ei3': 'e3i',
                                    'ei4': 'e4i',
                                    'ou1': 'o1u',
                                    'ou2': 'o2u',
                                    'ou3': 'o3u',
                                    'ou4': 'o4u'}

# map vowel-number combination to unicode
mapVowelTone2Unicode = {'a1': 'ā',
                        'a2': 'á',
                        'a3': 'ǎ',
                        'a4': 'à',
                        'e1': 'ē',
                        'e2': 'é',
                        'e3': 'ě',
                        'e4': 'è',
                        'i1': 'ī',
                        'i2': 'í',
                        'i3': 'ǐ',
                        'i4': 'ì',
                        'o1': 'ō',
                        'o2': 'ó',
                        'o3': 'ǒ',
                        'o4': 'ò',
                        'u1': 'ū',
                        'u2': 'ú',
                        'u3': 'ǔ',
                        'u4': 'ù',
                        'v1': 'ǜ',
                        'v2': 'ǘ',
                        'v3': 'ǚ',
                        'v4': 'ǜ',
                       }

def ConvertPinyinToneNumbers(lineIn):

  lineOut = lineIn

  # first transform
  for x, y in mapConstTone2ToneConst.items():
    lineOut = lineOut.replace(x, y).replace(x.upper(), y.upper())

  # second transform
  for x, y in mapVowelVowelTone2VowelToneVowel.items():
    lineOut = lineOut.replace(x, y).replace(x.upper(), y.upper())

  # third transform
  for x, y in mapVowelTone2Unicode.items():
    lineOut = lineOut.replace(x, y).replace(x.upper(), y.upper())

  return lineOut.replace('v', 'ü').replace('V', 'Ü')

if __name__ == '__main__':
  import sys
  # print (sys.argv[0])
  # for lineIn in sys.stdin:
  lineIn = "ni1hao3"
  lineOut = ConvertPinyinToneNumbers(lineIn)
  print lineOut
    # sys.stdout.write(lineOut)