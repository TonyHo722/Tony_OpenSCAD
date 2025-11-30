// Simple Cylinder Three-View Orthographic Drawing (2D-Only for Instant Render)
// 100 mm length, Ø10 mm diameter
// Units: mm; Scale: 1:1
// Save as .scad, F5/F6 in OpenSCAD, export DXF for editing

$fn = 50;  // Smoothness for circles

// Front/Right View: Rectangle with centerline
module front_view() {
    // Outline rectangle (100 mm high, 10 mm wide)
    translate([-5, 0]) square([10, 100]);
    
    // Centerline
    translate([0, 0]) square([0.1, 100]);
}

// Top View: Circle with centerline
module top_view() {
    // Circle Ø10 mm
    circle(r=5);
    
    // Horizontal centerline
    translate([0, 0]) square([10, 0.1]);
}

// Simple dimension line/arrow (using hull for line + triangles for arrows)
module dim_line(x1, y1, x2, y2, label) {
    // Line
    hull() {
        translate([x1, y1]) circle(r=0.05);
        translate([x2, y2]) circle(r=0.05);
    }
    
    // Arrowheads (basic triangles)
    angle = atan2(y2 - y1, x2 - x1);
    arrow_len = 0.5;
    
    // End arrow
    translate([x2, y2]) rotate(angle) polygon([[0,0], [-arrow_len, -0.2], [-arrow_len, 0.2]]);
    
    // Start arrow (reversed)
    translate([x1, y1]) rotate(angle + 180) polygon([[0,0], [-arrow_len, -0.2], [-arrow_len, 0.2]]);
    
    // Label midway
    translate([(x1 + x2)/2, (y1 + y2)/2 - 1]) text(label, size=2, halign="center");
}

// Layout: Arrange views (A4-ish: 200x150 mm sheet)
translate([20, 20]) front_view();  // Front view

translate([120, 20]) top_view();   // Top view

translate([20, -100]) rotate([0,0,90]) front_view();  // Right view (rotated 90° for side; same as front)

// Dimensions (examples)
translate([20, 20]) {  // Relative to front
    dim_line(0, -5, 0, 105, "100");  // Overall length
    dim_line(-7.5, 50, 7.5, 50, "Ø10");  // Diameter
}

translate([120, 20]) {  // Relative to top
    dim_line(-7.5, 0, 7.5, 0, "Ø10");  // Diameter
}

// Labels
translate([20, 115]) text("Front View", size=3);
translate([120, 115]) text("Top View", size=3);
translate([20, -195]) text("Right View", size=3);

// Title
translate([100, -210]) text("Simple Cylinder (100 mm L, Ø10 mm) - Orthographic Views (1:1 Scale)", size=3, halign="center");

// Optional sheet border
%translate([0, 0]) square([200, 250]);