// =========================================================
// OpenSCAD Code: 100mm 圓柱體切割成半圓柱 (Half Cylinder)
// =========================================================

// 設定曲面平滑度 (數值越大越平滑)
$fn = 60;

// --- 尺寸變數 ---
cylinder_length = 100; // 圓柱體長度
outer_radius = 5;      // 圓柱體半徑

// --- 主體與切割體 ---
difference() {

    // 1. 主要圓柱體 (Main Cylinder)
    // 圓柱體長度為100，半徑為5。
    // center=true 使圓柱體中心位於 [0, 0, 0]，沿著 Z 軸延伸。
    cylinder(
        h = cylinder_length,
        r = outer_radius,
        center = true
    );


    // 2. 切割用的立方體 (The Cutter/Box)
    // 我們需要一個足夠大的立方體來切掉圓柱體的「上半部」（Y > 3 的部分）。

    // 定義立方體尺寸：
    // X軸：略大於直徑 (10 + 2 = 12)
    // Y軸：略大於半徑 (5 + 1 = 6)
    // Z軸：等於圓柱體長度 (100)

    // 將立方體移動到正確的切割位置：
    // 為了讓立方體的底部邊緣精確對齊圓柱體的中心軸 (Z軸)，
    // 我們將其中心點從 [0, 0, 0] 移動到 [X_offset, Y_offset, Z_offset]。
    translate(v = [-outer_radius - 1, 3, -cylinder_length/2])
    {
        // 立方體從 Y=0 開始向正 Y 方向延伸，完美覆蓋圓柱體的上半部。
        cube(
            size = [outer_radius * 2 + 2, outer_radius + 1, cylinder_length]
        );
    }


    // 3. 切割用的立方體 (The Cutter/Box)
    // 我們需要一個足夠大的立方體來切掉圓柱體的「上半部」（Y <-3 的部分）。

    // 定義立方體尺寸：
    // X軸：略大於直徑 (10 + 2 = 12)
    // Y軸：略大於半徑 (5 + 1 = 6)
    // Z軸：等於圓柱體長度 (100)

    // 將立方體移動到正確的切割位置：
    // 為了讓立方體的底部邊緣精確對齊圓柱體的中心軸 (Z軸)，
    // 我們將其中心點從 [0, 0, 0] 移動到 [X_offset, Y_offset, Z_offset]。
    translate(v = [-outer_radius - 1, -(outer_radius + 1)-3, -cylinder_length/2])
    {
        // 立方體從 Y=0 開始向正 Y 方向延伸，完美覆蓋圓柱體的上半部。
        cube(
            size = [outer_radius * 2 + 2, outer_radius + 1, cylinder_length]
        );
    }

}