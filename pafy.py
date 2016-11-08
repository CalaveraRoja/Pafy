import pafy

archivo = open("Down.txt", "r")

for linea in archivo.readlines():
  url = linea.rstrip('\r\n')
  video = pafy.new(url)
  print (video.title)
  best = video.getbest()
  best.resolution, best.extension
  best.download(quiet=False)
  print ("")
 
    

