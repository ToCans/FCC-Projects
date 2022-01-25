class Rectangle:

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def set_width(self,width_input):
        self.width = width_input

    def set_height(self,height_input):
        self.height = height_input
    
    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = (2 * self.width + 2 * self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            top = "*" * self.width + "\n"
            shape_output = top

            if self.height > 2:
                for self.index in range(self.height-2):
                    inner_middle = ("*" * self.width) + "\n"
                    shape_output += inner_middle
                
            bot = "*" * self.width + "\n"
            shape_output += bot

            return shape_output

    def get_amount_inside(self,shape_inp):
        base_area = self.width * self.height
        shape_area = shape_inp.height * shape_inp.width
        fits = int(base_area / shape_area)
        return fits

    def __str__(self):
        string = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
        return string

### Square Class ###
class Square(Rectangle):
    def __init__(self,width):
        self.width = width
        self.height = width

    def set_side(self,width):
        self.width = width
        self.height = width

    def __str__(self):
        string = "Square(side=" + str(self.width) + ")"
        return string