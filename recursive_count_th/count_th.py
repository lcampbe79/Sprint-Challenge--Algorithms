'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #base case-since there can't be matches
    if len(word) < 2:
        return 0
    #if the first 2 letters are "th", it adds 1 
    if word[0:2] == "th":
        return count_th(word[1:]) + 1
    #if it doesn't match then it moves on
    else:
        return count_th(word[1:])

print(count_th("iamtestingwiththecountththth"))
