##    https://www.hackerrank.com/challenges/counting-valleys/problem
##
##    An avid hiker keeps meticulous records of their hikes. During the last
##    hike that took exactly steps steps, for every step it was noted if it was an
##    uphill, U, or a downhill, D step. Hikes always start and end at sea level,
##    and each step up or down represents a 1 unit change in altitude. We define
##    the following terms:
##
##        A mountain is a sequence of consecutive steps above sea level,
##        starting with a step up from sea level and ending with a step down
##        to sea level.
##
##        A valley is a sequence of consecutive steps below sea level,
##        starting with a step down from sea level and ending with a step up
##        to sea level.
##
##    Given the sequence of up and down steps during a hike, find and print
##    the number of valleys walked through.

##### ##### ##### #####

#   Iterative solution
#   O(n)
#   n is the number of characters in the path string
#   The key realization is that a valley starts anytime the
#   current elevation is 0 and the current step is 'D' as this
#   step down will take us below sea level.  Therefore this problem
#   is reduced to simply the book keeping of the current elevation
#   and the incrementing of a valley counter every time our elevation
#   and step conditions align.

def countingValleys(steps, path):
    
    current_elevation = 0
    valleys_found = 0
    
    for step in path:
        
        if step == 'D':

            if current_elevation == 0:

                valleys_found += 1
            
            current_elevation -= 1
            
        else:
            
            current_elevation += 1
                
    return valleys_found
