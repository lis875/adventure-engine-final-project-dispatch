graph TD
    %% 定义节点样式
    classDef location fill:#e1f5fe,stroke:#0288d1,stroke-width:2px,color:#000;
    classDef item fill:#fff9c4,stroke:#fbc02d,stroke-width:2px,color:#000;
    classDef danger fill:#ffcdd2,stroke:#c62828,stroke-width:2px,color:#000;
    classDef endState fill:#e8f5e9,stroke:#388e3c,stroke-width:3px,color:#000,shape:rounded;
    classDef failState fill:#263238,stroke:#000,stroke-width:3px,color:#fff,shape:rounded;

    %% 起始点（假设从卧室开始）
    Start((开始)) --> Bedroom

    %% --- 卧室区域 ---
    subgraph BEDROOM_ZONE [卧室区域]
        Bedroom[卧室]:::location
        %% 卧室内部循环动作
        Bedroom -- 检查衣柜 --> BR_Act1[SAN -15]:::danger --> Bedroom
        Bedroom -- 检查床底 --> BR_Act2[获得: 湿日记本]:::item --> Bedroom
    end

    %% 卧室对外连接
    Bedroom -- 去门 A --> Bathroom
    Bedroom -- 去门 B --> Hall

    %% --- 浴室区域 ---
    subgraph BATHROOM_ZONE [浴室区域]
        Bathroom[浴室]:::location
        %% 浴室内部循环动作
        Bathroom -- 检查镜子 --> BA_Act1[SAN -20]:::danger --> Bathroom
        Bathroom -- 检查马桶 --> BA_Act2[获得: 生锈小钥匙]:::item --> Bathroom
    end
    %% 浴室返回
    Bathroom -- 返回 --> Bedroom

    %% --- 大厅区域 ---
    subgraph HALL_ZONE [大厅区域]
        Hall[大厅]:::location
        %% 大厅内部循环动作
        Hall -- 拉开床单 --> HA_Act1[SAN -10]:::danger --> Hall
    end
    %% 大厅对外连接
    Hall -- 去厨房 --> Kitchen

    %% --- 厨房区域 ---
    subgraph KITCHEN_ZONE [厨房区域]
        Kitchen[厨房]:::location
        %% 厨房内部循环动作
        Kitchen -- 检查冰柜 --> KI_Act1[HP -30 <br>怪物攻击]:::danger --> Kitchen
        Kitchen -- 检查台面 --> KI_Act2[获得: 沉重银钥匙]:::item --> Kitchen
    end
    
    %% 关键路径：厨房水槽 -> 返回大厅
    Kitchen -- 检查水槽 <br>(需: 生锈小钥匙) --> KI_Sink[获得线索 <br>并返回大厅]:::item --> Hall

    %% --- 结局路径 ---
    %% 只有在完成水槽任务回到大厅后，才能进行 Final Check
    Hall -- "Final Check (调查完水槽后)" --> FinalKey[获得: 沉重铁门钥匙]:::item --> EndCheck{结局判定}

    %% 判定逻辑
    EndCheck -- "使用钥匙成功 <br>(HP>0 且 SAN≥10)" --> Victory([成功逃脱]):::endState
    EndCheck -- "判定失败 <br>(HP=0 或 SAN<10)" --> Defeat([陷入疯狂 / 死亡]):::failState