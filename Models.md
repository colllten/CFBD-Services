# Player Model
| FIELD      | TYPE | USED? | VALUES / NOTES                                                |
|------------|------|-------|---------------------------------------------------------------|
| id         | int  | TRUE  |                                                               |
| first_name | str  | TRUE  |                                                               |
| last_name  | str  | TRUE  |                                                               |
| team       | str  | TRUE  |                                                               |
| height     | int  | TRUE  |                                                               |
| weight     | int  | TRUE  |                                                               |
| jersey     | int  | TRUE  |                                                               |
| position   | str  | TRUE  | QB, P, RB, PK, TE, WR. ~~LB~~, ~~DL~~, ~~LS~~, ~~OL~~, ~~DB~~ |

# Team Model
| FIELD          | TYPE  | USED? | VALUES / NOTES                                                                                                                      |
|----------------|-------|-------|-------------------------------------------------------------------------------------------------------------------------------------|
| id             | int   | TRUE  |                                                                                                                                     |
| school         | str   | TRUE  |                                                                                                                                     |
| mascot         | str   | TRUE  |                                                                                                                                     |
| abbreviation   | str   | TRUE  |                                                                                                                                     |
| alt_name_1     | str   | TRUE  |                                                                                                                                     |
| alt_name_2     | str   | TRUE  |                                                                                                                                     |
| classification | str   | FALSE |                                                                                                                                     |
| conference     | str   | TRUE  | SEC, B1G (Big Ten), Mountain West, Sun Belt, Mid-American, Pac-12, American Athletic, Conference USA, ACC, Big 12, FBS Independents |
| division       | str   | FALSE |                                                                                                                                     |
| color          | str   | TRUE  | #012345                                                                                                                             |
| alt_color      | str   | TRUE  | #012345                                                                                                                             |
| logos          | [str] | TRUE  |                                                                                                                                     |


# PlayerGame Model
Returned by GamesApi.get_player_game_stats()

| FIELD      | TYPE               | USED? | VALUES / NOTES                                                |
|------------|--------------------|-------|---------------------------------------------------------------|
| id         | int                | TRUE  |                                                               |
| teams      | [PlayerGameTeams]  | TRUE  |                                                               |

# PlayerGameTeams
Contained in response from GamesApi.get_player_game_stats()

| FIELD      | TYPE                   | USED? | VALUES / NOTES |
|------------|------------------------|-------|----------------|
| school     | str                    | TRUE  |                |
| conference | str                    | TRUE  | Big Ten, etc.  |
| home_away  | str                    | TRUE  | home, away     |
| points     | int                    | TRUE  |                |
| categories | [PlayerGameCategories] | TRUE  |                |

# PlayerGameCategories
Within the PlayerGameTeams

| FIELD | TYPE              | USED? | VALUES / NOTES                                                                                                     |
|-------|-------------------|-------|--------------------------------------------------------------------------------------------------------------------|
| name  | str               | TRUE  | ~~defensive~~, fumbles, receiving, rushing, passing, punting, kicking, puntReturns, kickReturns, ~~interceptions~~ |
| types | [PlayerGameTypes] | TRUE  |                                                                                                                    |


# PlayerGameTypes
Within the PlayerGameCategories

| FIELD    | TYPE                 | USED? | VALUES / NOTES                                                                                                                                                                                                                                                                                                                                                                                    |
|----------|----------------------|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name     | str                  | TRUE  | Depends on the category name; defensive(QB HUR, PD, TFL, SACKS, SOLO, TOT), fumbles(REC, LOST, FUM), receiving(LONG, TD, AVG, YDS, REC), rushing(LONG, TD, AVG, YDS, CAR), passing(QBR, INT, TD, AVG, YDS, C/ATT), punting(LONG, IN 20, TB, AVG, YDS, NO), kicking(PTS, XP, LONG, PCT, FG), puntReturns(TD, LONG, AVG, YDS, NO), kickReturns(TD, LONG, AVG, YDS, NO), interceptions(TD, YDS, INT) |
| athletes | [PlayerGameAthletes] | TRUE  |                                                                                                                                                                                                                                                                                                                                                                                                   |


# PlayerGameAthletes
Within PlayerGameTypes

| FIELD | TYPE | USED? | VALUES / NOTES |
|-------|------|-------|----------------|
| id    | int  | TRUE  |                |
| name  | str  | TRUE  |                |
| stat  | str  | TRUE  |                |