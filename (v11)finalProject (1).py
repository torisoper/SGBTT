# Tori, Teelin, Spencer, Geraldine, Ben
# Code Final Project - Fauxtoshopsnapgram

import gui
import random
from gui import *
from functools import partial
import image
from image import *
import urllib
import simplejson as json


picture = None
filepath = None


# ---------------------------- drawArt() Function ----------------------------

# example code to get a button working
# we kept this just for fun :p
#dont have on actual code ;)
def drawArt():
  drawACircle(random.randint(0,500),random.randint(150,500),random.randint(0,75),blue,false,random.randint(10,100))

 
def drawACircle(x,y,radius,color,filled,thickness): 
  global window
  circle1 = gui.Circle(x,y,radius)
  window.add(circle1,x,y)


# ---------------------- Importing Photos -------------------------------

# function for selecting a photo and adding it to the GUI window. once
# you add a picture, it also gives the user the option to choose a new 
# photo by adding the the GUI window a button called 
# chooseNewPictureButton
# arguments:
# none
# returns:
# none
def importPhoto():
  global window, picture, filepath
  filepath = pickAFile()
  
  jesPicture = makePicture(filepath)
  width = 650
  if jesPicture.getHeight() > jesPicture.getWidth():
    width = 450
    
  picture = Icon(filepath, width)
  #picture = makePicture(pickAFile())
  
  window.add(picture, 425, 100)
  window.add(chooseNewPictureButton, 25, 200)

# this function is called by the button chooseNewPictureButton. This
# function removes everything from the GUI window so that the old
# photo is removed, and then it addes everything back onto the window.
# arguments:
# none
# returns:
# none
def importNewPhoto():
  global window
  window.removeAll()
  window.add(Rectangle(0, 0, window.getWidth(), window.getHeight(), Color.PINK, true, 1))
  window.add(clearButton, 25, 125)
  window.add(drawButton, 25, 150)
  window.add(pickPhotoButton, 25, 175)
  window.add(chooseNewPictureButton, 25, 200)
  window.drawLabel("Edit Your Own Photo!", 500, 20, Color.BLACK, Font("Bebas Neue", Font.BOLD, 50))
  picture = Icon(pickAFile())
  window.add(picture, window.getWidth()/3, 100)
  

# -------------------------- Clear Button --------------------------

# this clears all progress you've done and allows the user to
# restart
def clearArt():
  global window, clearButton, drawButton, pickPhotoButton, sepiaButton, grayButton, posterizeButton, drawLabel, queryButton
  window.drawLabel('foo', 50, 50)
  #window.removeAll()
  window.add(Rectangle(0, 0, window.getWidth(), window.getHeight(), Color.LIGHT_GRAY, true, 1))
  window.drawLabel("Edit Your Own Photo!", 500, 20, Color.BLACK, Font("Bebas Neue", Font.BOLD, 50))
  window.drawLabel("1. Pick a Photo", 25, 100, Color.WHITE, Font("Bebas Neue", Font.BOLD, 25))
  window.drawLabel("2. Choose a Filter", 25, 125, Color.WHITE, Font("Bebas Neue", Font.BOLD, 25))
  window.drawLabel("3. Start Over or Apply a New Filter!", 25, 150, Color.WHITE, Font("Bebas Neue", Font.BOLD, 25))
  window.add(pickPhotoButton, 25, 225)
  window.add(sepiaButton, 25, 275)
  window.add(grayButton, 25, 300)
  window.add(posterizeButton, 25, 325)
  window.add(queryButton, 25, 350)
  window.add(negativeButton, 25, 375)
  window.add(vscoButton, 25, 400)
  window.add(sepiaVignetteButton, 25, 425) 
  window.add(clearButton, 25, 475)
  window.add(Rectangle(400, 75, 1100, 725, Color.WHITE, true, 1))
  

# ------------------- Sepia Filter ----------------------- 

# creates sepia look to photographs. updates pixels in origional photograph and saves it in the same folder 
# that the user got the og picture from. used by a file path and jesPicture to have the libaries talk with the icon.
# tints the shadows and midtones if the red is less than 63 it adds the red by 1.4 and the blue by .07
# arguments:
# none
# returns:
# updated picture to the file path of the original photograph
def sepiaFilter():
  global picture, filepath, window
  #setMediaPath()
  jesPicture = makePicture(filepath)
  #writePictureTo(jesPicture, getMediaPath() + 'sepia.jpg')
  
  for p in getPixels(jesPicture):
    newRed = getRed(p) * 0.299
    newGreen = getGreen(p) * 0.587
    newBlue = getBlue(p) * 0.114
    luminance = newRed+newGreen+newBlue
    setColor(p,makeColor(luminance,luminance,luminance))
  
  for p in getPixels(jesPicture):
    red = getRed(p)
    blue = getBlue(p)
    
    #tint shadows
    if (red <63):
      red = red*1.4
      blue = blue*.07
    
    #tint midtones
    if (red > 62 and red < 192):
      red = red*1.25
      if (red > 255):
        red = 255
      blue = blue*0.8
      
    setBlue(p,blue)
    setRed(p,red)
  
  shortenedFilepath = filepath[:len(filepath)-4]
  writePictureTo(jesPicture, shortenedFilepath + 'sepia.jpg')
  
  window.remove(picture)
  
  width = 650
  if jesPicture.getHeight() > jesPicture.getWidth():
    width = 450
    
  picture = Icon(shortenedFilepath + 'sepia.jpg', width)
  window.add(picture, window.getWidth()/3, 100)
  

# ------------------- Black & White Filter -----------------------
# applies a black and white filter look to photographs. updates pixels in origional photograph and saves it in the same folder 
# that the user got the og picture from. used by a file path and jesPicture to have the libaries talk with the icon.
# updates the red green and blue pixels and uses the luminace to remove the color and make it black and white. 
# arguments:
# none
# returns:
# updated picture to the file path of the original photograph
def grayScale():
  global window, filepath, picture

  jesPicture = makePicture(filepath)

  for p in getPixels(jesPicture):
    newRed = getRed(p) * 0.299
    newGreen = getGreen(p) * 0.587
    newBlue = getBlue(p) * 0.114
    luminance = newRed+newGreen+newBlue
    setColor(p,makeColor(luminance,luminance,luminance))
    
  shortenedFilepath = filepath[:len(filepath)-4]
  writePictureTo(jesPicture, shortenedFilepath + 'grayScale.jpg')
  
  window.remove(picture)
  
  width = 650
  if jesPicture.getHeight() > jesPicture.getWidth():
    width = 450
    
  picture = Icon(shortenedFilepath + 'grayScale.jpg', width)
  window.add(picture, window.getWidth()/3, 100)


# ------------------- Posterize Filter -----------------------
# applies posterized look to photographs. updates pixels in origional photograph and saves it in the same folder 
# that the user got the og picture from. used by a file path and jesPicture to have the libaries talk with the icon.
# uses if, elif and else statements to set the red, blue, and green pixels in the photo for a comic book type look.
# arguments:
# none
# returns:
# updated picture to the file path of the original photograph
def posterize():
  global window, filepath, picture
  
  jesPicture = makePicture(filepath)
  
  for p in getPixels(jesPicture):
    red = getRed(p)
    blue = getBlue(p)
    green = getGreen(p)
    
    # rewrite above if statements using elif and else
    if red < 64:
      setRed(p, 31)
    elif red < 128:
      setRed(p, 95)
    elif red < 192:
      setRed(p, 159)
    else:
      setRed(p, 223)

    #check and set green values
    if green < 64:
      setGreen(p, 31)
    if green > 63 and green < 128:
      setGreen(p, 95)
    if green > 127 and green < 192:
      setGreen(p, 159)
    if green > 191 and green < 256:
      setGreen(p, 223)

    #check and set blue values
    if blue < 64:
      setBlue(p, 31)
    if blue > 63 and blue < 128:
      setBlue(p, 95)
    if blue > 127 and blue < 192:
      setBlue(p, 159)
    if blue > 191 and blue < 256:
      setBlue(p, 223)


  shortenedFilepath = filepath[:len(filepath)-4]
  writePictureTo(jesPicture, shortenedFilepath + 'posterize.jpg')
  
  window.remove(picture)
  
  width = 650
  if jesPicture.getHeight() > jesPicture.getWidth():
    width = 450
    
  picture = Icon(shortenedFilepath + 'posterize.jpg', width)
  window.add(picture, window.getWidth()/3, 100)


# ------------------- Query Filter -----------------------
# adds data from a surf swell on Kahalui Harbor, Maui if the surf swell is high it will be bluer than if it is low
# adjusts water level from 0 to 3 because those are the adverage swell sizes
# uses the url lib and jyson lib
# arguments:
# none
# returns:
# updated picture to the file path of the original photograph
def queryFilter():
  global window, filepath, picture
  jesPicture = makePicture(filepath)
  rangeOfWL = 3 # Range of water levels from 0 to 3
  #Query pulls data from water levels in Kahalui Harbor on Maui
  url = "https://tidesandcurrents.noaa.gov/api/datagetter?date=today&station=1615680&product=water_level&datum=mllw&units=english&time_zone=lst&application=web_services&format=json"
  response = urllib.urlopen(url)
  data = json.loads(response.read())
  waterLevel = float(data['data'][len(data['data'])-1]['v'])

  for px in getPixels(jesPicture):
    b = getBlue(px)
    #print b
    adjB = (waterLevel / rangeOfWL) * b
    b = b + adjB
    #print b
    setBlue(px, b)
   
  shortenedFilepath = filepath[:len(filepath)-4]
  writePictureTo(jesPicture, shortenedFilepath + 'queryFilter.jpg')
  
  window.remove(picture)
  
  width = 650
  if jesPicture.getHeight() > jesPicture.getWidth():
    width = 450
    
  picture = Icon(shortenedFilepath + 'queryFilter.jpg', width)
  window.add(picture, window.getWidth()/3, 100)
  

# ------------------- Negative Filter -----------------------
# applies negative updates pixels in origional photograph and saves it in the same folder 
# that the user got the og picture from. used by a file path and jesPicture to have the libaries talk with the icon.
# 
# arguments:
# none
# returns:
# updated picture to the file path of the original photograph
def negative():

  global window, filepath, picture
  
  jesPicture = makePicture(filepath)
  
  for p  in getPixels(jesPicture):
    red=getRed(p)
    green=getGreen(p)
    blue=getBlue(p)
    negColor=makeColor(255-red, 255-green, 255-blue)
    setColor(p, negColor)


  shortenedFilepath = filepath[:len(filepath)-4]
  writePictureTo(jesPicture, shortenedFilepath + 'negative.jpg')
  
  window.remove(picture)
  
  width = 650
  if jesPicture.getHeight() > jesPicture.getWidth():
    width = 450
    
  picture = Icon(shortenedFilepath + 'negative.jpg', width)
  window.add(picture, window.getWidth()/3, 100)
  
# ------------------- VSCO Inspired Filter -----------------------
# applies VSCO inspired look to photographs. updates pixels in origional photograph and saves it in the same folder 
# that the user got the og picture from. used by a file path and jesPicture to have the libaries talk with the icon.
# uses if statements to set the red, blue, and green pixels in the photo for subltle VSCO filter look that is seen on instagram alot. 
# arguments:
# none
# returns:
# updated picture to the file path of the original photograph
def vscoEffect():
  global window, filepath, picture

  jesPicture = makePicture(filepath)

  for p in getPixels(jesPicture):
    red = getRed(p)
    green = getGreen(p)
    blue = getBlue(p)
    
    #tint shadows
    if (red < 63):
      red = red*1.0
      blue = blue*1.1
      
    #tint midtones
    if (red > 62 and red < 192):
      red = red*1.0
      blue = blue*1.1
      
    #tint highlights
    if (red > 191):
      red = red*0.9
      if (red > 255):
        red = 255
      blue = blue*0.95
      
    #set color
    setBlue(p, blue)
    setRed(p, red)
    
        
    
  shortenedFilepath = filepath[:len(filepath)-4]
  writePictureTo(jesPicture, shortenedFilepath + 'vscoEffect.jpg')
  
  window.remove(picture)
  
  width = 650
  if jesPicture.getHeight() > jesPicture.getWidth():
    width = 450
    
  picture = Icon(shortenedFilepath + 'vscoEffect.jpg', width)
  window.add(picture, window.getWidth()/3, 100)


# ------------------- Vignette + Sepia Filter -----------------------    
# applies another Sepia  look to photographs. but also adds a vignette for a fun take on this classic filter.
# updates pixels in origional photograph and saves it in the same folder 
# that the user got the og picture from. used by a file path and jesPicture to have the libaries talk with the icon.
# arguments:
# none
# returns:
# updated picture to the file path of the original photograph   
def sepiaVignette():
  global picture, filepath, window
  
  jesPicture = makePicture(filepath)
  
  for p in getPixels(jesPicture):
    newRed = getRed(p) * 0.299
    newGreen = getGreen(p) * 0.587
    newBlue = getBlue(p) * 0.114
    luminance = newRed+newGreen+newBlue
    setColor(p,makeColor(luminance,luminance,luminance))
  
  
  for p in getPixels(jesPicture):
    red = getRed(p)
    green = getGreen(p)
    blue = getBlue(p)
    
    #tint shadows
    if (red < 63):
      red = red * 1.15
      blue = blue * .1
    
    #tint midtones
    if (red > 62 and red < 192):
      red = red * 1.15
      if (red > 225):
        red = 225
      blue = blue * 0.9
      
    setBlue(p,blue)
    setRed(p,red)
    setGreen(p,green)
    

  width = getWidth(jesPicture)
  height = getHeight(jesPicture)
  centerX = width/2
  centerY = height/2
  
  for p in getPixels(jesPicture):
    pX = getX(p)
    pY = getY(p)
    
    distance = sqrt((pX - centerX)**2 + (pY - centerY)**2)
    
    #this determines the distance from the center
    
    darknessFactor = distance / (width/3)
    if(darknessFactor < 1):
      darknessFactor = 1
      
      # this is what is darkening those pixels
      
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    
    r = r * 1 / darknessFactor
    g = g * 1 / darknessFactor
    b = b * 1 / darknessFactor
    
    setColor(p, makeColor(r, g, b))

  shortenedFilepath = filepath[:len(filepath)-4]
  writePictureTo(jesPicture, shortenedFilepath + 'sepiaVignetteEffect.jpg')
  
  window.remove(picture)
  
  width = 650
  if jesPicture.getHeight() > jesPicture.getWidth():
    width = 450
    
  picture = Icon(shortenedFilepath + 'sepiaVignetteEffect.jpg', width)
  window.add(picture, window.getWidth()/3, 100)


# -------------------------- GUI Window  --------------------------

# gets screen width to use later when making GUI window
# arguments:
# none
# returns: 
# the width of the user's screen
def getScreenWidth():
  global window
  return Toolkit.getDefaultToolkit().getScreenSize().width
  
# gets screen height to use later when making GUI window
# arguments:
# none
# returns: 
# the height of the user's screen
def getScreenHeight():
  global window
  return Toolkit.getDefaultToolkit().getScreenSize().height

def setUp():
  global window, clearButton, drawButton, pickPhotoButton, sepiaButton, grayButton, posterizeButton, drawLabel, queryButton, negativeButton, vscoButton, sepiaVignetteButton
  
  # this creates the GUI window using the functions under the "Make
  # GUI Window" section
  window = Display("Fauxtoshopsnapgram", getScreenWidth(), getScreenHeight())

  # This code makes all the buttons
  drawButton = Button("Draw Circle", drawArt)
  pickPhotoButton = Button("Pick a Photo", importPhoto)
  chooseNewPictureButton = Button("Pick a New Photo", importNewPhoto)
  clearButton = Button("Clear", clearArt)
  sepiaButton = Button("Sepia", sepiaFilter)
  grayButton = Button("B&W", grayScale)
  posterizeButton = Button("Posterize", posterize)
  queryButton = Button("Ocean", queryFilter)
  negativeButton = Button("Negative", negative)
  vscoButton = Button("VSCO", vscoEffect)
  sepiaVignetteButton = Button("Soft Sepia + Vignette", sepiaVignette)

  # this section of setting up the GUI window is for adding
  # the buttons we have created to the window.
  window.add(Rectangle(0, 0, window.getWidth(), window.getHeight(), Color.LIGHT_GRAY, true, 1))
  window.drawLabel("Edit Your Own Photo!", 500, 20, Color.BLACK, Font("Bebas Neue", Font.BOLD, 50))
  window.drawLabel("1. Pick a Photo", 25, 100, Color.WHITE, Font("Bebas Neue", Font.BOLD, 25))
  window.drawLabel("2. Choose a Filter", 25, 125, Color.WHITE, Font("Bebas Neue", Font.BOLD, 25))
  window.drawLabel("3. Start Over or Apply a New Filter!", 25, 150, Color.WHITE, Font("Bebas Neue", Font.BOLD, 25))
  window.add(pickPhotoButton, 25, 225)
  window.add(sepiaButton, 25, 275)
  window.add(grayButton, 25, 300)
  window.add(posterizeButton, 25, 325)
  window.add(queryButton, 25, 350)
  window.add(negativeButton, 25, 375)
  window.add(vscoButton, 25, 400)
  window.add(sepiaVignetteButton, 25, 425) 
  window.add(clearButton, 25, 475)
  window.add(Rectangle(400, 75, 1100, 725, Color.WHITE, true, 1))

#the globals and calling the setup function. 
global window, clearButton, drawButton, pickPhotoButton, sepiaButton, grayButton, posterizeButton, drawLabel, queryButton, negativeButton, vscoButton, sepiaVignetteButton
setUp()