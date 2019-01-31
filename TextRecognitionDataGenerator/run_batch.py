import os
os.chdir('/root/yq/TextRecognitionDataGenerator/TextRecognitionDataGenerator/')
for i in range(100):
  try:
     os.system('python run.py -w 5 -f 128 -b 1 -wk -l en -c 1000 -na 3') 
  except:
     pass
  
