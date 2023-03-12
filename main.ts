function playMusic () {
    music.playMelody("B A B A B A B A ", 263)
}
function turnOnFans10s () {
    pins.digitalWritePin(DigitalPin.P2, 1)
    basic.pause(10000)
    pins.digitalWritePin(DigitalPin.P2, 0)
    basic.pause(250)
}
input.onButtonPressed(Button.A, function () {
    playMusic()
    turnOnFans10s()
})
function getTemp2 () {
    temp = input.temperature()
}
function getTemp () {
    dht11.set_pin(DigitalPin.P8)
    temp = dht11.temperature()
}
let rotated = 0
let temp = 0
// let temp = 0
basic.showIcon(IconNames.Diamond)
basic.forever(function () {
    getTemp2()
    basic.showNumber(temp)
    basic.pause(250)
    if (temp >= 30) {
        if (rotated == 0) {
            playMusic()
            rotated = 1
        }
        turnOnFans10s()
    } else if (temp <= 29) {
        rotated = 0
    }
})
