class GapBufferTextEditor:
    def __init__(self, size=1000):
        """
        Initialize the gap buffer with an initial size.
        """
        self.buffer = [''] * size
        self.gap_start = 0
        self.gap_end = size
        self.size = size

    def _gap_size(self):
        return self.gap_end - self.gap_start

    def _expand_gap(self, new_size):
        """
        Expand the gap if needed.
        """
        new_buffer = [''] * new_size
        new_gap_end = new_size - (self.size - self.gap_end)

        # Copy parts before and after the gap
        new_buffer[0:self.gap_start] = self.buffer[0:self.gap_start]
        new_buffer[new_gap_end:] = self.buffer[self.gap_end:]

        self.buffer = new_buffer
        self.gap_end = new_gap_end
        self.size = new_size

    def move_cursor(self, position):
        """
        Move the gap to the desired position.
        """
        if position < 0 or position > self.size - self._gap_size():
            raise IndexError("Cursor position out of range")

        if position < self.gap_start:
            # Move text after cursor into gap
            shift_size = self.gap_start - position
            self.buffer[self.gap_end - shift_size:self.gap_end] = self.buffer[position:self.gap_start]
            self.gap_start -= shift_size
            self.gap_end -= shift_size

        elif position > self.gap_start:
            # Move text before cursor into gap
            shift_size = position - self.gap_start
            self.buffer[self.gap_start:self.gap_start + shift_size] = self.buffer[self.gap_end:self.gap_end + shift_size]
            self.gap_start += shift_size
            self.gap_end += shift_size

    def insert(self, text):
        """
        Insert text at the current cursor position.
        """
        if len(text) > self._gap_size():
            self._expand_gap(self.size * 2)

        for char in text:
            self.buffer[self.gap_start] = char
            self.gap_start += 1

    def delete(self, length):
        """
        Delete 'length' characters at the current cursor (increase gap size).
        """
        self.gap_end += length
        if self.gap_end > self.size:
            self.gap_end = self.size

    def get_text(self):
        """
        Return the current text as a string.
        """
        return ''.join(self.buffer[0:self.gap_start] + self.buffer[self.gap_end:])

    def display(self):
        print(self.get_text())


# Example Usage
editor = GapBufferTextEditor()

editor.insert("Hello, World!")
editor.display()

editor.move_cursor(7)
editor.insert("beautiful ")
editor.display()

editor.delete(6)
editor.display()

editor.move_cursor(0)
editor.insert(">>> ")
editor.display()
