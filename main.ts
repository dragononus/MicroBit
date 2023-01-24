input.onGesture(Gesture.Shake, function () {
    music.stopAllSounds()
    led.stopAnimation()
    basic.clearScreen()
})
input.onSound(DetectedSound.Loud, function () {
    music.ringTone(262)
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
    basic.clearScreen()
    basic.showString("Stop Prosim")
})
basic.forever(function () {
	
})
