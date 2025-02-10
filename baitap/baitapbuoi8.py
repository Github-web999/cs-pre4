# Bài 1: Duyệt danh sách lồng nhau và trích xuất ID
lstDemo = [
    {"id": 1, "value": [
        {"id": 2, "value": [
            {"id": 3, "value": [
                {"id": 4, "value": []}
            ]}
        ]}
    ]},
    {"id": 5, "value": []}
]

def extract_ids(lst):
    result = []
    for item in lst:
        result.append(item["id"])
        result.extend(extract_ids(item["value"]))
    return result

print("Danh sách ID:", extract_ids(lstDemo))  # Output: [1, 2, 3, 4, 5]

# Bài 2: Phân tích độ phức tạp của thuật toán (ví dụ O(n²))
def example_complexity(n):
    for i in range(n):
        for j in range(n):
            print(i, j)  # O(n²)

example_complexity(3)

# Bài 3: Tính chiều cao của cây
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def tree_height(node):
    if not node.children:
        return 0
    return 1 + max(tree_height(child) for child in node.children)

root = Node("A")
root.children = [Node("B"), Node("C")]
root.children[0].children = [Node("D")]
root.children[1].children = [Node("E")]

print("Chiều cao của cây:", tree_height(root))  # Output: 2

# Bài 4: Cấu trúc Trie để lưu trữ danh sách từ
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def display(self, node=None, word=""):
        if node is None:
            node = self.root
        if node.is_end_of_word:
            print(word)
        for char, child in node.children.items():
            self.display(child, word + char)

trie = Trie()
words = ["cat", "banana", "obama", "car", "cow", "alibaba"]
for word in words:
    trie.insert(word)

print("Danh sách từ trong Trie:")
trie.display()
