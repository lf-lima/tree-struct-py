class Tree:
  def __init__(self, cargo = None, left = None, right = None):
    self.cargo = cargo
    self.left = left
    self.right = right

def print_tree_in_order(tree=None):
  print('Print Tree In Order => ', end=' ')

  def _print_tree_in_order(_tree=None):
    if _tree is None:
      return

    _print_tree_in_order(_tree.left)
    print(_tree.cargo, end=' ')
    _print_tree_in_order(_tree.right)
  
  _print_tree_in_order(tree)
  print('\n')

def print_tree_pre_order(tree=None):
  print('Print Tree Pre Order => ', end=' ')

  def _print_tree_pre_order(_tree=None):
    if _tree is None:
      return

    print(_tree.cargo, end=' ')
    _print_tree_pre_order(_tree.left)
    _print_tree_pre_order(_tree.right)
  
  _print_tree_pre_order(tree)
  print('\n')

def print_tree_pos_order(tree=None):
  print('Print Tree Pos Order => ', end=' ')

  def _print_tree_pos_order(_tree=None):
    if _tree is None:
      return

    _print_tree_pos_order(_tree.left)
    _print_tree_pos_order(_tree.right)
    print(_tree.cargo, end=' ')
  
  _print_tree_pos_order(tree)
  print('\n')

def insert_in_tree(tree, node):
  if node.cargo < tree.cargo:
    if tree.left is None:
      tree.left = node
    else:
      insert_in_tree(tree.left, node)
  else:
    if tree.right is None:
      tree.right = node
    else:
      insert_in_tree(tree.right, node)

def find_in_tree(tree, cargo):
  def _find_in_tree(_tree, _cargo):
    if _tree is None:
      return
    elif _cargo == _tree.cargo:
      return _tree.cargo
    elif _cargo < _tree.cargo:
      return _find_in_tree(_tree.left, _cargo)
    else:
      return _find_in_tree(_tree.right, _cargo)

  found_cargo = _find_in_tree(tree, cargo)

  if found_cargo is None:
    print('Not Found Cargo in Tree\n')
    return

  print('Found Cargo in Tree => ' + str(found_cargo) + '\n')

  return found_cargo

def find_the_smallest_in_tree(tree):
  smallest_node = tree

  while smallest_node.left is not None:
    smallest_node = smallest_node.left
  
  smallest_cargo = smallest_node.cargo

  print('Smallest Cargo in Tree => ' + str(smallest_cargo) + '\n')

  return smallest_cargo

def find_the_biggest_in_tree(tree):
  biggest_node = tree

  while biggest_node.right is not None:
    biggest_node = biggest_node.right
  
  biggest_cargo = biggest_node.cargo

  print('Biggest Cargo in Tree => ' + str(biggest_cargo) + '\n')

  return biggest_cargo

tree = Tree(50)
insert_in_tree(tree, Tree(24))
insert_in_tree(tree, Tree(60))
insert_in_tree(tree, Tree(12))
insert_in_tree(tree, Tree(30))
insert_in_tree(tree, Tree(21))
insert_in_tree(tree, Tree(55))
insert_in_tree(tree, Tree(70))

print_tree_in_order(tree)
print_tree_pre_order(tree)
print_tree_pos_order(tree)

find_in_tree(tree, 24)

find_the_smallest_in_tree(tree)
find_the_biggest_in_tree(tree)