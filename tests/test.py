from package import myModule

def test_top_n():
    """" 
    Test top_n function to make sure its working
    """

    assert myModule.top_n([8,3,2,5,7],3) == [8,7,4], "incorrect" 
    assert myModule.top_n([81,32,52,25,7],5) == [81,52,32,25,7], "incorrect" 
    assert myModule.top_n([18,33,12,54,71],4) == [71,54,33,18], "incorrect" 
    assert myModule.top_n([2,5,7],2) == [7,5], "incorrect" 