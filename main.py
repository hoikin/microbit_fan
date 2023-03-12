def playMusic():
    music.play_melody("B A B A B A B A ", 263)
def turnOnFans10s():
    pins.digital_write_pin(DigitalPin.P2, 1)
    basic.pause(10000)
    pins.digital_write_pin(DigitalPin.P2, 0)
    basic.pause(250)

def on_button_pressed_a():
    playMusic()
    turnOnFans10s()
input.on_button_pressed(Button.A, on_button_pressed_a)

def getTemp2():
    global temp
    temp = input.temperature()
def getTemp():
    global temp
    dht11.set_pin(DigitalPin.P8)
    dht11.read_from_sensor()
    temp = dht11.temperature()
    
rotated = 0
temp = 0
# let temp = 0
basic.show_icon(IconNames.DIAMOND)

def on_forever():
    global rotated
    getTemp()
    basic.show_number(temp)
    basic.pause(250)
    if temp >= 30:
        if rotated == 0:
            playMusic()
            rotated = 1
        turnOnFans10s()
    elif temp <= 29:
        rotated = 0
basic.forever(on_forever)
