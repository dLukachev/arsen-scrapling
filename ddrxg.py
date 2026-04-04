
alp = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def checkIfPangram(sentence: str):
    alp = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    detect  = alp.copy()
    for i in alp:
        if i.lower() in sentence.lower():
            try:
                detect.remove(i)
            except:
                pass
    if (len(detect) == 0):
        return True
    else:
        return False

