import re
import unittest

def sumNums(file):
    inputted = open(file,'r')
    readlines = inputted.readlines()
    inputted.close()
    sn = 0
    fl = []
    for line in readlines:
        line = line.rstrip()
        nums = re.findall('[0-9]+', line)

        for word in nums:
            finalList.append(int(word))
    for item in fl:
        sn += item
    return sn

def countWord(file, x):
    inputted = open(file, 'r')
    readlines = inputted.readlines()
    inputted.close()
    wc = 0
    for line in readlines:
        loW = re.findall(x + ('\\b'), line, re.IGNORECASE)
        for words in loW:
            wc += 1
    return wc 

def listURLs(file):
    inputted = open(file, 'r')
    readit = inputted.readlines()
    inputted.close()
    lurl = []
    for line in readit:
        line = line.rstrip()
        urls = re.findall(',*www.[a-zA-Z0-9]+.[a-z]{3}\S*', line)
        for url in urls:
            lurls.append(url)
    return lurls

##################UNITTESTS BELOW THIS LINE DON'T EDIT #############################
#GITHUB RESPOISTORY @ 
class TestHW6(unittest.TestCase):
    """ Class to test this homework """

    def test_sumNums1(self):
        """ test sumNums on the first file """
        self.assertEqual(sumNums("regex_sum_42.txt"), 445833)

    def test_sumNums2(self):
        """ test sumNums on the second file """
        self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)

    def test_countWord(self):
        """ test count word on the first file """
        self.assertEqual(countWord("regex_sum_42.txt", "computer"),21)

    def test_listURLs(self):
        """ test list URLs on the first file """
        self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)

# run the tests
unittest.main(verbosity=2)
