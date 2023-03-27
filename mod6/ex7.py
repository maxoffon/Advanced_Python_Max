import logging
import os.path
from collections import deque

logger = logging.getLogger(__name__)


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def walk_tree(self):
        custom_deque = deque([self])
        while custom_deque:
            v = custom_deque.popleft()

            logger.info(f'Visiting node with value {v.value}')

            if v.left:
                logger.debug(f'Node with value {v.value} has child node on the left with value {v.left.value}')
                custom_deque.append(v.left)
            if v.right:
                logger.debug(f'Node with value {v.value} has child node on the right with value {v.right.value}')
                custom_deque.append(v.right)

    def __str__(self):
        return f'Binary tree with root {self.value}'


def restore_tree(path: str) -> BinaryTreeNode:
    with open(path, 'r', encoding='utf-8') as file:
        root = BinaryTreeNode(get_info_node(file.readline()))
        temp_root = root
        node_dict = {root.value: root}
        for line in file:
            if line.startswith('INFO'):
                temp_value = get_info_node(line)
                temp_root = node_dict[temp_value]
            elif line.startswith('DEBUG') and 'left' in line:
                parent_value, child_value = get_debug_nodes(line)
                temp_root.left = BinaryTreeNode(child_value)
                node_dict[child_value] = temp_root.left
            elif line.startswith('DEBUG') and 'right' in line:
                parent_value, child_value = get_debug_nodes(line)
                temp_root.right = BinaryTreeNode(child_value)
                node_dict[child_value] = temp_root.right
    return root


def get_info_node(string: str):
    root_line = string.split()
    value = int(root_line[len(root_line) - 1].replace('\n', ''))
    return value


def get_debug_nodes(string: str):
    root_line = string.split()
    child_value = int(root_line[len(root_line) - 1].replace('\n', ''))
    parent_value = int(root_line[4])
    return parent_value, child_value


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        filename='binary_tree.log',
                        filemode='w',
                        format="%(levelname)s: %(message)s")
    root = BinaryTreeNode(1)
    root.right = BinaryTreeNode(3)
    root.left = BinaryTreeNode(2)
    root.left.right = BinaryTreeNode(5)
    root.left.left = BinaryTreeNode(4)

    root.walk_tree()

    print(restore_tree(os.path.join(os.path.abspath('binary_tree.log'))))
