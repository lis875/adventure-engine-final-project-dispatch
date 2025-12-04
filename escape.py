import turtle

def draw_house_plan():
    # screen
    screen = turtle.Screen()
    screen.title("The Lost House - Floor Plan")
    screen.setup(width=800, height=600)
    
    # pen
    pen = turtle.Turtle()
    pen.speed(0) # 最快速度
    pen.hideturtle()
    pen.width(3) # 线条宽度
    
    # color
    LINE_COLOR = "black"
    TEXT_COLOR = "#8B0000" # 酒红色 (DarkRed / Wine)
    BG_COLOR = "white"

    # room
    def draw_room(x, y, w, h):
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.color(LINE_COLOR)
        for _ in range(2):
            pen.forward(w)
            pen.left(90)
            pen.forward(h)
            pen.left(90)

    # room_name
    def write_label(x, y, text):
        pen.penup()
        # 计算中心位置大致坐标
        pen.goto(x, y)
        pen.color(TEXT_COLOR)
        pen.write(text, align="center", font=("Arial", 14, "bold"))

    # room_door
    def make_door(x, y, horizontal=True):
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.color("white")
        pen.width(4) # 比墙壁略宽以完全覆盖
        if horizontal:
            pen.forward(40)
        else:
            pen.left(90)
            pen.forward(40)
            pen.right(90)
        pen.width(3) # 恢复原来的宽度

    # --- 1. 绘制房间轮廓 ---
    
    # 定义房间坐标和尺寸
    # 坐标系以屏幕中心为(0,0)
    
    # 大厅 (Middle - Hall)
    # 中心位置，稍微大一点的长方形
    hall_x, hall_y = -50, -100
    hall_w, hall_h = 140, 200
    draw_room(hall_x, hall_y, hall_w, hall_h)

    # 卧室 (Left - Bedroom)
    # 在大厅左边，高度稍微矮一点
    bed_x, bed_y = -220, -100
    bed_w, bed_h = 170, 150 
    draw_room(bed_x, bed_y, bed_w, bed_h)

    # 厕所 (Left connected to Bedroom - Bathroom)
    # 连接在卧室的左侧
    bath_x, bath_y = -320, -60
    bath_w, bath_h = 100, 80
    draw_room(bath_x, bath_y, bath_w, bath_h)

    # 厨房 (Right Upper - Kitchen)
    # 在大厅右侧，偏上方
    kit_x, kit_y = 90, 20
    kit_w, kit_h = 140, 120
    draw_room(kit_x, kit_y, kit_w, kit_h)

    # --- 2. 绘制连通门 (打通墙壁) ---
    
    # 卧室 <-> 大厅 (Bedroom -> Door B -> Hall)
    # 在卧室右墙/大厅左墙开门
    make_door(-50, -60, horizontal=False)

    # 卧室 <-> 厕所 (Bedroom -> Door A -> Bathroom)
    # 在卧室左墙/厕所右墙开门
    make_door(-220, -40, horizontal=False)

    # 大厅 <-> 厨房 (Hall -> Kitchen)
    # 在大厅右墙/厨房左墙开门
    make_door(90, 50, horizontal=False)
    
    # --- 3. 标注房间名称 (酒红色) ---
    
    # 计算每个房间的中心点来写字
    write_label(bed_x + bed_w/2, bed_y + bed_h/2 - 10, "[bedroom]")
    write_label(bath_x + bath_w/2, bath_y + bath_h/2 - 10, "[bathroom]")
    write_label(hall_x + hall_w/2, hall_y + hall_h/2 - 10, "[hall]")
    write_label(kit_x + kit_w/2, kit_y + kit_h/2 - 10, "[kitchen]")

    # 保持窗口打开
    screen.mainloop()

if __name__ == "__main__":
    draw_house_plan()