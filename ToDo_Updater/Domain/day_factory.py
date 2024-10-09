from .Day import Day
import datetime

class day_factory:
    @staticmethod
    def create_day(year, month, day):
        return Day(datetime.datetime(year, month, day))