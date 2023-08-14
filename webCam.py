import cv2 

vid = cv2.VideoCapture(0)

if(vid.isOpened () == False):
    print("No es posible leer la entrada")


height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = int(vid.get(cv2.CAP_PROP_FPS))

out = cv2.VideoWriter('Prueba.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 30, (width,height))

while(True):
    ret, frame = vid.read()

    cv2.imshow("Camera web", frame)
    out.write(frame)
    if cv2.waitKey(25) == 32:
        break

    
vid.release()
out.release()

cv2.destroyAllWindows()    