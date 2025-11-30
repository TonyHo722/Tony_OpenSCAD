// =========================================================
// OpenSCAD Code: 100mm 圓柱體切割成半圓柱 (Half Cylinder)
// =========================================================

// 引用螺紋庫，確保 threads.scad 檔案位於同一目錄或 OpenSCAD 庫路徑中
include <threads.scad>

// 設定曲面平滑度 (數值越大越平滑，但渲染較慢)
$fn = 60;

// --- 尺寸變數 ---
cylinder_length = 28; // 圓柱體長度
outer_radius = 21/2;      // 圓柱體半徑
handle_wdith = 14;
hat_length = 3.5;
bottom_length = 7;

inner_thread_diameter = 10;
inner_thread_pitch = 1.25;
inner_thread_length = 7.5;

hole_radius = inner_thread_diameter/2;      // 圓柱體半徑
hole_length = inner_thread_length;

// Toggle: Set to false for instant previews (plain cylinders), true for threaded STL
use_detailed_threads = true;  // Change to false for quick tests

//*** do not use center=ture in metric_thread, it will show below warning ***
//WARNING: Normalized tree is growing past 200000 elements. Aborting normalization.  
//WARNING: CSG normalization resulted in an empty tree 

module threaded_section(diam, pitch, len, z_pos) {
    if (use_detailed_threads) {
        translate([0, 0, z_pos])
            metric_thread(diameter=diam, pitch=pitch, length=len, internal=true);
            // metric_thread(diameter=diam, pitch=pitch, length=len, internal=true, center=ture);
    } else {
        // Plain cylinder approximation (fast, no helix)
        translate([0, 0, z_pos])
            cylinder(h=len, r=diam/2);
    }
}



difference() {

  union() {
    // --- Hat ---

    translate([0, 0, -cylinder_length/2 -hat_length/2])
        cylinder(
            h = hat_length,
            r = outer_radius,
            center = true
        );

    translate([0, 0, -cylinder_length/2 -hat_length/2 -bottom_length/2])
        cylinder(
            h = bottom_length,
            r = handle_wdith/2,
            center = true
        );


    // --- Handle ---
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
        // 我們需要一個足夠大的立方體來切掉圓柱體的「上半部」（Y > handle_wdith/2 的部分）。

        // 定義立方體尺寸：
        // X軸：略大於直徑 (10 + 2 = 12)
        // Y軸：略大於半徑 (5 + 1 = 6)
        // Z軸：等於圓柱體長度 (100)

        // 將立方體移動到正確的切割位置：
        // 為了讓立方體的底部邊緣精確對齊圓柱體的中心軸 (Z軸)，
        // 我們將其中心點從 [0, 0, 0] 移動到 [X_offset, Y_offset, Z_offset]。
        translate(v = [-outer_radius - 1, handle_wdith/2, -cylinder_length/2])
        {
            // 立方體從 Y=0 開始向正 Y 方向延伸，完美覆蓋圓柱體的上半部。
            cube(
                size = [outer_radius * 2 + 2, outer_radius + 1, cylinder_length]
            );
        }


        // 3. 切割用的立方體 (The Cutter/Box)
        // 我們需要一個足夠大的立方體來切掉圓柱體的「上半部」（Y < handle_wdith/2的部分）。

        // 定義立方體尺寸：
        // X軸：略大於直徑 (10 + 2 = 12)
        // Y軸：略大於半徑 (5 + 1 = 6)
        // Z軸：等於圓柱體長度 (100)

        // 將立方體移動到正確的切割位置：
        // 為了讓立方體的底部邊緣精確對齊圓柱體的中心軸 (Z軸)，
        // 我們將其中心點從 [0, 0, 0] 移動到 [X_offset, Y_offset, Z_offset]。
        translate(v = [-outer_radius - 1, -(outer_radius + 1)- (handle_wdith/2), -cylinder_length/2])
        {
            // 立方體從 Y=0 開始向正 Y 方向延伸，完美覆蓋圓柱體的上半部。
            cube(
                size = [outer_radius * 2 + 2, outer_radius + 1, cylinder_length]
            );
        }
        
    }
    
  }


  threaded_section(inner_thread_diameter, inner_thread_pitch, inner_thread_length, -cylinder_length/2 -hat_length -bottom_length);

/*  
  translate([0, 0, -cylinder_length/2 -hat_length/2 -bottom_length/2]) 
  {


  
      // 1. use hole
      cylinder(
          h = hole_length,
          r = hole_radius,
          center = true
      );

      // 2. use thread
      
      // 內螺紋切割體 (The Internal Thread Cutter)
      // metric_thread 函式來自 threads.scad 庫
      // diameter=10, pitch=1.25
      // internal=true 表示這個螺紋是「挖孔」用的螺紋形狀
      metric_thread(
          diameter = inner_thread_diameter,
          pitch = inner_thread_pitch,
          length = inner_thread_length, // 螺紋貫穿整個長度
          internal = true,         // 產生內螺紋切割體
          center = true            // 與主體圓柱體在 Z 軸上對齊
      );
      
  }
  
*/
  
}


