# NFL sezona traje 18 tjedana
# September 8, 2022 (četvrtak) – January 8, 2023
# National Football League (NFL) regular season begins on the weekend following the first Monday of September
# uzet ćemo četvrtak kao početak, u nedjelju se igra prva utakmica,
# ali kao početak se gleda četvrtak, lakše mi je provjeriti, ali stavit ćemo prvu utakmicu u shedule da bude ona koja se igra u nedjelju
# sezona traje 18 tjedana ali završava nedjeljom pa ćemo uzeti onda od start date-a
# koji je četvrtak da je završni datum za 18*7-4 dana

import datetime as dt
import locale


def nfl_season_games_schedule(season_year):
    while True:

        try:
            date_start_season, date_end_season = calculate_start_end_date(int(season_year))
            game_schedule = make_schedule(date_start_season, date_end_season)
            return game_schedule
        except Exception as e:
            print(f"Došlo je do pogreške: {e}\n")


def calculate_start_end_date(year):
    month = 9
    day = 1
    while True:
        date_monday = dt.date(year, month, day)
        if date_monday.weekday() == 0:
            day += 3
            date_start_season = dt.date(year, month, day)
            date_end_season = date_start_season + dt.timedelta(days=7*18-4)
            return date_start_season, date_end_season
        else:
            day += 1


def make_schedule(start_date, end_date):
    game_schedule = {}
    for week in range(1, 19, 2):
        for day in range((week-1)*7, week*7):
            date_game = start_date + dt.timedelta(days=day)
            locale.setlocale(locale.LC_TIME, "hr_HR")
            if date_game.weekday() == 3 or date_game.weekday() == 6:
                game_schedule[date_game] = date_game.strftime("%A")

    # treba dodati kao closing day kao event još na raspored recimo, mislim, ne bi ga trebao nikada po ovome dodati, ali
    # bolje nek provjeri je li već dodan
    if end_date not in game_schedule.keys():
        game_schedule[end_date] = end_date.strftime("%A")
    return game_schedule


def user_interface():
    print("-"*10, "RASPORED UTAKMICA", "-"*10)
    season_year = input("Upišite godinu za koju želite raspored NFL utakmica u formatu YYYY: ")
    game_schedule = nfl_season_games_schedule(season_year)
    counter = 1
    for date in game_schedule.keys():
        print("-"*39)
        print(f"{counter}. utakmica\n")
        print(f"{game_schedule[date]}, {date}")
        print("-" * 39)
        counter += 1


user_interface()


