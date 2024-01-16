import csv

from cfbd import Conference
from dotenv import load_dotenv

from CFBD_Configuration.CFBD_Model_Converter import conference_to_dict

load_dotenv()

from CFBD_Configuration import CFBD_Services
from datetime import datetime


def main():
    # Ask if program needs to run setup or pull stats
    choice = input("(1) Setup resources for specific year\n"
                   "(2) Update stats in database\n"
                   "Choice: ")

    # Prompt for year
    year = get_year()

    if choice == "1":
        # Get all conferences to later ask which conferences should be included in the setup
        conferences = CFBD_Services.get_conferences()
        conference_names = [conference.name for conference in conferences]
        conference_names.sort()

        print("Enter a conference you want included in the setup (enter \'q\' to stop):")
        desired_conferences = set()
        while True:
            if len(desired_conferences) == 0:
                print("Current list of conferences: {}\n")
            else:
                print(f"Current list of conferences: {desired_conferences}")
            print("Type \'list\' for a list of all conferences in CFBD")

            desired_conference = input()
            if desired_conference == "q" and len(desired_conferences) > 0:
                break
            if desired_conference == "list":
                print(conference_names)
                continue
            if desired_conference in conference_names:
                desired_conferences.add(desired_conference)
                print(f"Added {desired_conference}")
            else:
                print(f"\'{desired_conference}\' is not a conference in CFBD")

        print(f"Final list of conferences: {desired_conferences}")

        # Write desired conferences (mapped to CFBD conferences) to local csv
        # Filter out all conferences not desired
        conferences = filter_desired_conferences(desired_conference_names=desired_conferences, conferences=conferences)
        write_conferences_to_csv(year=year, conferences=conferences)
        print("Finished writing desired conferences to the CSV")


def get_year() -> int:
    while True:
        year = input("What year do you want to setup?\n"
                     "Year: ")
        try:
            year = int(year)
        except ValueError:
            print(f"{year} could not be parsed into a year")
        else:
            if year > datetime.now().year:
                print(f"{year} is too far into the future")
                continue
            elif year < 2023:
                print(f"{year} is not supported")
                continue
            break
    return year


def filter_desired_conferences(desired_conference_names: [str], conferences: [Conference]):
    final_conference_list = []
    for conference in conferences:
        if conference.name not in desired_conference_names:
            continue
        else:
            final_conference_list.append(conference)
    return final_conference_list


def write_conferences_to_csv(year: int, conferences: [Conference]):
    with open(f"resources/{year}/conferences.csv", "w", newline="") as conference_csv:
        conference_csv_fieldnames = ["id", "name", "short_name", "abbreviation", "classification"]
        csv_writer = csv.DictWriter(conference_csv, fieldnames=conference_csv_fieldnames)
        csv_writer.writeheader()
        for conference in conferences:
            csv_writer.writerow(conference_to_dict(conference))


if __name__ == "__main__":
    main()
