Great request. Here's a **clear README with complexity analysis** for **both implementations** of the **Music Playlist Manager**, suitable for study, projects, or GitHub:

---

# 🎵 Music Playlist Manager

Manage a playlist using **Linked Lists** to add songs, play next, play previous, delete current, and display the entire playlist.

---

## ✅ **Implementations Included**

| Implementation            | Description                                             |
| ------------------------- | ------------------------------------------------------- |
| **1. Singly Linked List** | Simple forward-only playlist                            |
| **2. Doubly Linked List** | Fully featured → forward & backward traversal, deletion |

---

## 🚀 **Features**

| Feature             | Singly Linked List | Doubly Linked List |
| ------------------- | ------------------ | ------------------ |
| Add Song            | ✅                  | ✅                  |
| Play Next Song      | ✅                  | ✅                  |
| Play Previous Song  | ❌                  | ✅                  |
| Delete Current Song | ❌ (inefficient)    | ✅ (efficient)      |
| Display Playlist    | ✅                  | ✅                  |

---

## ⚙ **Time Complexity Analysis**

### 1️⃣ Singly Linked List

| Operation           | Time Complexity                                          |
| ------------------- | -------------------------------------------------------- |
| Add Song (at end)   | O(n) → must traverse to tail                             |
| Play Next           | O(1)                                                     |
| Play Previous       | ❌ Not supported                                          |
| Delete Current Song | ❌ Inefficient → need to traverse to find previous (O(n)) |
| Display Playlist    | O(n)                                                     |

#### 🔸 **Summary**: *Works for small playlists or forward-only navigation.*

---

### 2️⃣ Doubly Linked List

| Operation           | Time Complexity |
| ------------------- | --------------- |
| Add Song (at end)   | ✅ O(1)          |
| Play Next           | ✅ O(1)          |
| Play Previous       | ✅ O(1)          |
| Delete Current Song | ✅ O(1)          |
| Display Playlist    | ✅ O(n)          |

#### 🔸 **Summary**: *Efficient for any playlist size. Recommended.*

---

## ⚖ **Space Complexity**

* **Both Implementations**: O(n), where *n* = number of songs.
* **Doubly Linked List** has a slightly higher overhead due to storing both `next` and `prev` pointers.

---

## 📦 **Which One Should You Use?**

| Use Case                                          | Choose                 |
| ------------------------------------------------- | ---------------------- |
| ✅ Simple playlist, forward only                   | Singly Linked List     |
| ✅ Realistic playlist manager (next, prev, delete) | **Doubly Linked List** |

---

## 📚 Example Commands in Use:

```plaintext
Playlist:
- Song A
- Song B
- Song C

Now playing: Song B
Now playing: Song A
Deleting: Song A

Playlist:
- Song B
- Song C
