// =========================================================
// OpenSCAD Code: 100mm 圓柱體 (R=10) 沿 X 軸
// =========================================================

// 設定曲面平滑度
$fn = 60;

// --- 尺寸變數 ---
cylinder_length = 100; // L=100 mm (將沿 X 軸)
outer_radius = 10;     // R=10 mm

// 我們將使用 rotate() 將圓柱體從 Z 軸轉向 X 軸。
// 為了確保圓柱體的起點 (X=0) 位於世界座標的原點 [0, 0, 0]，
// 我們先讓圓柱體底部中心位於原點 (預設行為)，然後再旋轉。



translate(v = [0, 0, 0])
  difference() {

    translate(v = [-outer_radius - 1, handle_wdith/2, -cylinder_length/2])
    {
        // 立方體從 Y=0 開始向正 Y 方向延伸，完美覆蓋圓柱體的上半部。
        cube(
            size = [cylinder_length, outer_radius, outer_radius]
        );
    }

    translate(v = [0, outer_radius, outer_radius])
      rotate(a = 90, v = [0, 1, 0]) // 繞 Y 軸旋轉 90 度
      {
          // cylinder() 預設沿 Z 軸，底部中心在 [0, 0, 0]。
          // 旋轉後：
          // Z 軸 (高度) --> 變為 X 軸 (長度)
          // X, Y 軸 (半徑) --> 變為 Y, Z 軸 (半徑)
          cylinder(
              h = cylinder_length,
              r = outer_radius
          );
      }

  }
