// =========================================================
// OpenSCAD Code: 兩個球體的交集部分
// =========================================================

// 設定曲面平滑度
$fn = 60;

// --- 尺寸變數 ---
ball_radius = 5;    // 球體半徑 R=5 mm
center_distance = 4; // 球心距離 D=4 mm

// 為了讓交集區域在 X 軸上置中，我們將球體 1 移到 -D/2，球體 2 移到 +D/2。
x_offset = center_distance / 2; // 4 / 2 = 2

// intersection() 函式只保留所有子物件重疊的部分
intersection() {

    // 1. 球體 A (Ball A)
    // 沿著 X 軸向左移動 2 mm
    translate(v = [-x_offset, 0, 0])
    {
        sphere(r = ball_radius);
    }

    // 2. 球體 B (Ball B)
    // 沿著 X 軸向右移動 2 mm
    translate(v = [x_offset, 0, 0])
    {
        sphere(r = ball_radius);
    }
}