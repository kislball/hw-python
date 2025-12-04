from queue import PriorityQueue


class TreeNode:
    def __init__(self, value: str):
        self.left: None | TreeNode = None
        self.right: None | TreeNode = None
        self.value = value


def sorted_insert(lst: list, value, key):
    target_idx = 0
    for i in range(len(lst)):
        target_idx = i
        if key(lst[i]) > key(value):
            break
    lst.insert(target_idx, value)


def encode(inp: str) -> tuple[str, dict[str, str]]:
    """Encodes inp using Huffman's algorithm"""
    output_string = ""
    dictionary = {}

    frequencies = {}
    for chr in inp:
        if chr in frequencies:
            frequencies[chr] += 1
        else:
            frequencies[chr] = 1

    nodes = PriorityQueue()
    for k, v in frequencies.items():
        nodes.put((v, k, TreeNode(k)))

    while nodes.qsize() > 1:
        s1 = nodes.get()
        s2 = nodes.get()

        node = TreeNode(s1[2].value + s2[2].value)
        node.left = s1[2]
        node.right = s2[2]

        nodes.put((s1[0] + s2[0], node.value, node))
    root = nodes.get()[2]

    def walk(node, acc):
        if node.left is None and node.right is None:
            dictionary[node.value] = acc
        else:
            if node.left is not None:
                walk(node.left, acc + "0")
            if node.right is not None:
                walk(node.right, acc + "1")

    walk(root, "")

    for ch in inp:
        output_string += dictionary[ch]

    return (output_string, dictionary)

def decode(encoded: str, table: dict[str, str]) -> str:
    """Decodes encoded using Huffman's algorithm on the provided table"""
    output = ""
    acc = ""
    reversed_dict = {v:k for k, v in table.items()}

    for x in encoded:
        acc += x
        if acc in reversed_dict:
            output += reversed_dict[acc]
            acc = ""

    return output
