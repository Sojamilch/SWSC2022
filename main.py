import pandas as pd #import library to parce data
import json as js #import library to work with json file
import neopixel 
import board 
import time

numOfPixels = 100

strip1 = neopixel.NeoPixel(board.D18, numOfPixels)

attributes = [0,0,0,255]
data = "SensorGroup1.xlsx" #File path

strip1.fill((0,0,0))
strip1[0] = (255,255,255)
strip1.show()

x=0
y=0
rows = 2880
#8 columns
#in iloc 1st one is row and 2nd is column

CM = [] #List to store data
NO = [] #List to store data
ND = [] #List to store data
RH = [] #List to store data
TE = [] #List to store data
BA = [] #List to store data
NS = [] #List to store data

df = pd.read_excel(data)

for r in range(rows):
    for c in range(9):
        if c==1:
            CMDICT=[]
            CM.append([df.iloc[r,0], df.iloc[r,c],0])
        # if c==2:
            # NODICT=[]
            # NO.append(NODICT)
        # if c==3:
            # NDDICT={}
            # NDDICT[df.iloc[r,0]] = df.iloc[r,c]
            # ND.append(NDDICT)
        # if c==4:
            # RHDICT={}
            # RHDICT[df.iloc[r,0]] = df.iloc[r,c]
            # RH.append(RHDICT)
        # if c==5:
            # TEDICT={}
            # TEDICT[df.iloc[r,0]] = df.iloc[r,c]
            # TE.append(TEDICT)
        # if c==6:
            # BADICT={}
            # BADICT[df.iloc[r,0]] = df.iloc[r,c]
            # BA.append(BADICT)
        # if c==7:
            # NSDICT={}
            # NSDICT[df.iloc[r,0]] = df.iloc[r,c]
            # NS.append(NSDICT)



def nextLight(value, row, lightIndex, white,strip):
	print("value\t", value, "\nrow\t", row, "\nlightIndex\t", lightIndex)
	
	if row == rows-1:
		return 0	
		print("start")
		
	if value < float(CM[row+1][1]):
		lightIndex += 1
		# if white - 25 < 0:
			# white -= 25 
		
		strip[lightIndex] = (white,255,white)
		strip[lightIndex+1] = (white,255,white)
		strip[lightIndex+2] = (white,255,white)
		print("up", lightIndex)
			
	elif value > float(CM[row+1][1]):
		strip[lightIndex] = (0,0,0)
		strip[lightIndex+1] = (0,0,0)
		strip[lightIndex+2] = (0,0,0)
		if lightIndex - 1 != -1:
			# if white + 25 > 255:
				# white += 25
			lightIndex -=1 
		print("down", lightIndex)
		
	else:
		print("same")
		
	
	strip.show()

	row +=1
	value = CM[row][1]
	
	print("mainvalue ->", value)
	print(row, CM[row][1], lightIndex)
	
	
	newAttributes[0] = value
	newAttributes[1] = row
	newAttributes[2] = lightIndex
	newAttributes[3] = white
	
	
	return newAttributes
		
while True:  
	row = 0
	for i in range(rows):
		
		nextLight(attributes1[0],attributes1[1],attributes1[2],attributes1[3],strip1)
		nextlight(attributes2[0],attributes2[1],attributes2[2],attributes3[3],strip2)
		
		
		
	attributes = [0,0,0,255]
	strip1.fill((0,0,0))


#	mainValue = CM[nextLight(mainValue,i,mainLightIndex)][1]
	#nextLight(mainValue,i,mainLightIndex)
		
	

# for i in range(numOfPixels):
	# brightness = 255
	# strip[i] = (0,brightness,0)
	# brightness -= 10
	# strip.show()
	# time.sleep(0.1)
	

# for i in range(numOfPixels):
	
	# strip[-i] = (0,0,0)
	# strip.show()
	# time.sleep(0.1)
	
		
