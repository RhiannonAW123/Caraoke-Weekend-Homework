class Room:
    def __init__(self, name, song_played_title, song_played_artist, capacity, fee, till):
        self.name = name
        self.song_played_title =  song_played_title
        self.song_played_artist = song_played_artist
        self.capacity = capacity
        self.fee = fee
        self.till = till
        self.guest_list = []

    def guest_count(self):
        return(len(self.guest_list))

    def check_in_guest(self,guest):
        self.guest_list.append(guest)
