import uuid
import datetime


class UUIDTools(object):

    @staticmethod
    def uuid1_hex():
        return uuid.uuid1().hex


class DateTools(object):

    @staticmethod
    def now():
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')