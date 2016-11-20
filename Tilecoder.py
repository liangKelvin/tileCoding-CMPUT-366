from math import *

numTilings = 8
    
def tilecode(in1,in2,tileIndices):
    # write your tilecoder here (5 lines or so)


    for tiling in range (numTilings) :
    	offset = (0.6/8)*tiling
    	x = floor((in1 + offset)/0.6)
    	y = floor((in2 + offset)/0.6)*11
    	tileIndices[tiling] = int(x + y + 121*tiling)

    return tileIndices


    	
def printTileCoderIndices(in1,in2):
    tileIndices = [-1]*numTilings
    tilecode(in1,in2,tileIndices)
    print('Tile indices for input (',in1,',',in2,') are : ', tileIndices)

#printTileCoderIndices(0.1,0.1)
#printTileCoderIndices(4.0,2.0)
#printTileCoderIndices(5.99,5.99)
#printTileCoderIndices(4.0,2.1)
    
