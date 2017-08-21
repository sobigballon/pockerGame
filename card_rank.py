# Modify the card_ranks() function so that cards with
# rank of ten, jack, queen, king, or ace (T, J, Q, K, A)
# are handled correctly. Do this by mapping 'T' to 10, 
# 'J' to 11, etc...

def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    m_dictionary={'T':'10','J':'11','Q':'12','K':'13','A':'14'}
    ranks = [r for r,s in cards]#attention
    i,j=0,0
    while i<len(ranks) :
        if ranks[i] in m_dictionary:
            ranks[i]=m_dictionary[ranks[i]]
        i+=1
    print ranks
    while j<len(ranks):
        ranks[j]=int(ranks[j])
        j+=1
    ranks.sort(reverse=True)
    if ranks==[14,5,4,3,2]:
        ranks=[5,4,3,2,1]
    return ranks

print card_ranks(['AC', '3D', '4S', 'KH']) #should output [14, 13, 4, 3]
'''def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    al = "AC 2D 4H 3D 5S".split() # Ace-Low Straight
    assert straight(card_ranks(al)) == True 
    return 'tests pass'
print test()'''
