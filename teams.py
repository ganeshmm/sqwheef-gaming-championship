import csv
import random

random.seed(17)

def randomize_teams(rsvp):
    done = False
    while not done:
        teams = shuffle_teams(rsvp)
        done = check_gender_balance(teams) and check_no_roommates(teams) and anika_on_four(teams)
    return teams

def shuffle_teams(rsvp):
    random.shuffle(rsvp)
    teams = [rsvp[0:4], rsvp[4:8], rsvp[8:11], rsvp[11:14], rsvp[14:17], rsvp[17:20]]
    return teams

def check_gender_balance(teams):
    # Either one or two girls per team
    for team in teams:
        girl_count = 0
        for member in team:
            if member[1] == 'girl':
                girl_count += 1
        if girl_count == 0 or girl_count > 2:
            return False
    return True

def check_no_roommates(teams):
    # No roommates on same team
    for team in teams:
        rooms = set()
        for member in team:
            if member[2] in rooms:
                return False
            rooms.add(member[2])
    return True

def anika_on_four(teams):
    # Anika must be on team of 4
    for member in (teams[0] + teams[1]):
        if member[0] == 'Anika Halder':
            return True
    return False

def print_teams(teams):
    for i, team in enumerate(teams):
        print(f"Team {i+1}:")
        for member in team:
            print(member[0])
        print()

if __name__ == '__main__':
    with open('rsvp.csv') as rsvp_file:
        rsvp = list(csv.reader(rsvp_file))
    teams = randomize_teams(rsvp)
    print_teams(teams)