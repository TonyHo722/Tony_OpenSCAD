// =========================================================
// OpenSCAD Code: 100mm 圓柱體 (R=10) 與 M10x1.25P 內螺紋孔
// 起點定位在 [0, 0, 0]
// =========================================================

// 引用螺紋庫，假設 threads.scad 檔案可用
include <threads.scad>

// 設定曲面平滑度
$fn = 60;

// --- 尺寸變數 ---
cylinder_length = 100; // L=100 mm
outer_radius = 10;     // R=10 mm (外徑 D=20 mm)
thread_diameter = 10;  // M10 公稱直徑
thread_pitch = 1.25;   // 1.25 螺距

difference() {

    // 1. 主體圓柱體 (The Outer Body)
    // 預設情況下，cylinder(h=100, r=10) 的底部中心點位於 [0, 0, 0]，
    // Z 軸範圍是 [0, 100]。
    cylinder(
        h = cylinder_length,
        r = outer_radius
        // 不使用 center=true
    );

    // 2. 內螺紋切割體 (The Internal Thread Cutter)
    // metric_thread 函式需要手動定位，使其底部對齊 Z=0。
    // 由於 metric_thread 函式預設可能也是底部在 Z=0，
    // 但為確保與主體對齊，我們使用 translate 函式確保其起點在 Z=0。
    translate([0, 0, 0]) // 顯式將切割體底部移動到 Z=0
    {
        metric_thread(
            diameter = thread_diameter,
            pitch = thread_pitch,
            length = cylinder_length,
            internal = true,
            center = false           // 確保螺紋形狀底部在 Z=0
        );
    }
}