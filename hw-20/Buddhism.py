import random


class Error(Exception):
    pass


class KillError(Error):
    pass


class DrunkError(Error):
    pass


class CarCrashError(Error):
    pass


class GluttonyError(Error):
    pass


class DepressionError(Error):
    pass


class Buddhism:
    max_karma = 500

    def __init__(self):
        self.karma = 0

    def one_day(self):
        with open('karma.log', 'a') as ouf:
            try:
                self.karma += random.randint(1, 7)
                if 10 == random.randint(1, 10):
                    raise random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
            except KillError:
                ouf.write('KillError\n')
            except DrunkError:
                ouf.write('DrunkError\n')
            except CarCrashError:
                ouf.write('CarCrushError\n')
            except GluttonyError:
                ouf.write('GluttonyError\n')
            except DepressionError:
                ouf.write('DepressionError\n')
