class DataPoint:
    def __init__(self,label,typ):
        self.__label = label
        self.__typ = typ
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

    def getDia(self):
        return self.__Diameter

    def getLen(self):
        return self.__Length

    def getWid(self):
        return self.__Width

    def getX(self):
        return self.__X

    def getY(self):
        return self.__Y

    def getZ(self):
        return self.__Z

    def getCSV(self):
        if self.__typ == "Hole":
            return self.__label + ',' + self.__typ + ',' + "{:.3f}".format(self.__X["Nominal"]) + ',' + "{:.3f}".format(self.__X["Measured"]) + ',' + "{:.3f}".format(self.__X["Deviation"]) + ',' + "{:.3f}".format(self.__Y["Nominal"]) + ',' + "{:.3f}".format(self.__Y["Measured"]) + ',' + "{:.3f}".format(self.__Y["Deviation"]) + ',' + "{:.3f}".format(self.__Z["Nominal"]) + ',' + "{:.3f}".format(self.__Z["Measured"]) + ',' + "{:.3f}".format(self.__Z["Deviation"]) + ',' + "{:.3f}".format(self.__Diameter["Measured"]) + ',' + "N/A" + '\n'
        elif self.__typ == "Slot":
            return self.__label + ',' + self.__typ + ',' + "{:.3f}".format(self.__X["Nominal"]) + ',' + "{:.3f}".format(self.__X["Measured"]) + ',' + "{:.3f}".format(self.__X["Deviation"]) + ',' + "{:.3f}".format(self.__Y["Nominal"]) + ',' + "{:.3f}".format(self.__Y["Measured"]) + ',' + "{:.3f}".format(self.__Y["Deviation"]) + ',' + "{:.3f}".format(self.__Z["Nominal"]) + ',' + "{:.3f}".format(self.__Z["Measured"]) + ',' + "{:.3f}".format(self.__Z["Deviation"]) + ',' + "{:.3f}".format(self.__Length["Measured"]) + ',' + "{:.3f}".format(self.__Width["Measured"]) + '\n'
        elif self.__typ == "Edge":
            return self.__label + ',' + self.__typ + ',' + "{:.3f}".format(self.__X["Nominal"]) + ',' + "{:.3f}".format(self.__X["Measured"]) + ',' + "{:.3f}".format(self.__X["Deviation"]) + ',' + "{:.3f}".format(self.__Y["Nominal"]) + ',' + "{:.3f}".format(self.__Y["Measured"]) + ',' + "{:.3f}".format(self.__Y["Deviation"]) + ',' + "{:.3f}".format(self.__Z["Nominal"]) + ',' + "{:.3f}".format(self.__Z["Measured"]) + ',' + "{:.3f}".format(self.__Z["Deviation"]) + ',' + "N/A" + ',' + "N/A" + '\n'
        elif self.__typ == "Surface":
            return self.__label + ',' + self.__typ + ',' + "{:.3f}".format(self.__X["Nominal"]) + ',' + "{:.3f}".format(self.__X["Measured"]) + ',' + "{:.3f}".format(self.__X["Deviation"]) + ',' + "{:.3f}".format(self.__Y["Nominal"]) + ',' + "{:.3f}".format(self.__Y["Measured"]) + ',' + "{:.3f}".format(self.__Y["Deviation"]) + ',' + "{:.3f}".format(self.__Z["Nominal"]) + ',' + "{:.3f}".format(self.__Z["Measured"]) + ',' + "{:.3f}".format(self.__Z["Deviation"]) + ',' + "N/A" + ',' + "N/A" + '\n'
        else:
            return "Invalid Type"

    def getComparisonPoints(self):
        if self.__typ == "Hole":
            points = list(self.__Diameter["Measured"],self.__X["Measured"],self.__Y["Measured"],self.__Z["Measured"])
        elif self.__typ == "Slot":
            points = list(self.__Length["Measured"],self.__Width["Measured"],self.__X["Measured"],self.__Y["Measured"],self.__Z["Measured"])
        elif self.__typ == "Edge":
            points = list(self.__X["Measured"],self.__Y["Measured"],self.__Z["Measured"])
        elif self.__typ == "Surface":
            points = list(self.__X["Measured"],self.__Y["Measured"],self.__Z["Measured"])

        return points

class Part:
    def __init__(self):
        self.datapoints = list()

    def getData(self):
        return self.datapoints

    def pointIndex(self,label):
        for point in self.datapoints:
            if point.getLabel() == label:
                return self.datapoints.index(point)
        return -1
        
    def addData(self,label,control,nom,meas,tol,dev):
        index = self.pointIndex(label)
        realControl = control
        typ = ''
        if realControl == "Edge Point X" or realControl == "Surface Point X":
            realControl = "X"
        elif realControl == "Edge Point Y" or realControl == "Surface Point Y":
            realControl = "Y"
        elif realControl == "Edge Point Z" or realControl == "Surface Point Z":
            realControl = "Z"
        elif realControl == "Edge Distance" or realControl == "Surface Distance":
            return
        
        if index != -1:
            self.datapoints[index].update(realControl,"Nominal",nom)
            self.datapoints[index].update(realControl,"Measured",meas)
            self.datapoints[index].update(realControl,"Tolerance",tol)
            self.datapoints[index].update(realControl,"Deviation",dev)
        else:
            if label[:1] == "H":
                typ = "Hole"
            elif label[:1] == "M" or label[:1] == "L":
                typ = "Slot"
            elif label[:1] == "E":
                typ = "Edge"
            elif label[:1] == "S":
                typ = "Surface"
            self.datapoints.append(DataPoint(label,typ))
            index = self.pointIndex(label)
            self.datapoints[index].update(realControl,"Nominal",nom)
            self.datapoints[index].update(realControl,"Measured",meas)
            self.datapoints[index].update(realControl,"Tolerance",tol)
            self.datapoints[index].update(realControl,"Deviation",dev)

    def getCSV(self):
        matrix = list()
        for point in self.datapoints:
            matrix.append(point.getCSV())
        return matrix

    def getComparisonPoints(self):
        points = list()
        for point in self.datapoints:
            points.append(point.getComparisonPoints())
        return points

