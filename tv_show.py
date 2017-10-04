import video

class TvShow(video):
    def __init__(self, tv_season, tv_episode, tv_station):
        self.season = tv_season
        self.episode = tv_episode
        self.station = tv_station
