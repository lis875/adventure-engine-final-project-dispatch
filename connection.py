import turtle
import time

# === 导入现有模块 ===
# 我们直接使用 scenes 里的数据，保证状态同步
from scenes import STATE, SCENES, DISPLAY_NAMES
# 我们可以复用 main.py 里的显示场景文本的函数，省去重复代码
from main import show_scene
# 导入 turtle 画图模块 (注意：导入时它会自动运行顶层的 screen 初始化代码)
import escape_turtle

# ==========================================
# 1. 坐标映射配置 (Coordinate Mapping)
# ==========================================
# 这里我们需要手动“测量”一下 escape_turtle.py 里各个房间的大致中心点坐标
# 比如 卧室原本是 draw_room(-220, -100, 170, 150)，中心大概在 (-135, -25)
# 这样无论玩家在 "bedroom_intro" 还是 "bedroom_bed"，红点都在卧室区域
ROOM_COORDS = {
    "bedroom": (-135, -25),  # 卧室中心
    "bathroom": (-270, -20), # 浴室中心
    "hall": (20, -60),         # 大厅中心
    "kitchen": (135, 80)     # 厨房中心
}

def get_coordinates(scene_id):
    """
    根据场景ID (如 'bedroom_underbed') 返回对应的 (x, y) 坐标。
    如果找不到精确匹配，就进行模糊匹配。
    """
    # 1. 判断属于哪个大区域
    if scene_id == "door_a":
        return ROOM_COORDS["bathroom"]
    # door_b 是去大厅的门，位置应视为大厅
    elif scene_id == "door_b":
        return ROOM_COORDS["hall"]
    if "bedroom" in scene_id:
        return ROOM_COORDS["bedroom"]
    elif "bathroom" in scene_id:
        return ROOM_COORDS["bathroom"]
    elif "hall" in scene_id:
        return ROOM_COORDS["hall"]
    elif "kitchen" in scene_id:
        return ROOM_COORDS["kitchen"]
    else:
        # 如果是结局画面或者未知区域，暂时不动，或者可以设一个默认位置
        return (0, 0)

# ==========================================
# 2. 玩家对象初始化 (Player Setup)
# ==========================================
def create_player_marker():
    """创建一个代表玩家的红色圆点"""
    player = turtle.Turtle()
    player.shape("circle")  # 形状设为圆点
    player.color("red")     # 颜色设为红色
    player.shapesize(0.8)   # 稍微调小一点，不要遮住太多家具
    player.penup()          # 抬笔，移动时不留痕迹
    player.speed(3)         # 设置移动速度 (1-10)，0为瞬移
    return player

# ==========================================
# 3. Modified Game Loop
# ==========================================
def run_game_with_map():
    # --- A. 初始化地图 ---
    # 调用 escape_turtle 里的函数把家具画出来
    # 注意：因为 escape_turtle.py 里的绘制代码在 if name == main 下，
    # 我们作为模块导入时不会自动执行绘制，所以需要手动调用一次。
    escape_turtle.draw_house_plan()
    escape_turtle.draw_bed(-120, -40)
    escape_turtle.draw_toilet(-315, -40)
    escape_turtle.draw_cutlery(150, 70)
    escape_turtle.draw_dining_set(20, -25)
    
    # --- B. 初始化玩家 ---
    player = create_player_marker()
    
    # 获取当前初始位置
    current_location = STATE["location"]
    start_x, start_y = get_coordinates(current_location)
    player.goto(start_x, start_y)

    print("=== 游戏开始 ===")
    print("提示：请查看弹出的 Turtle 窗口查看地图，但在本窗口输入指令。")

    # --- C. 循环逻辑 (这是 main.py game_loop 的改良版) ---
    while STATE["alive"]:
        
        # 1. 更新地图上的位置
        target_x, target_y = get_coordinates(STATE["location"])
        player.goto(target_x, target_y)

        # 2. 显示当前剧情文本 (调用 main.py 的现有功能)
        # 注意：因为 current 变量在循环里更新，这里再次获取
        current_scene_id = STATE["location"]
        show_scene(current_scene_id)
        
        # 3. 获取场景数据
        scene_data = SCENES.get(current_scene_id)
        if not scene_data:
            print("游戏结束 (场景未定义)")
            break
            
        choices = scene_data.get("choices", {})

        # 如果没有选项，说明是结局，退出循环
        if not choices:
            break

        # 4. 打印选项 (逻辑照搬 main.py，保持体验一致)
        print("\n你可以选择:")
        # 对选项key进行排序
        for key in sorted(choices.keys(), key=lambda x: int(x) if x.isdigit() else 0):
            next_scene_name = choices[key]
            # 获取友好的显示名称
            display_entry = DISPLAY_NAMES.get(next_scene_name)
            
            # 处理显示逻辑
            label = ""
            if isinstance(display_entry, dict):
                label = display_entry.get('label', next_scene_name)
            elif isinstance(display_entry, str):
                label = display_entry
            else:
                label = next_scene_name
            
            print(f"{key}. {label}")

        # 5. 获取用户输入
        user_input = input("\n> 请输入选项数字: ").strip()

        # 6. 验证并更新状态
        if user_input in choices:
            next_scene = choices[user_input]
            STATE["location"] = next_scene  # 更新全局状态
            # 循环回到开头，红点会自动根据新的 location 移动
        else:
            print("无效的选项，请重试。")

    print("\n=== 游戏结束 ===")
    print("点击 Turtle 窗口即可关闭程序。")
    escape_turtle.screen.exitonclick()

if __name__ == "__main__":
    run_game_with_map()