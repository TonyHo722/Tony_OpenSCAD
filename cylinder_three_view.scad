// Stepped cylinder three-view drawing
// Based on stepped_cylinder.scad
// Download threads.scad from https://dkprojects.net/openscad-threads/ if using threads

include <threads.scad>;  // Comment out if not using library

$fn = 100;  // Resolution

// Original 3D model module (from stepped_cylinder.scad)
module stepped_cylinder() {
    union() {
        // Section 1: 3 mm, Ø8.4 mm
        translate([0, 0, 0])
            cylinder(h=3, r=8.4/2);

        // Section 2: 7.5 mm, Ø10.0 mm, M10×1.25 thread
        translate([0, 0, 3])
            metric_thread(diameter=10, pitch=1.25, length=7.5, internal=false);

        // Section 3: 54.4 mm, Ø10.05 mm
        translate([0, 0, 3 + 7.5])
            cylinder(h=54.4, r=10.05/2);

        // Section 4: 9.6 mm, Ø8 mm
        translate([0, 0, 3 + 7.5 + 54.4])
            cylinder(h=9.6, r=8/2);

        // Section 5: 7 mm, Ø8 mm, M8×1 thread
        translate([0, 0, 3 + 7.5 + 54.4 + 9.6])
            metric_thread(diameter=8, pitch=1, length=7, internal=false);
    }
}

// Generate projections for each view
front_view = projection(cut=false) stepped_cylinder();  // Front: along Z (shows steps in profile)

top_view = projection(cut=false)
    rotate([90, 0, 0])  // Rotate for top-down view
    stepped_cylinder();

right_view = projection(cut=false)
    rotate([0, -90, 0])  // Rotate for right-side view (along X)
    stepped_cylinder();

// Arrange views on a 2D sheet (scale: 1 unit = 1 mm)
// Front at bottom-left, top to the right, right below front
translate([0, 0, 0]) front_view;  // Front view

translate([100, 0, 0]) top_view;  // Top view (offset 100 mm right; adjust as needed)

translate([0, -100, 0]) right_view;  // Right view (offset 100 mm down)

// Optional: Add simple labels (text is 2D, so it works in projection)
translate([0, 5, 0]) text("Front View", size=4);
translate([100, 5, 0]) text("Top View", size=4);
translate([0, -95, 0]) text("Right View", size=4);

// Optional: Draw a title block or grid (uncomment and customize)
// %square(200, 150);  // Background sheet (commented; % makes it non-exported)