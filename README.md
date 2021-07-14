# pocket-nc-jog-controller

this project use raspberry pi pico with CircuitPython, if you dont have it yet. install it following this link: https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython

once you done that upload code.py to your pi pico.


on the computer side this project achive all the website buttion clicking using selenium, and detect the key presses sent from the pi pico with python keyboard library. 

to install selenium follow this link: https://pypi.org/project/selenium/

the python keyboard library: https://github.com/boppreh/keyboard


the fuction of the receiver.py file is to turn the key press sent by the pico into button press on the pocket NC control website. upon running this file, this program will open up a web browser, open your pocket nc control website, run Home All commend, and after 30 second you can use the jog controller. 

for the jog wheel to your you have to enable the mouse wheel jog on the control website. 

# before you run receiver.py!!!

disconnect main power to your pocket nc in case it crashes. 
