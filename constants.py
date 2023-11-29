import datetime


class Constants:
    maxDate = datetime.datetime.now().date()
    minDate = datetime.date(1900, 1, 1)
    case_status = ["Open", "Close", "Pending", "Unknown"]
    case_types = ["Homicide", "Assault", "Burglary/Theft", "Robbery", "Fraud/Financial Crimes", "Drug-Related Offenses",
                  "Sexual Offenses", "Traffic Violations", "Vandalism", "Missing Persons", "Domestic Violence",
                  "Cybercrime", "Arson", "Public Disorder", "Terrorism", "Unknown"]
    officer_ranks = ["Colonel", "Lieutenant Colonel", "Major", "Captain",
                     "Lieutenant", "Sergeant", "Trooper First", "Trooper"]
