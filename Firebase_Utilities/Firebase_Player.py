class FirebasePlayer:
    def __init__(self, id: int):
        self.id = id

        self.fumbles_lost = 0

        self.receiving_tds = 0
        self.receiving_yds = 0
        self.receiving_receptions = 0

        self.rushing_tds = 0
        self.rushing_yds = 0
        self.rushing_carries = 0

        self.passing_ints = 0
        self.passing_tds = 0
        self.passing_yds = 0
        self.passing_completions = 0
        self.passing_attempts = 0

        self.punting_in_twenty = 0
        self.punting_tbs = 0
        self.punting_yds = 0

        self.kicking_pts = 0
        self.fgm = 0
        self.fga = 0
        self.xpa = 0
        self.xpm = 0

        self.puntReturn_tds = 0
        self.puntReturn_yds = 0

        self.kickReturn_tds = 0
        self.kickReturn_yds = 0
