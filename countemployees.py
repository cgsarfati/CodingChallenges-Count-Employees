"""Count employees in an org chart.

Our organization has the following org chart::

                    Jane
          Jessica          Janet
       Al  Bob  Jen     Nick  Nora
                                Henri

Let's make this chart::

    >>> henri = Node("Henri")
    >>> nora = Node("Nora", [henri])
    >>> nick = Node("Nick")
    >>> janet = Node("Janet", [nick, nora])
    >>> al = Node("Al")
    >>> bob = Node("Bob")
    >>> jen = Node("Jen")
    >>> jessica = Node("Jessica", [al, bob, jen])
    >>> jane = Node("Jane", [jessica, janet])

And test our counting function::

    >>> henri.count_employees()
    0

    >>> nora.count_employees()
    1

    >>> jane.count_employees()
    8

We provide a non-recursive version, let's make sure that gives the same
answer::

    >>> jane.count_employees_nonrecursive()
    8

"""

# brainstorm:
    # want to traverse tree (either depth/breadth method), keeping
    # a counter in the process. traverse until children is None (meaning leaf)
    # at the end, have a lst of all nodes. count how many items in final lst.
    # recursive method -- progress until base case where children is None
        # children = kept in list? pop off w/ each traversal until empty lst?
        # popping from to_visit lst could be where counter is


class Node(object):
    """Node in a tree."""

    def __init__(self, name, children=None):
        self.name = name
        self.children = children or []

    def count_employees(self):
        """Use recursion."""

        # initialize counter
        count = 0

        # BASE: loop through children until no more to loop over
        for child in self.children:
            # inc. count in current recursive fn
            # PROGRESSION: recurse to child (DEPTH-FIRST)
            count = count + 1 + child.count_employees()

        return count

    def count_employees_nonrecursive(self):
        """Return a count of how many employees this person manages.

        Return a count of how many people that manager manages. This should
        include *everyone* under them, not just people who directly report to
        them.
        """

        # keep count
        count = 0

        # keep track of children
        to_visit = [self]

        # while lst not empty
        while to_visit:
            # get last item from lst (DEPTH-FIRST SEARCH)
            emp = to_visit.pop()

            # update count and add children
            for child in emp.children:
                count += 1

                # used .append vs .extend for counting purposes
                to_visit.append(child)
        return count


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU ARE A TREE GENIUS!\n"
