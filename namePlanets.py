import cv2
planets = cv2.imread("./assets/planets.jpg")
sun = "Sun"
mercury = "Mercury"
venus = "Venus"
earth = "Earth"
mars = "Mars"
jupiter = "Jupiter"
saturn = "Saturn"
uranus = "Uranus"
neptune = "Neptune"
cv2.putText(planets,sun,(30,50), color=(0,0,225), fontScale=1,fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,)
cv2.putText(planets,mercury,(60,100), color=(0,0,225), fontScale=0.5,fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,)
cv2.putText(planets,venus,(80,160), color=(0,0,225), fontScale=0.5,fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,)
cv2.putText(planets,earth,(120,100), color=(255,0,0), fontScale=0.5,fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,)
cv2.putText(planets,mars,(170,160), color=(0,0,225), fontScale=0.4, fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL)
cv2.putText(planets,jupiter,(200,70), color=(0,0,225), fontScale=1, fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL)
cv2.putText(planets,saturn,(300,180), color=(0,0,225), fontScale=1, fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL)
cv2.putText(planets,uranus,(380,110), color=(0,0,225), fontScale=0.5, fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL)
cv2.putText(planets,neptune,(400,160), color=(0,0,225), fontScale=0.6, fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL)
cv2.imshow("NamePlanets", planets)
cv2.waitKey(0)