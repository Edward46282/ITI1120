class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'


class Rectangle:
    'class that represents a rectangle'
    def __init__(self, pointone, pointtwo, color):
        '''
        (Rectangle,Point,Point,str)-> None
        Initialize (self.po,self.pt,self.co)
        '''
        self.po = pointone
        self.pt = pointtwo
        self.co = color

    def __repr__(self):
        '''
        (Rectangle)-> str
        Canonical representation of the object
        '''
        return "Rectangle(" + str(self.po) +',' + str(self.pt) + ", '" + str(self.co) + "')"

    def get_color(self):
        '''
        (Rectangle)-> str
        returns the color of the rectangle
        '''
        return self.co

    def get_bottom_left(self):
        '''
        (Rectangle)-> Point
        returns the bottom left point
        '''
        return self.po

    def get_top_right(self):
        '''
        (Rectangle)-> Point
        returns the top right point
        '''
        return self.pt

    def reset_color(self, change_to):
        '''
        (Rectangle,str) -> None
        it changes the color of the rectangle
        '''
        self.co = change_to

    def move(self, dx, dy):
        '''
        (Rectangle,number,number)-> None
        It moves the rectangle if the x and y values of change are given.
        '''
        self.po.move(dx, dy)
        self.pt.move(dx, dy)

    def __str__(self):
        '''
        (Rectangle) -> str
        nice represantation of object
        '''
        return "I am a " + str(self.co) + " rectangle with bottom left corner at " + str(self.po.get()) + " and top right corner at " + str(self.pt.get()) + "."

    def __eq__(self, other):
        '''
        (Rectangle,Rectangle) -> bool
        it returns True if two given rectangles are same. Otherwise, False.
        '''
        return self.po == other.po and self.pt == other.pt and self.co == other.co

    def get_perimeter(self):
        '''
        (Rectangle) -> number
        it returns the perimeter of the rectangle.
        '''
        return (2*abs(self.po.x - self.pt.x)) + (2*abs(self.po.y - self.pt.y))

    def get_area(self):
        '''
        (Rectangle) -> number
        it returns the area of the rectangle.
        '''
        return (abs(self.po.x - self.pt.x) * abs(self.po.y - self.pt.y))

    def contains(self, dx, dy):
        '''
        (Rectangle,number,number) -> bool
        it returns True if the given point is in the rectengle. Otherwise, returns False.
        '''
        if dx >= self.po.x and dx <= self.pt.x and dy >= self.po.y and dy <= self.pt.y:
            return True
        else:
            return False

    def intersects(self, other):
        '''
        (Rectangle,Rectangle)-> bool
        it returns True if these two rectangles share at least one point. Otherwise, returns False.
        '''
        width1 = self.pt.x - self.po.x
        height1 = self.pt.y - self.po.y

        width2 = other.pt.x - other.po.x
        height2 = other.pt.y - other.po.y

        if (self.po.x <= other.po.x + width2) and (self.po.x + width1 >= other.po.x) and (self.po.y <= other.po.y + height2) and (self.po.y + height1 >= other.po.y):
            return True
        return False
        


class Canvas:
    'class that represents Canvas'
    list_ofrec = []
    def __init__(self):
        '''
        (Canvas) -> None
        initialize the list of rectangle
        '''
        self.list = Canvas.list_ofrec

    def __len__(self):
        '''
        (Canvas)->int
        it returns the length of the list
        '''
        return len(self.list)

    def add_one_rectangle(self, rectangle):
        '''
        (Canvas,Rectangle)-> None
        it adds a rectange to the list
        '''
        self.list.append(rectangle)

    def __repr__(self):
        '''
        (Cangas)-> str
        Canonical representation of the object
        '''
        return "Canvas("+str(self.list)+")"

    
    def count_same_color(self, color):
        '''
        (Canvas, str)-> int
        It counts the number of rectangles that have same color.
        '''
        color_count = []
        counter = 0

        for i in range(len(self.list)):
            color_count.append(self.list[i].get_color())

        for p in color_count:
            if p == color:
                counter += 1

        return counter

    def total_perimeter(self):
        '''
        (Canvas)-> number
        it returns the perimeters of all rectangles.
        '''
        perimeterc = 0
        for i in range(len(self.list)):
            perimeterc += self.list[i].get_perimeter()

        return perimeterc

    def min_enclosing_rectangle(self):
        '''
        (Canvas)-> Rectangle
        it returns the rectangle that contains all the rectangles in the Canvas
        '''
        minx = self.list[0].po.x
        miny = self.list[0].po.y
        maxx = self.list[0].pt.x
        maxy = self.list[0].pt.y
        
        for i in range(len(self.list)):
            if minx > self.list[i].po.x:
                minx = self.list[i].po.x

            if miny > self.list[i].po.y:
                miny = self.list[i].po.y

            if maxx < self.list[i].pt.x:
                maxx = self.list[i].pt.x

            if maxy < self.list[i].pt.y:
                maxy = self.list[i].pt.y

        return Rectangle(Point(minx,miny), Point(maxx,maxy), 'red')

    def common_point(self):
        '''
        (Canvas)-> bool
        it returns True if all the rectangles in Canvas have a common point.
        '''
        for i in range(len(self.list)-1):
            for p in range(i+1, len(self.list)):
                if self.list[i].intersects(self.list[p]) == False:
                    return False
        return True




                         
