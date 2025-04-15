n = 5
while n <= 50:
    basic.show_number(n)
    n += 5
    basic.pause(1000)

def on_forever():
    pass
basic.forever(on_forever)
