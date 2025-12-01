// 參數定義（輸入弦長）
chord_length = 7 * sqrt(5);  // ≈15.652 mm
r = 21 / 2;  // 10.5 mm
d = sqrt(r * r - pow(chord_length / 2, 2));  // ≈7 mm

// 繪製圓
circle(r);

// 計算端點
half_chord = chord_length / 2;
p1 = [-half_chord, d];
p2 = [half_chord, d];

// 方法 1: polygon() - 為什麼用？精確、無厚度、適合路徑
polygon(points = [p1, p2]);  // 簡單，但零厚度（預覽中幾乎不可見）

// 方法 2: 薄 square() - 推薦給水平線，易見
translate([0, d])  // 置中在 y=d
    rotate([0, 0, 0])  // 若非水平，可旋轉
    square([chord_length, 0.01], center = true);  // 厚度 0.01 mm

// 方法 3: 自訂 polyline 模組（像 vector graphics）
module polyline(points, width = 0.01) {
    for (i = [0 : len(points) - 2]) {
        translate(points[i])
            rotate(atan2(points[i+1][1] - points[i][1], points[i+1][0] - points[i][0]))
            square([norm(points[i+1] - points[i]), width], center = false);
    }
}
polyline([p1, p2]);  // 使用：支援多點、多角度線

// 選用：擠出成 3D（讓線有高度）
linear_extrude(height = 1)
union() {
    //circle(r);
    // 選一方法：polygon 或 square
    //polygon(points = [p1, p2]);
    
    translate([0, d])  // 置中在 y=d
      rotate([0, 0, 0])  // 若非水平，可旋轉
      square([chord_length, 0.01], center = true);  // 厚度 0.01 mm

}