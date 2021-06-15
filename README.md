# Multi_Pass VERSION 1
This document contains all aspects to completing this project. Please read before implementing.
I will also supply the links

![Image of MultiPassV2](https://github.com/nmsr1196/Multi_Pass/blob/main/MP_FRONT.jpg)


BELOW ARE THE NOTES FOR HOW EVERYTHING WAS USED AND METHODS TO CREATE THE MULTIPASS VERSION 1:

CODE:

THIS PROJECT USES CIRCUITPYTHON

The code file 'MultiPass_SR.py' has to be changed to 'code.py' for the QT Py 2040.  If you use the QT Py SAMD you may have memory errors using the ssd1306. If you 
decide to use the QT Py SAMD you will need Flash chip (https://www.adafruit.com/product/4763) to provide enough space for the libraries. If you don't use the ssd1306 
you can use the QT Py SAMD you should not need the Flash chip if you only want the leds without the ssd1306.

WIRING:

To try and keep a thin profile, I used wire-wrap. To insure connectivity, I also soldered the connections of the wire-wrap connections.

GLUE USED:

I used hot glue to secure the parts. And just a small bead on the bottom of the QT Py. The 3D geometry should hold the QT Py but the bead of glue helps more.

3D PRINTING MODIFICATION:

As mentioned before, this is a re-mix of the Ruiz brothers. The files will be included

-The height geometery of the top part was increased to hold button, QT Py, Oled and neopixel 

-Additional geometry was added for button(if same button is not used,then hot glue is your friend)

-An addition part was created to hold the round acrylic lens. 

-I added some small holes for the wiring to go through so that very little wiring is exposed on top

-Added a battery holder, This depends on the type of LiPo used

-An extra .stl was added for the holder of the neopixel lens This will be a very snug fit for the lens and no hot glue is needed for this




ACRYLIC:

Acrylic does not have to be used. A light diffusion 3D material can be use
There were two simple pieces of clear green 1/8" acrylic used. These were simple and fast to cut. The files will be included

-For the round acrylic lens for the neopixel I used 1/4 clear green acrylic. I used a frosting spray to offset some brightnes of the neopixel light

-For the stem I used a smaller size due to the added geometry of the switch

POWER:

You can use any lipo battery you like. But, you will have to change the 3D holder for it if you don't use the same one I used

-100 mAh LiPo  (https://www.adafruit.com/product/1570)

-Power Boost (You can use any one)

-Used a diode to connect to 5 volt pin of the QT Py 2040. Cathode side to 5V pin of QT Py (https://learn.adafruit.com/adafruit-qt-py-2040/pinouts)

LED:
You can use any led you like. The hole fits a 3mm. If you change to a larger one, the 3D hole will have to be modified
-I used a 3mm green led

BELOW ARE THE PARTS USED:

-QT Py 2040 (https://www.adafruit.com/product/4900) I think you can use any version of th QT Py

-7 Neopixel jewel (https://www.adafruit.com/product/2859) I think you can use any one of them. I think they are the same size

-Button (https://www.adafruit.com/product/3870)

-3mm LED (https://www.adafruit.com/product/4202) You can use any type of 3mm LED

-Diode is used to connect between powerboost 5V and 5V pin to QT Py. Cathode to 5V pin (https://learn.adafruit.com/adafruit-qt-py-2040/pinouts)

-Resistor I used a 2.2K ohm. You can select your own value. I chose a higher value to reduce brightness

-Wire wrap (https://www.amazon.com/gp/product/B01CK9GZV6/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) I used multiple colors to keep my wiring sanity.
    You can use a solid color option is you like (https://www.adafruit.com/product/1446)
    
-OLED SSD1306 I2C (https://www.amazon.com/Pieces-Display-Module-SSD1306-Screen/dp/B08N6N8L5Q/ref=sr_1_8?dchild=1&keywords=oled+i2c&qid=1622717100&sr=8-8)
  You can use any version of this type. I chose this because of it low profile and its wiring connectors on one end.
  
-3D Material  I had some Prusa Silver PLA, you can use any color/material of your selection

-Acrylic 1/8" green clear acrylic (you can use any color of your choosing) 1/8" fits the created model. As mentioned above, this can be replace with 3D material

-SP PH 2-pin Cable (https://www.adafruit.com/product/3814) This is for the connection to the power boost. Not needed depends on which powerboost chosen

-PowerBoost (https://www.adafruit.com/product/2030) Almost any powerboost can be used depending on your selected wiring

-Light cardstock black paper or regular paper (The color chose is of your choosing)


BELOW IS THE TYPE OF CARD YOU WILL USE TO PLACE IN YOUR MULTIPASS:

You can put in the card similar to the movie.

If you want to use something similiar to the movie I will include a Photoshop file.

You will/can change the following because remember in order to get to 'Fhloston Paradise' duplicate IDs are highly unacceptable:

--name

--pictures

--numbers on pictures

--Size of pictures can be done in Photoshop menu: 'Image', 'Image Size'

--For the xray looking picture. Copy your original picutre and use Photoshop just 'invert'the image under the 'Image', 'Adjustments', then 'Invert' menu.


FILES:

MultiPass_Lense_Holder.stl - This is the holder for the lens. The hold of this should measure about 39.23mm(outer), 25.7mm(inner hole), 1.8mm height

Multipass_Insert.psd - This is a photoshop file for a movie version insert. Due to the power led, you will have to cut a notch for the insert to fit all the way.
     Version 2 MP you can use either the movie version insert or your vaccine card.

Multipass_Rod_.svg - This is the rod for the side of the multipass. It should measure about 40..89mm x 3.99mm

Multipass_lense.svg - This is the lens cover for the neopixel jewel. It should measure 25.6mm This will be a very snug fit. No hot glue necessary

MultiPass_SR.py - This is the code for the QT Py 2040. This has to be changed to 'code.py' for circuitpython for the QT Py 2040.

MultiPass_Mod_BOTTOM.stl - This is the modified bottom piece of the multipass

MultiPass_Mod_TOP.stl - This is the modified top piece of the multipass

MP_QTPi-1.mov - This video file shows the function of the multipass

MP_QTPi_2-1.mov - This shows the side profile of the multipass

MP_FRONT.jpg - This is a picture of the front of the multipass

MP_BACK.jpg - This is a picture of the back of the multipass

MultiPass_CRICUT_BACK.svg - This is the file to use on a cricut to cover wiring on the back of multipass (remember light cardstock or regular paper)

MultiPass.fzz - Fritzing document with wired device connectivity

MultiPass_Battery_Holder.stl - LiPo 3.7v battery 100/105 mAh holder

MultiPass_Suggestion.jpg - Suggestion to cut notch in movie card to bypass led



