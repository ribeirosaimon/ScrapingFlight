import datetime


class StringTreatment:

    def time_treatment(self, time):
        # 09 h 50 m
        hour, minutes = 0, 0
        time_list = time.split(" ")
        if "h" in time:
            hour = int(time_list[0])
            if "m" in time:
                minutes = int(time_list[2])
        new_time = (hour * 60) + minutes
        return new_time

    def month_treatment(self, time):
        # março 2022
        month = 0
        time_list = time.split(" ")
        month_string = time_list[0].lower()

        if month_string == "janeiro":
            month = 1
        elif month_string == "fevereiro":
            month = 2
        elif month_string == "março":
            month = 3
        elif month_string == "abril":
            month = 4
        elif month_string == "maio":
            month = 5
        elif month_string == "junho":
            month = 6
        elif month_string == "julho":
            month = 7
        elif month_string == "agosto":
            month = 8
        elif month_string == "setembro":
            month = 9
        elif month_string == "outubro":
            month = 10
        elif month_string == "novembro":
            month = 11
        elif month_string == "dezembro":
            month = 12

        return f"{time_list[1]}-{month}-01"
