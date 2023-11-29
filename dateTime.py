from datetime import datetime

class DateTime:
    def __init__(self, year, month, day, hours=0, minutes=0, seconds=0, mseconds=0):
        self._year = year
        self._month = month     
        self._day = day       
        self._hours = hours       
        self._minutes = minutes      
        self._seconds = seconds
        self._mseconds = mseconds    

        if not self.is_valid_date(self._day, self._month, self._year):
            raise ValueError("Invalid date provided.")

    def to_iso_format(self):
        return f"{self._year:04d}-{self._month:02d}-{self._day:02d}T{self._hours:02d}:{self._minutes:02d}:{self._seconds:02d}"

    def to_human_readable(self):
        return f"{self._year}-{self._month:02d}-{self._day:02d} {self._hours:02d}:{self._minutes:02d}:{self._seconds:02d}"

    @classmethod
    def iso_format(cls, iso_datetime):
        date_str, *time_str = iso_datetime.split('T')
        date_val = [int(val) for val in date_str.split('-')]
        if len(time_str) > 0:
            time_val = [int(val) for val in time_str[0].split(':')]
        else:
            time_val = [0, 0, 0]
        year, month, day = date_val
        hours, minutes, seconds = time_val
        return cls(year, month, day, hours, minutes, seconds)

    @classmethod
    def from_current_utc(cls):
        now = datetime.utcnow()
        return cls(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond // 1000)

    @staticmethod
    def is_valid_date(day, month, year):
        try:
            datetime(year, month, day)
            return True
        except ValueError:
            return False

    @staticmethod
    def calculate_date_difference(date1, date2):
        delta = date1 - date2
        return abs(delta.days)

    @classmethod
    def create_from_string(cls, date_string):
        try:
            parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
            return cls(parsed_date.year, parsed_date.month, parsed_date.day)
        except ValueError:
            raise ValueError("Invalid date string format. Please provide date in the format YYYY-MM-DD")
        
    @staticmethod
    def format_to_iso(date):
        return date.to_iso_format()

    @staticmethod
    def format_to_human_readable(date):
        return date.to_human_readable()

    @staticmethod
    def convert_to_julian_calendar(date):
        gregorian_date = datetime(date.year, date.month, date.day)
        julian_date = gregorian_date - datetime(4713, 11, 24)
        return DateTime(julian_date.year, julian_date.month, julian_date.day)

    @staticmethod
    def convert_to_gregorian_calendar(date):
        julian_date = datetime(date.year, date.month, date.day)
        gregorian_date = julian_date + datetime(4713, 11, 24)
        return DateTime(gregorian_date.year, gregorian_date.month, gregorian_date.day)

    @staticmethod
    def get_weekday(date):
        return datetime(date.year, date.month, date.day).strftime("%A")

    @property
    def year(self):
        return self._year
    @property
    def months(self):
        return self._month
    @property
    def days(self):
        return self._day
    @property
    def hours(self):
        return self._hour
    @property
    def minute(self):
        return self._minutes
    @property
    def second(self):
        return self._seconds
    @property
    def msecond(self):
        return self._mseconds
    
clas_instance = DateTime(2023, 11, 29, 20, 28, 29, 22323)
output = clas_instance.msecond
print(output)
