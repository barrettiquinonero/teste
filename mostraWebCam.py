import cv2 #Importa a biblioteca
video = cv2.VideoCapture(0)
while True:
  conectado, frame = video.read() #conecta ao drive de videao caso presente
  cv2.imshow('video', frame) #mostra a imagem da webcam
  if cv2.waitKey(1) == ord('q'): # comando de saída, converte um caracter em um numeral da tabela ASCII
    break
video.release()
cv2.destroyAllWindows()
