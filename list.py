# count(5, [ 5, 5, 3 ]) returns 2
def count(n, l):
    count = 0
    for number in l:
        if number == n:
            count = count + 1
    return count


# length([ 5, 3, 2, 4]) returns 4
def length(l):
    length = 0
    for _ in l:
        length = length + 1
    return length


# max([ 5, 4, 8, 9]) returns 9
# max([ -5, -4, -8, -9]) returns -4
def max(l):
    max = 0
    for number in l:
        if number > max:
            max = number
    return max


# min([ 5, 4, 8, 9]) returns 4
def min(l):
    min = max(l)
    for number in l:
        if number < min:
            min = number
    return min


# isFound(5, [ 3, 4, 5, 6]) returns True
def isFound(n, l):
    count(n, l)
    if count != 0:
        return True
    return False

# removeDuplicates([ 2,  5, 3, 2, 3]) returns [2, 3, 5]
2

def removeDuplicates(l):
    nonduplicits = []
    for ch in l:
        true = True
        for nonduplicit in nonduplicits:
            if ch == nonduplicit:
                true = False
                break
        if true == True:
            nonduplicits.append(ch)
    return nonduplicits
