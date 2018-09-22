import unittest
from MainGame import *
class PlayerTest(unittest.TestCase):

    def testcase__00(self):  #DeleteOnePlayerCoin

        coins = [Coin(Colour(128,0,0),"Foo"),
                 Coin(Colour(128,0,0),"Foo")]
        initialCount = coins.__len__()
        testTarget = Player("foo", coins)


        testTarget.makeTurn(ColumnDummy())
        self.assertEqual(initialCount-1, testTarget.Coins.__len__())

    def testcase__01(self): #MakeTurnDropsCoin

        coins = [Coin(Colour(128,0,0),"Foo"),
                 Coin(Colour(128,0,0),"Foo")]
        initialCount = coins.__len__()
        testTarget = Player("foo", coins)
        column = ColumnDummy()

        testTarget.makeTurn(column)
        self.assertTrue(column.IsCoinDropped())

class LineTest(unittest.TestCase):

    def testcase__00(self): #FourInARow
        slots = []
        for i in range(0,4):
            testSlot = Slot(0,i)
            testSlot.Coin = Coin(Colour(128,0,0), "Foo")
            slots.append(testSlot)
        testTarget = LineDummy(slots)
        playerName = testTarget.checkIfFourConnect()
        self.assertEqual(playerName,"Foo")

    def testcase__01(self): #NotFourInARow
        slots = []
        for i in range(0,4):
            testSlot = Slot(0,i)
            testSlot.Coin = Coin(Colour(128,0,0), "Foo")
            if i == 2 : testSlot.Coin = Coin(Colour(0,128,0), "Bar")
            slots.append(testSlot)
        testTarget = LineDummy(slots)
        playerName = testTarget.checkIfFourConnect()
        self.assertEqual(playerName, None)

    def testcase__02(self): #FourInARow
        slots = []
        for i in range(0,4):
            testSlot = Slot(0,i)
            testSlot.Coin = Coin(Colour(0,128,0), "Bar")
            slots.append(testSlot)
        testTarget = LineDummy(slots)
        playerName = testTarget.checkIfFourConnect()
        self.assertEqual(playerName, "Bar")

    def testcase__03(self): #FourInARow
        slots = []
        for i in range(0,6):
            testSlot = Slot(0,i)
            testSlot.Coin = Coin(Colour(0,128,0), "Bar")
            if i == 1 : testSlot.Coin = None
            slots.append(testSlot)
        testTarget = LineDummy(slots)
        playerName = testTarget.checkIfFourConnect()
        self.assertEqual(playerName, "Bar")


class ColumnTest(unittest.TestCase):

    def testcase_00(self): #DropCoinInEmptyColumn
        slots = []
        for i in range(0,6):
            slots.append(Slot(0,i))
        testTarget = Column(slots)
        testCoin = Coin(Colour(0,0,0),"Foo")

        testTarget.DropCoin(testCoin)

        for i in range(0,slots.__len__()):
            if i == 0:
                self.assertEqual(testCoin,slots[0].Coin)
                continue
            self.assertIsNone(slots[i].Coin)

    def testcase_01(self): #DropCoinInFullColumn
        slots = []
        testCoin = Coin(Colour(0,0,0),"Foo")
        for i in range(0,6):
            testSlot = Slot(0,i)
            testSlot.Coin = testCoin
            slots.append(testSlot)
        testTarget = Column(slots)

        with self.assertRaises(AttributeError):
            testTarget.DropCoin(testCoin)

    def testcase_02(self): #IsColumnFull
        slots = []
        testCoin = Coin(Colour(0,0,0),"Foo")
        for i in range(0,6):
            testSlot = Slot(0,i)
            testSlot.Coin = testCoin
            slots.append(testSlot)
        testTarget = Column(slots)

        self.assertTrue(testTarget.IsColumnFull())

    def testcase_03(self): #IsColumnNotFull
        slots = []
        testCoin = Coin(Colour(0,0,0),"Foo")
        for i in range(0,6):
            testSlot = Slot(0,i)
            testSlot.Coin = testCoin
            slots.append(testSlot)
        slots.append(Slot(0,7))
        testTarget = Column(slots)

        self.assertFalse(testTarget.IsColumnFull())

class BoardFactoryTest(unittest.TestCase):


    def testcase_00(self):
        testTarget = BoardFactory()
        testBoard = testTarget.CreateBoard(6,7)
        self.assertEqual(6,testBoard.Rows.__len__())


    def testcase_01(self):
        testTarget = BoardFactory()
        testBoard = testTarget.CreateBoard(6, 7)
        self.assertEqual(7,testBoard.Columns.__len__())

    def testcase__02(self):
        testTarget = BoardFactory()
        testBoard = testTarget.CreateBoard(6, 7)
        column3 = testBoard.Columns[2]

        for slot in column3.Slots:
            self.assertTrue(2 == slot.X)

    def testcase__03(self):
        testTarget = BoardFactory()
        testBoard = testTarget.CreateBoard(6, 7)
        row4 = testBoard.Rows[3]

        for slot in row4.Slots:
            self.assertTrue(3 == slot.Y)

    def testcase__04(self):
        testTarget = BoardFactory()
        testBoard = testTarget.CreateBoard(6,7)
        testDiagonal = None
        for diagonal in testBoard.Diagonal:
            if diagonal.DiagonalDirection == DiagonalDirection.DownLeft and diagonal.StartIndexX == 5 and diagonal.StartIndexY == 0:
                testDiagonal = diagonal
                break
        firstSlot = testDiagonal.Slots[0]
        lastSlot = testDiagonal.Slots[-1]

        self.assertTrue(firstSlot.X == 5 and firstSlot.Y == 0)
        self.assertTrue(lastSlot.X == 0 and lastSlot.Y == 5)

    def testcase__05(self):
        testTarget = BoardFactory()
        testBoard = testTarget.CreateBoard(6,7)
        testDiagonal = None
        for diagonal in testBoard.Diagonal:
            if diagonal.DiagonalDirection == DiagonalDirection.DownRight and diagonal.StartIndexX == 0 and diagonal.StartIndexY == 2:
                testDiagonal = diagonal
                break
        firstSlot = testDiagonal.Slots[0]
        lastSlot = testDiagonal.Slots[-1]

        self.assertTrue(firstSlot.X == 0 and firstSlot.Y == 2 )
        self.assertTrue(lastSlot.X  == 3 and lastSlot.Y == 5)

    def testcase__06(self):
        testTarget = BoardFactory()
        testBoard = testTarget.CreateBoard(6, 7)
        for diagonal in testBoard.Diagonal:
            self.assertTrue(diagonal.Slots.__len__() >= 4)





class ColumnDummy(IColumn):
    def __init__(self):
        super().__init__()
        self.__countDropCoin = 0

    def DropCoin(self, Coin):
        self.__countDropCoin +=1

    def IsCoinDropped(self):
        if self.__countDropCoin == 1:
            return True
        else:
            return False
    def IsColumnFull(self):
        NotImplementedError


class LineDummy(Line):
    def __init__(self, value):
        super().__init__(value)





if __name__ == "__main__":
    unittest.main()
