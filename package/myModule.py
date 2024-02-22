def top_n(items, n):
    """Return the top n items in an array in desc order 
    
    Args:
        items: list or array like object
        n (int): num of items to be returned

    Return 
        array: top n items in desc order    
    
    Egs :
        >>>top([8,2,3,5,7,3], 3)
        [8,7,5]
    
    """

    for i in range(n): # keep sorting until we have the top n items
        for j in range(len(items)-1 - i):
            if(items[j]> items[j+1]): # if the item is bigger than the next item
                items[j], items[j+1] = items[j+1], items[j] # swap the two

    # get the last top n items
    top_n = items[-n:]

    # return in descending order
    return top_n[::-1]
    

