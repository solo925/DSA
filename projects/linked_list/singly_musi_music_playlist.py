class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None
        self.current = None

    def add_song(self, title):
        """
        Add song at the end of the playlist.
        """
        new_song = SongNode(title)
        if not self.head:
            self.head = new_song
            self.current = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_song

    def play_next(self):
        """
        Play the next song in the playlist.
        """
        if self.current and self.current.next:
            self.current = self.current.next
            print(f"Now playing: {self.current.title}")
        else:
            print("End of playlist.")

    def display_playlist(self):
        """
        Display all songs in the playlist.
        """
        node = self.head
        print("Playlist:")
        while node:
            print(f"- {node.title}")
            node = node.next


# Example usage
playlist = Playlist()
playlist.add_song("Song A")
playlist.add_song("Song B")
playlist.add_song("Song C")

playlist.display_playlist()
playlist.play_next()
playlist.play_next()
playlist.play_next()
