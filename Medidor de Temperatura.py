'''
temperaturas para o cozimento

48°c - (selada)
54°c - (ao ponto para o mal)
60°c - (ao ponto)
65°c - (ao ponto para o bem)
71°c - (bem passada)
'''

tc = input('qual a temperatura do bifão?: ')
tc = int(tc)

#programa da temperatura
if tc < 48:
  print('ta cru, cozinha mais')
elif tc in range(48, 53):
  print('selada')
elif tc in range(54, 59):
  print('ao ponto para o mal')
elif tc in range(60, 64):
  print('ao ponto')
elif tc in range(65, 71):
  print('ao ponto para o bem')
elif tc == 71:
  print('bem passada')
elif tc > 71:
  print('puta merda irmão vai torra o bagui')