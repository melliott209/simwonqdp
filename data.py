class DataPoint:
    def __init__(self,label):
        self.__label = label
        self.__Diameter = dict.fromkeys(["Nominal","Measured","Tolerance","Deviation"])
        self.__Length = dict.fromkeys(["Nominal","Measured","Tolerance","Deviation"])
        self.__Width = dict.fromkeys(["Nominal","Measured","Tolerance","Deviation"])
        self.__X = dict.fromkeys(["Nominal","Measured","Tolerance","Deviation"])
        self.__Y = dict.fromkeys(["Nominal","Measured","Tolerance","Deviation"])
        self.__Z = dict.fromkeys(["Nominal","Measured","Tolerance","Deviation"])

    def update(self,control,key,value):
        if control == "Diameter":
            self.__Diameter[key] = value
        elif control == "Length":
            self.__Length[key] = value
        elif control == "Width":
            self.__Width[key] = value
        elif control == "X":
            self.__X[key] = value
        elif control == "Y":
            self.__Y[key] = value
        elif control == "Z":
            self.__Z[key] = value

    def getLabel(self):
        return self.__label

class Part:
    def __init__(self):
        self.datapoints = list()

    def getData(self):
        return self.datapoints

    def pointIndex(self,label):
        for point in self.datapoints:
            if point.getLabel() == label:
                return index(point)
        return -1
        
    def addData(self,label,control,nom,meas,tol,dev):
        index = self.pointIndex(label)
        realControl = control
        if realControl == "Edge Point X" or realControl == "Surface Point X":
            realControl = "X"
        elif realControl == "Edge Point X" or realControl == "Surface Point X":
            realControl = "Y"
        elif realControl == "Edge Point X" or realControl == "Surface Point X":
            realControl = "Z"
        
        if index != -1:
            self.datapoints[index].update(realControl,"Nominal",nom)
            self.datapoints[index].update(realControl,"Measured",meas)
            self.datapoints[index].update(realControl,"Tolerance",tol)
            self.datapoints[index].update(realControl,"Deviation",dev)
        else:
            self.datapoints.append(label)
            index = self.pointIndex(label)
            self.datapoints[index].update(realControl,"Nominal",nom)
            self.datapoints[index].update(realControl,"Measured",meas)
            self.datapoints[index].update(realControl,"Tolerance",tol)
            self.datapoints[index].update(realControl,"Deviation",dev)

