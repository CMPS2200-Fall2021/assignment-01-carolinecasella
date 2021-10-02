"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        return foo(x-1) + foo(x-2)


def longest_run(mylist, key):
    prev = None
    size = 1
    max_size = 0
    for i in range(len(mylist)):
        if (mylist[i] == key):
            size += 1
        if size > max_size:
            max_size = size
        else:
            size = 0
    return max_size


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key

    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))

def combineRes(resRight, resLeft):
    final = Result(0,0,0,False)

    if resRight.is_entire_range == False and resLeft.is_entire_range == False:
        final = Result(resLeft.left_size, resRight.right_size, max(resLeft.longest_size, resRight.longest_size, (resLeft.right_size + resLeft.left_size)), False)
        return final

    if resRight.is_entire_range == True and resLeft.is_entire_range == True:
        run = resRight.longest_size + resLeft.longest_size
        final = Result(run, run, run, True)
        return final

    if resRight.is_entire_range == False and resLeft.is_entire_range == True:
        final = Result((resLeft.longest_size + resRight.left_size), resRight.right_size, max(resLeft.longest_size, resRight.longest_size, (resLeft.right_size + resRight.left_size)), False)
        return final

    if resRight.is_entire_range == True and resLeft.is_entire_range == False:
        final = Result(resLeft.left_size, (resRight.longest_size + resLeft.right_size), max(resLeft.longest_size, resRight.longest_size, (resLeft.right_size + resRight.left_size)), False)
        return final

def longest_run_recursive(mylist, key):
    if len(mylist) == 1:
        if mylist[0] == key:
            res = Result(1,1,1,True)
            return res
        else:
            res1 = Result(0,0,0, False)
            return res1

    resLeft = longest_run_recursive(mylist[:len(mylist)//2], key)
    resRight = longest_run_recursive(mylist[len(mylist)//2:], key)
    return combineRes(resLeft, resRight)

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
