
# MIT License

# Copyright (c) 2021 George0023

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# install keyboard and selenium linked below.
# https://github.com/boppreh/keyboard
# https://pypi.org/project/selenium/

import time
from selenium import webdriver
import keyboard

# Here Chrome will be used
web = webdriver.Chrome()

# # Opening the website
web.get('YOURPOCKETNCIP')       # TODO: change this to your pocket nc ip address
# wait 10 sec for the website to load
time.sleep(10)

# home all axis
homeALL = web.find_element_by_class_name("width-button.btn.xbtn-primary")
homeALL.click()

# wait 30 sec for pocket nc to be homed.
time.sleep(30)

# the axis button on the web page
x = web.find_element_by_xpath(
    '/html[1]/body[1]/div[2]/span[1]/div[1]/div[1]/div[1]/div[2]/span[1]/div[1]/div[1]/button[1]')
y = web.find_element_by_xpath(
    '/html[1]/body[1]/div[2]/span[1]/div[1]/div[1]/div[1]/div[2]/span[1]/div[1]/div[1]/button[2]')
z = web.find_element_by_xpath(
    '/html[1]/body[1]/div[2]/span[1]/div[1]/div[1]/div[1]/div[2]/span[1]/div[1]/div[1]/button[3]')
a = web.find_element_by_xpath(
    '/html[1]/body[1]/div[2]/span[1]/div[1]/div[1]/div[1]/div[2]/span[1]/div[1]/div[1]/button[4]')
b = web.find_element_by_xpath(
    '/html[1]/body[1]/div[2]/span[1]/div[1]/div[1]/div[1]/div[2]/span[1]/div[1]/div[1]/button[5]')


def key1_press():
    # print('x')
    x.click()

def key2_press():
    # print('y')
    y.click()

def key3_press():
    # print('z')
    z.click()

def key4_press():
    # print('a')
    a.click()

def key5_press():
    # print('b')
    b.click()

# detect key presses sent by the pico
keyboard.add_hotkey('windows+alt+ctrl+shift+1', key1_press)
keyboard.add_hotkey('windows+alt+ctrl+shift+2', key2_press)
keyboard.add_hotkey('windows+alt+ctrl+shift+3', key3_press)
keyboard.add_hotkey('windows+alt+ctrl+shift+4', key4_press)
keyboard.add_hotkey('windows+alt+ctrl+shift+5', key5_press)

# stop the program from exiting. 
keyboard.wait()
