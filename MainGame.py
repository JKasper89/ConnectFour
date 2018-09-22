from abc import ABC, abstractmethod
from enum import Enum


class MainGame:
    def __init__(self):
        self.__Board = None
        self.__Players = None

    def getBoard(self):
        return self.__Board
    Board = property(getBoard, None)

    def getPlayers(self):
        return self.__Players
    Players =  property(getPlayers, None)

    def startGame(self):
        raise NotImplementedError


class Board:

    def __init__(self, iSlots = [], iRows = [], iColumns = [], iDiagonals = []):
        if iSlots == None: raise AttributeError("Slots Missing")
        if iRows == None : raise AttributeError("Rows Missing")
        if iColumns == None : raise AttributeError("Columns Missing")
        if iDiagonals == None : raise AttributeError("Diagonals Missing")
        self.__Rows = iRows
        self.__Columns  = iColumns
        self.__Slots = iSlots
        self.__Diagonal = iDiagonals

    def getRows(self):
        return self.__Rows
    Rows = property(getRows, None)
    def getColumns(self):
        return self.__Columns
    Columns = property(getColumns, None)
    def getSlots(self):
        return self.__Slots
    Slots = property(getSlots, None)
    def getDiagonal(self):
        return self.__Diagonal
    Diagonal = property(getDiagonal, None)


class BoardFactory:

    def __init__(self):
        self.__Slots =  []
        self.__Columns = []
        self.__Rows = []
        self.__Diagonals = []

    def getSlots(self):
        return self.__Slots
    Slots=property(getSlots, None)

    def getColumns(self):
        return self.__Columns
    Columns = property(getColumns, None)

    def getRows(self):
        return self.__Rows
    Rows = property(getRows,None)

    def getDiagonals(self):
        return self.__Diagonals
    Diagonals = property(getDiagonals,None)

    def CreateBoard(self,rowsCount, columnCount):
        isinstance(columnCount, int)
        isinstance(rowsCount, int)
        if columnCount <=2 or rowsCount <= 2 :
            raise AttributeError("Column- and Row- number have to be greater than 2")
        #Create SlotArray
        self.__Slots = [[0 for x in range(rowsCount)] for y in range(columnCount)]
        for i in range(0,columnCount):
            for j in range (0,rowsCount):
                self.Slots[i][j] = Slot(i,j)
        #Create ColumnArray
        for i in range(0,columnCount):
            columnSlots = []
            for j in range(0,rowsCount):
                columnSlots.append(self.Slots[i][j])
            self.Columns.append(Column(columnSlots))

        #Create RowArray
        for j in range(0,rowsCount):
            rowSlots = []
            for i in range(0,columnCount):
                rowSlots.append(self.Slots[i][j])
            self.Rows.append(Row(rowSlots))
        #Create DiagonalArray
        #LeftUp to RightDown
        diagonalDirection = DiagonalDirection.DownRight
        for i in range(0, columnCount):
            columnIndex = i
            rowsIndex = 0
            diagonalSlots=[]
            while columnIndex < columnCount and rowsIndex < rowsCount :
                diagonalSlots.append(self.Slots[columnIndex][rowsIndex])
                columnIndex += 1
                rowsIndex += 1
            if diagonalSlots.__len__() >= 4:
                self.Diagonals.append(Diagonal(i,0, diagonalDirection,diagonalSlots))
        for j in range(1,rowsCount):
            columnIndex = 0
            rowsIndex = j
            diagonalSlots = []
            while columnIndex < columnCount and rowsIndex < rowsCount:
                diagonalSlots.append(self.Slots[columnIndex][rowsIndex])
                columnIndex += 1
                rowsIndex += 1
            if diagonalSlots.__len__() >= 4:
                self.Diagonals.append(Diagonal(0,j,diagonalDirection, diagonalSlots))
        #RightUp To LeftDown
        diagonalDirection = DiagonalDirection.DownLeft
        for i in range(0, columnCount):
            columnIndex = i
            rowsIndex = 0
            diagonalSlots = []
            while  columnIndex >=0 and rowsIndex < rowsCount:
                diagonalSlots.append(self.Slots[columnIndex][rowsIndex])
                columnIndex -= 1
                rowsIndex += 1
            if diagonalSlots.__len__() >= 4:
                self.Diagonals.append(Diagonal(i, 0, diagonalDirection, diagonalSlots))
        for j in range(1, rowsCount):
            columnIndex = columnCount -1
            rowsIndex = j
            diagonalSlots = []
            while columnIndex >= 0 and rowsIndex < rowsCount:
                diagonalSlots.append(self.Slots[columnIndex][rowsIndex])
                columnIndex -= 1
                rowsIndex  += 1
            if diagonalSlots.__len__() >= 4:
                self.Diagonals.append(Diagonal(columnCount-1, j, diagonalDirection, diagonalSlots))

        return Board(self.Slots, self.Rows, self.Columns, self.Diagonals)





class Coin:

    def __init__(self, value, value2):
        isinstance(value, Colour)
        if value == None:
            raise ValueError("Colour Missing!")
        isinstance(value2, str)
        if value2 == None:
            raise ValueError("Name Missing!")
        self.__Colour = value
        self.__PlayerName = value2

    def getColour(self):
        return self.__Colour
    Colour = property(getColour, None)

    def getPlayerName(self):
        return self.__PlayerName
    PlayerName = property(getPlayerName, None)


class Colour:
    def __init__(self,value, value2, value3):
        isinstance(value, list)
        if value == None:
            raise ValueError("Red Missing!")
        if value2 == None:
            raise ValueError("Yellow Missing!")
        if value3 == None:
            raise ValueError("Blue Missing!")
        self.__Red = value
        self.__Yellow = value2
        self.__Blue = value3


class IColumn(ABC):

    def __init__(self):
        self.__Slots = None

    def getSlots(self):
        return self.__Slots
    Slots = property(getSlots, None)

    @abstractmethod
    def DropCoin(self, value):
        pass

    @abstractmethod
    def IsColumnFull(self):
        pass


class Line(ABC):

    def __init__(self, value = None):
        isinstance(value,list)
        if value == None:
            value = []
            raise ValueError("Slots Missing!")
        self.__Slots = value

    def getSlots(self):
        return self.__Slots
    Slots = property(getSlots, None)

    def checkIfFourConnect(self):
        self.__counter = 0
        self.__actualPlayerName = None

        for Slot in self.Slots:
            self.__Coin = Slot.Coin
            if Slot.Coin == None:
                self.__actualPlayerName = None
                self.__counter = 0
                continue
            if self.__actualPlayerName != self.__Coin.PlayerName:
                self.__actualPlayerName = self.__Coin.PlayerName
                self.__counter = 1
                continue
            self.__counter += 1
            if self.__counter >= 4:
                return self.__actualPlayerName
        return None


class Column(Line,IColumn):
    def __init__(self, value):
        super().__init__(value)

    def DropCoin(self, value):
        isinstance(value, Coin)

        for slot in self.Slots:
            if slot.Coin == None:
                slot.Coin  = value
                return

        raise AttributeError("Column is full!")

    def IsColumnFull(self):
        for Slot in self.Slots:
            if Slot.Coin == None:
                return False
        return True




class Player:

    def __init__(self, iName, iLCoins = None):
        isinstance(iName,str)
        isinstance(iLCoins,list)
        if iName is None:
            raise ValueError("Name Missing")
        if iLCoins is None:
            iLCoins = []
        self.__Name = iName
        self.__Coins = iLCoins

    def getName(self):
        return self.__Name
    Name = property(getName, None)

    def getCoins(self):
        return self.__Coins
    Coins = property(getCoins, None)

    def makeTurn(self,iColumn):
        isinstance(iColumn, type(Column))
        if iColumn == None:
            raise ValueError("Column missing!")

        self.__topCoin = self.__Coins[0]
        self.__Coins.__delitem__(0)

        iColumn.DropCoin(self.__topCoin)


class Row(Line):

    def __init__(self, value):
        super().__init__(value)


class Slot:

    def __init__(self,iX, iY):
        self.__Coin = None
        isinstance(iX, int)
        isinstance(iY, int)
        if iX < 0 : raise AttributeError("X-coordinate")
        if iY < 0 : raise AttributeError("Y-coordinate")
        self.__X = iX
        self.__Y = iY

    def getCoin(self):
        return self.__Coin
    def setCoin(self,value):
        isinstance(value,Coin)
        self.__Coin = value
    Coin = property(getCoin, setCoin)

    def getX(self):
        return self.__X
    X = property(getX,None)

    def getY(self):
        return self.__Y
    Y = property(getY,None)

    def __str__(self):
        return "Slot " + self.__X + ", " + self.__Y


class Diagonal(Line):
    def __init__(self,iStartIndexX, iStartIndexY, iDiagonalDirection, iSlots):
        if iStartIndexX < 0 : raise AttributeError("StartIndexX")
        if iStartIndexY < 0 : raise AttributeError("StartIndexY")
        self.__StartIndexX = iStartIndexX
        self.__StartIndexY = iStartIndexY
        self.__DiagonalDirection = iDiagonalDirection
        super().__init__(iSlots)

    def getStartIndexX(self):
        return self.__StartIndexX
    StartIndexX = property(getStartIndexX, None)

    def getStartIndexY(self):
        return self.__StartIndexY
    StartIndexY = property(getStartIndexY, None)

    def getDiagonalDirection(self):
        return self.__DiagonalDirection
    DiagonalDirection = property(getDiagonalDirection, None)


class DiagonalDirection(Enum):
    DownLeft = 1
    DownRight = 2
