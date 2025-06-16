class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None
        self.prev = None


class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_song(self, title):
        """
        Add song at the end of the playlist.
        """
        new_song = SongNode(title)
        if not self.head:
            self.head = self.tail = self.current = new_song
        else:
            self.tail.next = new_song
            new_song.prev = self.tail
            self.tail = new_song

    def play_next(self):
        """
        Play the next song.
        """
        if self.current and self.current.next:
            self.current = self.current.next
            print(f"Now playing: {self.current.title}")
        else:
            print("End of playlist.")

    def play_previous(self):
        """
        Play the previous song.
        """
        if self.current and self.current.prev:
            self.current = self.current.prev
            print(f"Now playing: {self.current.title}")
        else:
            print("Start of playlist.")

    def delete_current_song(self):
        """
        Delete the currently playing song.
        """
        if not self.current:
            print("No song to delete.")
            return

        print(f"Deleting: {self.current.title}")

        if self.current.prev:
            self.current.prev.next = self.current.next
        else:
            self.head = self.current.next

        if self.current.next:
            self.current.next.prev = self.current.prev
        else:
            self.tail = self.current.prev

        self.current = self.current.next or self.head

    def display_playlist(self):
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
playlist.play_previous()
playlist.delete_current_song()
playlist.display_playlist()
