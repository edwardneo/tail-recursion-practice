from trampoline import trampoline

def find_fringe(t):
    """Basic recursive find fringe function"""

    if t.fringe:
        return [t.label]

    lst = []
    for branch in t.branches:
        lst += find_fringe(branch)
    return lst

@trampoline
def find_fringe_tr(t):
    """Tail recursive find fringe function"""

    def find_fringe_helper(queue, lst):
        if not queue:
            return lst
        if queue[0].fringe:
            lst.append(queue[0].label)
        else:
            for branch in queue[0].branches:
                queue.append(branch)
        return lambda: find_fringe_helper(queue[1:], lst)
    return find_fringe_helper([t], [])

class Tree:
    """Tree class with 'fringe' implementation – subnodes of fringe nodes will also be fringe nodes"""

    def __init__(self, label, branches=[], fringe=False):
        self.label = label
        self.branches = branches
        self.fringe = fringe

        if self.fringe:
            self.set_fringe()
    
    def is_leaf(self):
        """Checks if tree is a leaf"""

        return not self.branches
    
    def set_fringe(self):
        """Sets subnodes as fringes"""

        for branch in self.branches:
            branch.fringe = True
            branch.set_fringe()

    def __str__(self):
        string = str(self.label)
        for branch in self.branches:
            string += str(branch).replace('\n', '\t\n')
        return string
    
    def __repr__(self):
        return f'Tree({self.label}, {[repr(branch) for branch in self.branches]})'