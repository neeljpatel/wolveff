import json

_players = '''[{"Player": "Adam Vinatieri", "Bye": 10, "Number": 166, "Pos": "K", "Team": "IND"}, {"Player": "Mike Evans", "Bye": 7, "Number": 134, "Pos": "WR", "Team": "TB"}, {"Player": "Steve Smith", "Bye": 11, "Number": 133, "Pos": "WR", "Team": "BAL"}, {"Player": "Dwayne Bowe", "Bye": 6, "Number": 132, "Pos": "WR", "Team": "KC"}, {"Player": "Greg Jennings", "Bye": 10, "Number": 131, "Pos": "WR", "Team": "MIN"}, {"Player": "Markus Wheaton", "Bye": 12, "Number": 138, "Pos": "WR", "Team": "PIT"}, {"Player": "Justin Hunter", "Bye": 9, "Number": 137, "Pos": "WR", "Team": "TEN"}, {"Player": "James Jones", "Bye": 5, "Number": 136, "Pos": "WR", "Team": "OAK"}, {"Player": "Hakeem Nicks", "Bye": 10, "Number": 135, "Pos": "WR", "Team": "IND"}, {"Player": "Rueben Randle", "Bye": 8, "Number": 140, "Pos": "WR", "Team": "NYG"}, {"Player": "Jarrett Boykin", "Bye": 9, "Number": 139, "Pos": "WR", "Team": "GB"}, {"Player": "Robbie Gould", "Bye": 10, "Number": 167, "Pos": "K", "Team": "CHI"}, {"Player": "Doug Martin", "Bye": 7, "Number": 25, "Pos": "RB", "Team": "TB"}, {"Player": "Le'Veon Bell", "Bye": 12, "Number": 26, "Pos": "RB", "Team": "PIT"}, {"Player": "Arian Foster", "Bye": 10, "Number": 27, "Pos": "RB", "Team": "HOU"}, {"Player": "Montee Ball", "Bye": 4, "Number": 28, "Pos": "RB", "Team": "DEN"}, {"Player": "Matt Forte", "Bye": 9, "Number": 21, "Pos": "RB", "Team": "CHI"}, {"Player": "Marshawn Lynch", "Bye": 4, "Number": 22, "Pos": "RB", "Team": "SEA"}, {"Player": "Eddie Lacy", "Bye": 9, "Number": 23, "Pos": "RB", "Team": "GB"}, {"Player": "DeMarco Murray", "Bye": 11, "Number": 24, "Pos": "RB", "Team": "DAL"}, {"Player": "Justin Tucker", "Bye": 11, "Number": 161, "Pos": "K", "Team": "BAL"}, {"Player": "Giovani Bernard", "Bye": 4, "Number": 29, "Pos": "RB", "Team": "CIN"}, {"Player": "Reggie Bush", "Bye": 9, "Number": 30, "Pos": "RB", "Team": "DET"}, {"Player": "Mason Crosby", "Bye": 9, "Number": 162, "Pos": "K", "Team": "GB"}, {"Player": "Peyton Manning", "Bye": 4, "Number": 1, "Pos": "QB", "Team": "DEN"}, {"Player": "Andrew Luck", "Bye": 10, "Number": 5, "Pos": "QB", "Team": "IND"}, {"Player": "Colin Kaepernick", "Bye": 8, "Number": 9, "Pos": "QB", "Team": "SF"}, {"Player": "Phil Dawson", "Bye": 8, "Number": 164, "Pos": "K", "Team": "SF"}, {"Player": "Marques Colston", "Bye": 6, "Number": 120, "Pos": "WR", "Team": "NO"}, {"Player": "Mike Wallace", "Bye": 5, "Number": 121, "Pos": "WR", "Team": "MIA"}, {"Player": "Eric Decker", "Bye": 11, "Number": 122, "Pos": "WR", "Team": "NYJ"}, {"Player": "Sammy Watkins", "Bye": 9, "Number": 123, "Pos": "WR", "Team": "BUF"}, {"Player": "Wes Welker", "Bye": 4, "Number": 124, "Pos": "WR", "Team": "DEN"}, {"Player": "Terrance Williams", "Bye": 11, "Number": 125, "Pos": "WR", "Team": "DAL"}, {"Player": "Anquan Boldin", "Bye": 8, "Number": 126, "Pos": "WR", "Team": "SF"}, {"Player": "Cecil Shorts", "Bye": 11, "Number": 127, "Pos": "WR", "Team": "JAC"}, {"Player": "DeAndre Hopkins", "Bye": 10, "Number": 128, "Pos": "WR", "Team": "HOU"}, {"Player": "Riley Cooper", "Bye": 7, "Number": 129, "Pos": "WR", "Team": "PHI"}, {"Player": "Danny Amendola", "Bye": 10, "Number": 130, "Pos": "WR", "Team": "NE"}, {"Player": "Dan Bailey", "Bye": 11, "Number": 168, "Pos": "K", "Team": "DAL"}, {"Player": "Jeremy Maclin", "Bye": 7, "Number": 119, "Pos": "WR", "Team": "PHI"}, {"Player": "Jeremy Hill", "Bye": 4, "Number": 60, "Pos": "RB", "Team": "CIN"}, {"Player": "Darren McFadden", "Bye": 5, "Number": 59, "Pos": "RB", "Team": "OAK"}, {"Player": "Khiry Robinson", "Bye": 6, "Number": 56, "Pos": "RB", "Team": "NO"}, {"Player": "Lamar Miller", "Bye": 5, "Number": 55, "Pos": "RB", "Team": "MIA"}, {"Player": "Chris Ivory", "Bye": 11, "Number": 58, "Pos": "RB", "Team": "NYJ"}, {"Player": "Bernard Pierce", "Bye": 11, "Number": 57, "Pos": "RB", "Team": "BAL"}, {"Player": "Fred Jackson", "Bye": 9, "Number": 52, "Pos": "RB", "Team": "BUF"}, {"Player": "Maurice Jones-Drew", "Bye": 5, "Number": 51, "Pos": "RB", "Team": "OAK"}, {"Player": "Knowshon Moreno", "Bye": 5, "Number": 54, "Pos": "RB", "Team": "MIA"}, {"Player": "DeAngelo Williams", "Bye": 12, "Number": 53, "Pos": "RB", "Team": "CAR"}, {"Player": "Nick Novak", "Bye": 10, "Number": 165, "Pos": "K", "Team": "SD"}, {"Player": "Torrey Smith", "Bye": 11, "Number": 116, "Pos": "WR", "Team": "BAL"}, {"Player": "T.Y. Hilton", "Bye": 10, "Number": 115, "Pos": "WR", "Team": "IND"}, {"Player": "Antonio Gates", "Bye": 10, "Number": 89, "Pos": "TE", "Team": "SD"}, {"Player": "Calvin Johnson", "Bye": 9, "Number": 90, "Pos": "WR", "Team": "DET"}, {"Player": "Cordarrelle Patterson", "Bye": 10, "Number": 112, "Pos": "WR", "Team": "MIN"}, {"Player": "Percy Harvin", "Bye": 4, "Number": 111, "Pos": "WR", "Team": "SEA"}, {"Player": "Michael Floyd", "Bye": 4, "Number": 114, "Pos": "WR", "Team": "ARI"}, {"Player": "Golden Tate", "Bye": 9, "Number": 113, "Pos": "WR", "Team": "DET"}, {"Player": "Greg Olsen", "Bye": 12, "Number": 83, "Pos": "TE", "Team": "CAR"}, {"Player": "Jordan Reed", "Bye": 10, "Number": 84, "Pos": "TE", "Team": "WAS"}, {"Player": "Jason Witten", "Bye": 11, "Number": 81, "Pos": "TE", "Team": "DAL"}, {"Player": "Dennis Pitta", "Bye": 11, "Number": 82, "Pos": "TE", "Team": "BAL"}, {"Player": "Delanie Walker", "Bye": 9, "Number": 87, "Pos": "TE", "Team": "TEN"}, {"Player": "Zach Ertz", "Bye": 7, "Number": 88, "Pos": "TE", "Team": "PHI"}, {"Player": "Kyle Rudolph", "Bye": 10, "Number": 85, "Pos": "TE", "Team": "MIN"}, {"Player": "Martellus Bennett", "Bye": 9, "Number": 86, "Pos": "TE", "Team": "CHI"}, {"Player": "Matthew Stafford", "Bye": 9, "Number": 4, "Pos": "QB", "Team": "DET"}, {"Player": "Nick Foles", "Bye": 7, "Number": 8, "Pos": "QB", "Team": "PHI"}, {"Player": "DeSean Jackson", "Bye": 10, "Number": 109, "Pos": "WR", "Team": "WAS"}, {"Player": "Reggie Wayne", "Bye": 10, "Number": 110, "Pos": "WR", "Team": "IND"}, {"Player": "Pierre Garcon", "Bye": 10, "Number": 103, "Pos": "WR", "Team": "WAS"}, {"Player": "Keenan Allen", "Bye": 10, "Number": 104, "Pos": "WR", "Team": "SD"}, {"Player": "Vincent Jackson", "Bye": 7, "Number": 101, "Pos": "WR", "Team": "TB"}, {"Player": "Larry Fitzgerald", "Bye": 4, "Number": 102, "Pos": "WR", "Team": "ARI"}, {"Player": "Michael Crabtree", "Bye": 8, "Number": 107, "Pos": "WR", "Team": "SF"}, {"Player": "Julian Edelman", "Bye": 10, "Number": 108, "Pos": "WR", "Team": "NE"}, {"Player": "Victor Cruz", "Bye": 8, "Number": 105, "Pos": "WR", "Team": "NYG"}, {"Player": "Roddy White", "Bye": 9, "Number": 106, "Pos": "WR", "Team": "ATL"}, {"Player": "Frank Gore", "Bye": 8, "Number": 40, "Pos": "RB", "Team": "SF"}, {"Player": "Ryan Mathews", "Bye": 10, "Number": 39, "Pos": "RB", "Team": "SD"}, {"Player": "Andre Ellington", "Bye": 4, "Number": 34, "Pos": "RB", "Team": "ARI"}, {"Player": "Alfred Morris", "Bye": 10, "Number": 33, "Pos": "RB", "Team": "WAS"}, {"Player": "Ben Tate", "Bye": 4, "Number": 32, "Pos": "RB", "Team": "CLE"}, {"Player": "Zac Stacy", "Bye": 4, "Number": 31, "Pos": "RB", "Team": "STL"}, {"Player": "Shane Vereen", "Bye": 10, "Number": 38, "Pos": "RB", "Team": "NE"}, {"Player": "C.J. Spiller", "Bye": 9, "Number": 37, "Pos": "RB", "Team": "BUF"}, {"Player": "Ray Rice", "Bye": 11, "Number": 36, "Pos": "RB", "Team": "BAL"}, {"Player": "Trent Richardson", "Bye": 10, "Number": 35, "Pos": "RB", "Team": "IND"}, {"Player": "Shonn Greene", "Bye": 9, "Number": 61, "Pos": "RB", "Team": "TEN"}, {"Player": "Roy Helu", "Bye": 10, "Number": 62, "Pos": "RB", "Team": "WAS"}, {"Player": "Donald Brown", "Bye": 10, "Number": 63, "Pos": "RB", "Team": "SD"}, {"Player": "Terrance West", "Bye": 4, "Number": 64, "Pos": "RB", "Team": "CLE"}, {"Player": "Mark Ingram", "Bye": 6, "Number": 65, "Pos": "RB", "Team": "NO"}, {"Player": "Carlos Hyde", "Bye": 8, "Number": 66, "Pos": "RB", "Team": "SF"}, {"Player": "Christine Michael", "Bye": 4, "Number": 67, "Pos": "RB", "Team": "SEA"}, {"Player": "Knile Davis", "Bye": 6, "Number": 68, "Pos": "RB", "Team": "KC"}, {"Player": "James Starks", "Bye": 9, "Number": 69, "Pos": "RB", "Team": "GB"}, {"Player": "Jonathan Stewart", "Bye": 12, "Number": 70, "Pos": "RB", "Team": "CAR"}, {"Player": "Drew Brees", "Bye": 6, "Number": 3, "Pos": "QB", "Team": "NO"}, {"Player": "Steven Hauschka", "Bye": 4, "Number": 163, "Pos": "K", "Team": "SEA"}, {"Player": "Robert Griffin III", "Bye": 10, "Number": 7, "Pos": "QB", "Team": "WAS"}, {"Player": "Randall Cobb", "Bye": 9, "Number": 100, "Pos": "WR", "Team": "GB"}, {"Player": "Andre Johnson", "Bye": 10, "Number": 99, "Pos": "WR", "Team": "HOU"}, {"Player": "Nick Folk", "Bye": 11, "Number": 169, "Pos": "K", "Team": "NYJ"}, {"Player": "Dez Bryant", "Bye": 11, "Number": 92, "Pos": "WR", "Team": "DAL"}, {"Player": "Demaryius Thomas", "Bye": 4, "Number": 91, "Pos": "WR", "Team": "DEN"}, {"Player": "Brandon Marshall", "Bye": 9, "Number": 94, "Pos": "WR", "Team": "CHI"}, {"Player": "A.J. Green", "Bye": 4, "Number": 93, "Pos": "WR", "Team": "CIN"}, {"Player": "Antonio Brown", "Bye": 12, "Number": 96, "Pos": "WR", "Team": "PIT"}, {"Player": "Julio Jones", "Bye": 9, "Number": 95, "Pos": "WR", "Team": "ATL"}, {"Player": "Alshon Jeffery", "Bye": 9, "Number": 98, "Pos": "WR", "Team": "CHI"}, {"Player": "Jordy Nelson", "Bye": 9, "Number": 97, "Pos": "WR", "Team": "GB"}, {"Player": "Tom Brady", "Bye": 10, "Number": 12, "Pos": "QB", "Team": "NE"}, {"Player": "Matt Ryan", "Bye": 9, "Number": 11, "Pos": "QB", "Team": "ATL"}, {"Player": "Philip Rivers", "Bye": 10, "Number": 14, "Pos": "QB", "Team": "SD"}, {"Player": "Tony Romo", "Bye": 11, "Number": 13, "Pos": "QB", "Team": "DAL"}, {"Player": "Ben Roethlisberger", "Bye": 12, "Number": 16, "Pos": "QB", "Team": "PIT"}, {"Player": "Jay Cutler", "Bye": 9, "Number": 15, "Pos": "QB", "Team": "CHI"}, {"Player": "Adrian Peterson", "Bye": 10, "Number": 18, "Pos": "RB", "Team": "MIN"}, {"Player": "Carson Palmer", "Bye": 4, "Number": 17, "Pos": "QB", "Team": "ARI"}, {"Player": "LeSean McCoy", "Bye": 7, "Number": 20, "Pos": "RB", "Team": "PHI"}, {"Player": "Jamaal Charles", "Bye": 6, "Number": 19, "Pos": "RB", "Team": "KC"}, {"Player": "Kendall Wright", "Bye": 9, "Number": 118, "Pos": "WR", "Team": "TEN"}, {"Player": "Emmanuel Sanders", "Bye": 4, "Number": 117, "Pos": "WR", "Team": "DEN"}, {"Player": "Denver Bronco", "Bye": 4, "Number": 152, "Pos": "DEF", "Team": "DEN"}, {"Player": "San Franciso 49ERS", "Bye": 8, "Number": 151, "Pos": "DEF", "Team": "SF"}, {"Player": "Carolina Panther", "Bye": 12, "Number": 154, "Pos": "DEF", "Team": "CAR"}, {"Player": "Arizona Cardinal", "Bye": 4, "Number": 153, "Pos": "DEF", "Team": "ARI"}, {"Player": "St. Louis Rams", "Bye": 4, "Number": 156, "Pos": "DEF", "Team": "STL"}, {"Player": "Cincinnati Bengal", "Bye": 4, "Number": 155, "Pos": "DEF", "Team": "CIN"}, {"Player": "New England Patriots", "Bye": 10, "Number": 158, "Pos": "DEF", "Team": "NE"}, {"Player": "Kansas City Cheifs", "Bye": 6, "Number": 157, "Pos": "DEF", "Team": "KC"}, {"Player": "Stephen Gostkowski", "Bye": 10, "Number": 160, "Pos": "K", "Team": "NE"}, {"Player": "Tampa Bay Buccaneers", "Bye": 7, "Number": 159, "Pos": "DEF", "Team": "TB"}, {"Player": "Bishop Sankey", "Bye": 9, "Number": 49, "Pos": "RB", "Team": "TEN"}, {"Player": "Darren Sproles", "Bye": 7, "Number": 50, "Pos": "RB", "Team": "PHI"}, {"Player": "Stevan Ridley", "Bye": 10, "Number": 47, "Pos": "RB", "Team": "NE"}, {"Player": "Danny Woodhead", "Bye": 10, "Number": 48, "Pos": "RB", "Team": "SD"}, {"Player": "Steven Jackson", "Bye": 9, "Number": 45, "Pos": "RB", "Team": "ATL"}, {"Player": "Pierre Thomas", "Bye": 6, "Number": 46, "Pos": "RB", "Team": "NO"}, {"Player": "Toby Gerhart", "Bye": 11, "Number": 43, "Pos": "RB", "Team": "JAC"}, {"Player": "Rashad Jennings", "Bye": 8, "Number": 44, "Pos": "RB", "Team": "NYG"}, {"Player": "Chris Johnson", "Bye": 11, "Number": 41, "Pos": "RB", "Team": "NYJ"}, {"Player": "Joique Bell", "Bye": 9, "Number": 42, "Pos": "RB", "Team": "DET"}, {"Player": "Aaron Rodgers", "Bye": 9, "Number": 2, "Pos": "QB", "Team": "GB"}, {"Player": "Cam Newton", "Bye": 12, "Number": 6, "Pos": "QB", "Team": "CAR"}, {"Player": "Russell Wilson", "Bye": 4, "Number": 10, "Pos": "QB", "Team": "SEA"}, {"Player": "Kelvin Benjamin", "Bye": 12, "Number": 147, "Pos": "WR", "Team": "CAR"}, {"Player": "Marqise Lee", "Bye": 11, "Number": 148, "Pos": "WR", "Team": "JAC"}, {"Player": "Doug Baldwin", "Bye": 4, "Number": 145, "Pos": "WR", "Team": "SEA"}, {"Player": "Steve Johnson", "Bye": 8, "Number": 146, "Pos": "WR", "Team": "SF"}, {"Player": "Tavon Austin", "Bye": 4, "Number": 143, "Pos": "WR", "Team": "STL"}, {"Player": "Brian Hartline", "Bye": 5, "Number": 144, "Pos": "WR", "Team": "MIA"}, {"Player": "Andrew Hawkins", "Bye": 4, "Number": 141, "Pos": "WR", "Team": "CLE"}, {"Player": "Brandin Cooks", "Bye": 6, "Number": 142, "Pos": "WR", "Team": "NO"}, {"Player": "Kenny Stills", "Bye": 6, "Number": 149, "Pos": "WR", "Team": "NO"}, {"Player": "Seattle Seahawk", "Bye": 4, "Number": 150, "Pos": "DEF", "Team": "SEA"}, {"Player": "Rob Gronkowski", "Bye": 10, "Number": 78, "Pos": "TE", "Team": "NE"}, {"Player": "Julius Thomas", "Bye": 4, "Number": 77, "Pos": "TE", "Team": "DEN"}, {"Player": "Jimmy Graham", "Bye": 6, "Number": 76, "Pos": "TE", "Team": "NO"}, {"Player": "Mike Tolbert", "Bye": 12, "Number": 75, "Pos": "RB", "Team": "CAR"}, {"Player": "Lance Dunbar", "Bye": 11, "Number": 74, "Pos": "RB", "Team": "DAL"}, {"Player": "Ahmad Bradshaw", "Bye": 10, "Number": 73, "Pos": "RB", "Team": "IND"}, {"Player": "Andre Williams", "Bye": 8, "Number": 72, "Pos": "RB", "Team": "NYG"}, {"Player": "LeGarrette Blount", "Bye": 12, "Number": 71, "Pos": "RB", "Team": "PIT"}, {"Player": "Jordan Cameron", "Bye": 4, "Number": 80, "Pos": "TE", "Team": "CLE"}, {"Player": "Vernon Davis", "Bye": 8, "Number": 79, "Pos": "TE", "Team": "SF"}]'''

def fill_league_with_players(league):
    for row in json.loads(_players):
        d = {}
        d['number'] = row['Number']
        d['name'] = row['Player']
        d['team'] = row['Team']
        d['bye_week'] = row['Bye']
        d['position'] = row['Pos'].lower()
        d['league'] = league
        league.player_set.create(**d)