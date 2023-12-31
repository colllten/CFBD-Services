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
