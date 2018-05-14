"""
4 metodos interesantes utilizando fechas.
days_in_month(year, month): Retorna el numero de dias en el mes month.

def is_valid_date(year, month, day): Retorna True si el año, mes y dia ingresado
son validos, sino regresa False. Utiliza el metodo anterior.

def days_between(year1, month1, day1, year2, month2, day2): El numero de dias
entre la primera y segunda fecha ingresadas. Utiliza el def anterior

def age_in_days(year, month, day): Ingresale tu fecha de nacimiento YYYY/M/DD
y te devuelve tu edad exacta en dias. Utiliza el metodo anterior.
"""

import datetime


def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    date1 = datetime.date(year, month, 1)
    if month == 12:
        return 31
    else:
        date2 = datetime.date(year, month+1, 1)
    difference = date2 - date1
    return difference.days


def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if datetime.MINYEAR <= year <= datetime.MAXYEAR:
        if 1 <= month <= 12:
            if 1 <= day <= days_in_month(year, month):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if is_valid_date(year1, month1, day1):
        date1 = datetime.date(year1, month1, day1)
    else:
        return 0

    if is_valid_date(year2, month2, day2):
        date2 = datetime.date(year2, month2, day2)
    else:
        return 0

    difference = date2 - date1
    if difference.days > 0:
        return difference.days
    else:
        return 0


def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input day as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    if is_valid_date(year, month, day):
        date1 = datetime.date(year, month, day)
    else:
        return 0
    difference = datetime.date.today() - date1
    dias = difference.days
    if dias < 0:
        return 0
    else:
        return dias

