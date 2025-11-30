// =========================================================
// OpenSCAD Code: 100mm 圓柱體 (R=10) 與 M10x1.25P 內螺紋孔
// 依賴於外部函式庫：threads.scad
// =========================================================

// 引用螺紋庫，確保 threads.scad 檔案位於同一目錄或 OpenSCAD 庫路徑中
include <threads.scad>

// 設定曲面平滑度 (數值越大越平滑，但渲染較慢)
$fn = 60;

// --- 尺寸變數 ---
cylinder_length = 100; // 圓柱體長度 L=100 mm
outer_radius = 10;     // 圓柱體外徑 R=10 mm (D=20 mm)

// 內螺紋規格
// 螺紋公稱直徑 (Nominal Diameter) M10 = 10 mm
thread_diameter = 10;
// 螺距 (Pitch) M10x1.25P = 1.25 mm
thread_pitch = 1.25;

// M10 螺紋的孔徑 (Minor Diameter) 約為 8.75 mm，但 OpenSCAD 庫會自動處理
// 為了確保螺紋能夠正確切割，我們讓螺紋的 h 等於圓柱體長度，且置中。
// 這裡將所有物件都設定為 center=true，使其在 Z 軸上從 Z=-50 延伸到 Z=+50。

difference() {

    // 1. 主體圓柱體 (The Outer Body)
    cylinder(
        h = cylinder_length,
        r = outer_radius,
        center = true
    );

    // 2. 內螺紋切割體 (The Internal Thread Cutter)
    // metric_thread 函式來自 threads.scad 庫
    // diameter=10, pitch=1.25
    // internal=true 表示這個螺紋是「挖孔」用的螺紋形狀
    metric_thread(
        diameter = thread_diameter,
        pitch = thread_pitch,
        length = cylinder_length, // 螺紋貫穿整個長度
        internal = true,         // 產生內螺紋切割體
        center = true            // 與主體圓柱體在 Z 軸上對齊
    );
}

// 備註：在 OpenSCAD 渲染精確螺紋（F6）時，由於幾何複雜度，可能需要較長時間。
// 如果不需要精確螺紋形狀，而只是想畫一個帶孔的圓柱體：
/*
// 備用：僅繪製鑽孔 (Drill Hole)
difference() {
    cylinder(h = cylinder_length, r = outer_radius, center = true);
    // M10x1.25 的鑽孔直徑約為 8.75mm (10 - 1.25 = 8.75)
    cylinder(h = cylinder_length, d = 8.75, center = true);
}
*/