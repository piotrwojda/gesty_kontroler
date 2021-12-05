grove.onGesture(GroveGesture.Down, function () {
    basic.showNumber(4)
    radio.sendNumber(4)
})
grove.onGesture(GroveGesture.Right, function () {
    basic.showNumber(2)
    radio.sendNumber(2)
})
grove.onGesture(GroveGesture.Up, function () {
    basic.showNumber(3)
    radio.sendNumber(3)
})
grove.onGesture(GroveGesture.Left, function () {
    basic.showNumber(1)
    radio.sendNumber(1)
})
basic.showIcon(IconNames.Asleep)
basic.pause(1000)
basic.clearScreen()
grove.initGesture()
radio.setGroup(1)
basic.forever(function () {
	
})
