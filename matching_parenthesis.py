def rec(n, diff, comb, combinations):
    """
    function rec

    @params : n diff comb combinations
    @returns : None

    A recursive function which generates valid
    parenthesisations of specified length.

    Time Complexity : O(n*2^n)
    Space Complexity : O(n*2^n)
    """

    if(diff < 0 or diff > n):
        return
    elif(n == 0):
        if(diff == 0):
            combinations.append("".join(comb))  # valid parenthsization added
    else:
        comb.append('(')
        rec(n-1, diff+1, comb, combinations)    # calling rec after appending (
        comb.pop()
        comb.append(')')
        rec(n-1, diff-1, comb, combinations)    # calling rec after appending )
        comb.pop()


def generate(n):
    """
    function generate

    @params : n
    @returns : list of combinations

    Function which calls the rec function
    and returns the combinations.
    It multiplies the input by 2 since parenthesizations are in pairs.

    """
    # required vars
    combinations = []
    comb = []
    diff = 0

    rec(2*n, diff, comb, combinations)  # parenthesization has pairs of ()
    return combinations


print(generate(2))
