from sense_hat import SenseHat

class WeatherDataPoints:
    def __init__(self):
        print('init')
        self.sense = SenseHat()

    def clear_day(self):
        print('clear Day')

        X = [242, 255, 0]  # Yellow
        O = [145, 187, 255]  # Light blue

        clearDay = [
            X, X, O, O, O, O, O, O,
            X, X, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O
        ]

        self.sense.set_pixels(clearDay)

    def clear_night(self):
        print('clear Night')

    def rain(self):
        print('Rain')

    def snow(self):
        print('snow')

    def sleet(self):
        print('sleet')

    def wind(self):
        print('wind')

    def fog(self):
        print('fog')

    def cloudy(self):
        print('cloudy')

    def partly_cloudy_day(self):
        print('partly cloudy')

    def partly_cloudy_night(self):
        print('partly cloudy night')

    def hail(self):
        print('hail')

    def thunderstorm(self):
        print('thunderstorm')

    def tornado(self):
        print('tornado')