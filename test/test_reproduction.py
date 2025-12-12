from src.reproduction import reproduction

def test_reproduction ():
    values = {1:[1, 2, 3, 4], 2:[1, 2, 3, 4], 3:[1, 2, 3, 4], 4:[1, 2, 3, 4]}

    assert reproduction ([(1,2),(2,3),(1,4)], values) == [[1,2,3,4],[1,2,3,4],[1,2,3,4],[3,4,1,2],[3,4,1,2],[3,4,1,2]]