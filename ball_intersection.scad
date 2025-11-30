// =========================================================
// OpenSCAD Code: 保留球體 A，並挖除與球體 B 的交集部分
// =========================================================

// 設定曲面平滑度
$fn = 60;

// --- 尺寸變數 ---
ball_radius = 5;     // 球體半徑 R=5 mm
center_distance = 4; // 球心距離 D=4 mm
x_offset = center_distance / 2; // 2 mm

// difference(主體, 切割體)
difference() {

    // 1. 主體 (Primary Object): 球體 A
    // 保留這個球體，並沿 X 軸向左移動 2 mm
    translate(v = [-x_offset, 0, 0])
    {
        sphere(r = ball_radius);
    }

    // 2. 切割體 (Subtracted Object): 兩個球體的交集體積
    // 使用 intersection() 來創建切割所需的形狀
    intersection() {

        // 2a. 球體 A (用來產生交集形狀)
        translate(v = [-x_offset, 0, 0])
        {
            sphere(r = ball_radius);
        }

        // 2b. 球體 B (用來產生交集形狀)
        translate(v = [x_offset, 0, 0])
        {
            sphere(r = ball_radius);
        }
    }
}