import turtle
#1.ending1-death
def ending1():
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.title("Castle Escape - Ending")
    t.goto(100, -100)  
    t.color("white")
    t.write("YOU DIED!", move=True, align="left", font=("Arial", font_size:=30, "bold")) 

    t.color("white")        
    t.pensize(4)        
    t.speed(8)             

    # === 2. head ===
    t.penup()              
    t.goto(0, -50)          
    t.pendown()             
    t.setheading(0)          
    t.circle(100)           

    # === 3. draw ===
 
    t.penup()
    t.goto(-60, 0)          
    t.pendown()
    t.setheading(270)   
    t.forward(80)         
    t.left(90)               
    t.forward(120)           
    t.left(90)           
    t.forward(80)           

    # === 4. tooth ===

    for x in range(-30, 40, 30): 
        t.penup()
        t.goto(x, 0)     
        t.pendown()
        t.goto(x, -80)       

    # === 5. eye ===
    def draw_eye(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.circle(25)        

    draw_eye(-40, 50)       
    draw_eye(80, 50)       

    # === 6. fork ===
    t.penup()
    t.pensize(10)   
    t.goto(-30, -160)           
    t.pendown()
    t.right(45)      
    t.forward(100)
    t.penup()            
    t.goto(30, -150)  
    t.pendown()
    t.left(90)      
    t.forward(100)        

    t.hideturtle()          
    turtle.done()   

#2.ending2-survive
def ending2():
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.title("Castle Escape - Ending")
    t.goto(100, -100)  
    t.color("white")
    t.write("SUCCESSFUL ESCAPE!", move=True, align="left", font=("Arial", font_size:=25, "bold"))
    def face():
        t.penup()
        t.goto(0, -100)
        t.setheading(0)
        t.pendown()
        t.circle(100)

    def eye():
        t.penup()
        t.goto(-40, 20)
        t.pendown()
        t.fillcolor("black")
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        
        t.penup()
        t.goto(40, 20)
        t.pendown()
        t.begin_fill()
        t.circle(10)
        t.end_fill()

    def smile():
        t.penup()
        t.goto(-50, -20)
        t.setheading(290)
        t.pendown()
        t.width(3)
        t.pencolor("black")
        t.circle(55, 140)

    def smileface():
        t.speed(5)
        t.begin_fill()
        t.color("yellow")
        face()
        t.end_fill()
        
        eye()
        smile()
        t.hideturtle()
        turtle.done()

    smileface()
#3.ending3-crazy
def ending3():
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.title("Castle Escape - Ending")
    t.speed(5)
    t.goto(100, -100)  
    t.color("white")
    t.write("YOU ARE CRAZY!", move=True, align="left", font=("Arial", font_size:=30, "bold"))
    def face():
        t.penup()
        t.goto(0, -100)
        t.setheading(0)
        t.pendown()
        t.color("black", "red") 
        t.begin_fill()
        t.circle(100)
        t.end_fill()

    def eye_cross(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.color("black")
        t.width(5)
        
        size = 15
        t.setheading(45)
        t.forward(size)
        t.backward(size * 2)
        t.forward(size)
        
        t.setheading(135)
        t.forward(size)
        t.backward(size * 2)
        t.forward(size)

    def toothy_mouth():
        t.penup()
        t.goto(-50, -30)
        t.setheading(0)
        t.pendown()
        t.width(2)
        t.color("black", "white")
        t.begin_fill()
        
        for _ in range(2):
            t.forward(100)
            t.right(90)
            t.forward(40)
            t.right(90)
        t.end_fill()
        
        t.color("black")
        
        t.penup()
        t.goto(-50, -50)
        t.pendown()
        t.forward(100)
        
        t.setheading(270)
        for i in range(1, 5):
            t.penup()
            t.goto(-50 + i * 20, -30)
            t.pendown()
            t.forward(40)

    face()
    eye_cross(-40, 20)
    eye_cross(40, 20)
    toothy_mouth()
    
    t.hideturtle()
    turtle.done()