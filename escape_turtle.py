import turtle

# ==========================================
# 0. base
# ==========================================
screen = turtle.Screen()
screen.title("Castle Escape - Floor Plan")
screen.setup(width=900, height=700)
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.width(2)

# ==========================================
# 1. Title
# ==========================================

def draw_gradient_title(text, font_size=60):
    screen.bgcolor("#0E0E72") 
    turtle.colormode(255)
    t = turtle.Turtle()
    t.hideturtle() 
    t.speed(0)    
    t.penup()
    
    start_x = -(len(text) * font_size * 0.4) 
    t.goto(start_x, 200)
    total_chars = len(text)
    
    for index, char in enumerate(text):
        if total_chars > 1:
            progress = index / (total_chars - 1)
        else:
            progress = 0
            
        r_val = int(255 * (1 - progress)) 
        g_val = 0
        b_val = 0
        
        t.pencolor(r_val, g_val, b_val)
        
        t.write(char, move=True, align="left", font=("Arial", font_size, "bold"))

# ==========================================
# 2. furnitures
# ==========================================

def draw_bed(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("white")
    # bed
    for _ in range(2):
        pen.forward(50)
        pen.left(90)
        pen.forward(80)
        pen.left(90)
    # pillow
    pen.penup()
    pen.goto(x, y + 60)
    pen.pendown()
    pen.setheading(0)
    pen.forward(50)

def draw_toilet(x, y):
    pen.color("white")
    # washing
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.setheading(0)
    for _ in range(2):
        pen.forward(15)
        pen.left(90)
        pen.forward(30)
        pen.left(90)
    #standing
    pen.penup()
    pen.goto(x + 25, y + 5)
    pen.pendown()
    pen.circle(10)

def draw_cutlery(x, y):
    pen.color("white")
    # fork
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.setheading(90)
    pen.forward(20)
    pen.backward(20)
    pen.forward(25)
    pen.left(90)
    pen.forward(4)
    pen.backward(8)
    pen.forward(4)
    pen.right(90)
    # knife
    pen.penup()
    pen.goto(x + 15, y)
    pen.pendown()
    pen.forward(25)

def draw_dining_set(x, y):
    pen.color("white")
    radius = 25
    chair_size = 12
    # table
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.setheading(0)
    pen.circle(radius)
    # chair
    center_x = x
    center_y = y + radius
    def draw_square(cx, cy):
        pen.penup()
        pen.goto(cx, cy)
        pen.pendown()
        pen.setheading(0)
        for _ in range(4):
            pen.forward(chair_size)
            pen.left(90)
    draw_square(center_x - chair_size/2, center_y + radius + 5)
    draw_square(center_x - chair_size/2, center_y - radius - 15)
    draw_square(center_x - radius - 15, center_y - chair_size/2)
    draw_square(center_x + radius + 5, center_y - chair_size/2)

# --- map drawing ---
def draw_house_plan():
    
    TEXT_COLOR = "#C30000"
    WALL_COLOR = "white"

    def draw_room(x, y, w, h):
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.color(WALL_COLOR)
        pen.setheading(0)
        for _ in range(2):
            pen.forward(w)
            pen.left(90)
            pen.forward(h)
            pen.left(90)

    def make_door(x, y, horizontal=True):
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.color("grey")
        pen.width(4)
        pen.setheading(0)
        if horizontal:
            pen.forward(40)
        else:
            pen.left(90)
            pen.forward(40)
            pen.right(90)
        pen.width(2)
        pen.color("black")

    def write_label(x, y, text):
        pen.penup()
        pen.goto(x, y)
        pen.color(TEXT_COLOR)
        pen.write(text, align="center", font=("Arial", 12, "bold"))

    # Hall
    draw_room(-50, -100, 140, 200)
    # Bedroom
    draw_room(-220, -100, 170, 150)
    # Bathroom
    draw_room(-320, -60, 100, 80)
    # Kitchen
    draw_room(90, 20, 140, 120)

    # 2. door
    make_door(-50, -60, horizontal=False)
    make_door(-220, -40, horizontal=False)
    make_door(90, 50, horizontal=False)

    # 3. named
    write_label(-135, -60, "[bedroom]")
    write_label(-270, -10, "[bathroom]")
    write_label(20, 60, "[hall]")
    write_label(160, 30, "[kitchen]")

# ==========================================
# 3. main
# ==========================================
if __name__ == "__main__":
    # map
    my_title = "Castle Escape"
    draw_gradient_title(my_title, font_size=70)
    draw_house_plan()
    # furniture
    draw_bed(-120, -40)
    draw_toilet(-315, -40)
    draw_cutlery(150, 70)
    draw_dining_set(20, -25)

    screen.mainloop()