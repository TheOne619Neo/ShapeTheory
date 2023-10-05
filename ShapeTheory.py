

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)

from cgi import print_arguments
from curses.ascii import isdigit


def get_shape():                                                                                                 #define a function called get_shape that can hold various various shape options from users input
    valid_shape = ["pyramid","square","triangle", "rectangle", "parallelogram", "gun"]                                                                #define a list of valid shape words 
    #shape = input("Select shape. The shape (it must be either pyramid, square or triangle) ")                   
    while True:                                                                                                  #create a loop that will repeat getting user input 
        shape = input(" Shape?:").lower().strip()                                                                #get user input and save in variable named shape and ensure user can enter capital letters or space and still be readible
        if shape in valid_shape:                                                                                 #check to see if users input is amongst the valid shapes list
            break                                                                                                #break out of the loop once user enters correct shape options
    return shape                                                                                                 #and store users input in function
    """else:                                                                                                     #alternatively use recurrsion instead of a loop if users input is not a valid option from the list then loop back and prompt the user to re-enter a option
        get_shape()"""




def get_height():                                                                                               #define a function called get_height that holds the row height of each shape
    while True:                                                                                                 #create a loop that will repeat getting user input
        height= input("Height?: ")                                                                              #get user input
        #height = int(choice)
   #height = int.input("Select height. The height (with a max of 80) ")                                       
        if height.isdigit():                                                                                    #test to see if user input is a digit, a numerical value if true enter block 
            if int(height) <= 80:                                                                               #test to see if user input is smaller than 80 or equal to and convert users input into a int value to test 
                break                                                                                           #break out of loop once the conditional test statements are met 
    return int(height)                                                                                          #and return user input as an interget to the function 
    """ else:                                                                                                   #alternatively used an if else statements  as opposed to a loop calling the function to loop back when users input are incorrect
             get_height()                                                                                       
   else:
         get_height() """                                                                                          



def draw_pyramid(height, outline):
    
    """sp = height -1

    for i in range(1,height, 2):
        for space in range(sp,i, -1):
            print(" ",end="")
   
        for star in range(height):
            print("*", end="")
        print()
        #print('pyramid')"""
    if outline == False:                                                                                       #an if statement that checks whether to use the solid or outline segment code of the pyramid  
        for row in range(height):                                                                              #create for loop to determine highest number of row, the hieght of the shape
            for col in range(height-row-1):                                                                    #create for loop that determines the spaces, iterate first before starting next loop that will draw shape 
                print(" ", end="")                                                                             #considering y axis and x axis, print empty spaces where there would be another invisble upside down right angle triangle
            for j in range(2* row + 1):                                                                        #create loop that determines shape using astrix in pyramid format
                print("*", end="")                                                                             #print axtrix in the shape of a pyramid 
            print()                                                                                            #ensure cursor goes to the next line when done
    else:
        for row in range(height):                                                                              #an outline segment code of the above code of the pyramid shape.
            for col in range(height-row-1):
                print(" ", end="")
            for col in range(2* row + 1):
                if (col == 0) or (col == 2*row) or (row == height - 1):
                #if col == height -1 or col == 2* row or col == height - row:
                    print("*", end="")
                else:
                        print(" ", end="")  
            print()

def draw_square(height, outline):                                                                             #declare a function that draws the shape of a square
    if outline == False:                                                                                      #a conditional statement that determines whether the output should produce an outline or solid version of the shape
        for row in range(height):                                                                             #a for loop that uses the height to determine the shape 
            for col in range(height):
                print("*", end="")                                                                                                                                                                                                                        
            print()
    else:
            for row in range(1, height+1):                                                                   #an outline version of the segment code above for drawing a square
                for col in range(1,height+1):
                    if (row == 1) or (row == height) or (col == 1) or (col == height):
                        print("*", end="")
                    else:
                        print(" ", end="")  
                print()


def draw_triangle(height, outline):                                                                         #A function created to hold loops that will create a triangle shape 
    if outline == False:
        for row in range(height):
            for col in range(row + 1):
                print("*", end="")
            print()
    else:                                                                                                   #function holds both a outline and solid version of the shape
        for row in range(1, height+1):
            for col in range(1, row + 1):
      
                if (row == col) or (col == 1) or (row == height):
                    print("*", end="")
                else:
                    print(" ", end="")
            print() 

 
"""Step 6 :To get used to understanding how all this works 3 more shapes were created and edited throughout the program."""

def draw_rectangle(height):                                                                                #A function declared called draw rectangle                     
                                                                                                           #the functions purpose is to draw a rectangle
    for y in range(height-4):                                                                              #the loop is designed to decrease the users input height range with a minus four making the length shorter and differentiating from a square.
        for x in range(height):                                                                            
            print("*",end=" ")
        print()
                                                          #RECTANGLE                                       
                                                                   
def draw_parallelogram(height):                                                                           #A function declared called draw parallelogram 
    for y in range(height):                                                                               #how the loops work was by first shaping an upside down right angle triangle to determine the spaces 
        for space in range(height-y):                                                                     #then ultimately using the square method loop 
            print(" ",end=" ")
        for x in range(height+6):
            print("*",end=" ")
        print()
                                                         #Parallelogram

def draw_Sniper_Gun_Shape(height):                                                                       #A function declared meant to draw a AK-47 Gun shape 
    for y in range(height):                                                                              
        for space in range(height-y-1):
            print("  ", end="")
            for x in range(2*y+1):
                print("*", end="")
            print()
                                                       #AK-47 Gun Shape
"""The above shapes do not have outline options only draws solid shapes""" #Had fun learning how to perform various shapes 



# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):                                                                       #a function that holds the shape, height and outline of each shape
                                                                                                        #enables each shape to be able to be drawn
    if   shape == 'pyramid':                                                                    
        return draw_pyramid(height, outline)
    elif shape == 'square': 
        return draw_square(height, outline)
    elif shape == 'triangle': 
          return draw_triangle(height, outline)
    elif shape == 'rectangle':
         return draw_rectangle(height)
    elif shape == 'gun':
          return draw_Sniper_Gun_Shape(height)
    elif shape == 'parallelogram':
          return draw_parallelogram(height)
    
   


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():                                                                                     #The function that determines whether a outline or a solid shape should be returned
    #option =['y', 'N']
    
    while True:
        ask = input("Outline only? (y/N): ").upper().strip()
        if ask == 'N':
            
            return False
        elif  ask == 'Y':
            break
    return True


if __name__ == "__main__":                                                                           #The main function where all other functions created in the class can be called.
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

