// Stepped Cylinder Three-View Orthographic Drawing (2D-Only for Instant Render)
// Based on your specs: Overall 81.5 mm length, sections as defined
// Units: mm; Scale: 1:1
// Save as .scad, F5/F6 in OpenSCAD for views, export DXF for editing

$fn = 50;  // Smoothness

// Section lengths and radii for calculations
sec_lengths = [3, 7.5, 54.4, 9.6, 7];
sec_diams = [8.4, 10.0, 10.05, 8.0, 8.0];
sec_radii = [for (d = sec_diams) d / 2];

// Cumulative Z positions
cum_z = [0];
for (i = [0:3]) cum_z = concat(cum_z, [cum_z[i+1] + sec_lengths[i]]);

// Front/Right View: Stepped polygon (symmetric outline with centerline)
module front_view() {
    // Centerline
    translate([0, cum_z[1]/2]) square([0.1, 81.5], center=true);

    // Stepped sides (left and right edges)
    for (side = [-1, 1]) {
        translate([side * sec_radii[0], cum_z[0]]) square([0.1, sec_lengths[0]]);
        translate([side * sec_radii[1], cum_z[1]]) square([0.1, sec_lengths[1]]);
        translate([side * sec_radii[2], cum_z[2]]) square([0.1, sec_lengths[2]]);
        translate([side * sec_radii[3], cum_z[3]]) square([0.1, sec_lengths[3]]);
        translate([side * sec_radii[4], cum_z[4]]) square([0.1, sec_lengths[4]]);
    }

    // Thread indicators (simple lines for drawing)
    translate([5.0, cum_z[1]]) {  // Sec2 thread
        for (i = [0:0.5:7.5]) translate([0, i]) square([0.1, 0.1]);
    }
    translate([-5.0, cum_z[1]]) {  // Mirror
        for (i = [0:0.5:7.5]) translate([0, i]) square([0.1, 0.1]);
    }
    translate([4.0, cum_z[4]]) {  // Sec5 thread
        for (i = [0:0.4:7]) translate([0, i]) square([0.1, 0.1]);
    }
    translate([-4.0, cum_z[4]]) {
        for (i = [0:0.4:7]) translate([0, i]) square([0.1, 0.1]);
    }
}

// Top View: Stacked circles with centerline
module top_view() {
    // Horizontal centerline
    translate([0, 0]) square([10.1, 0.1]);  // Approx full width

    // Circles for each section (overlapping)
    for (i = [0:4]) {
        translate([0, cum_z[i+1] - cum_z[i]/2]) circle(r = sec_radii[i]);
    }

    // Thread indicators on top (dashed circles)
    // Sec2: Dashed at r=5
    translate([0, cum_z[2] - cum_z[1]/2]) {
        for (a = [0:30:360]) rotate(a) translate([5, 0]) square([0.2, 0.2]);
    }
    // Sec5 similar...
}

// Simple dimension module
module dim_line(x1, y1, x2, y2, label) {
    line = [ [x1,y1], [x2,y2] ];
    polyline(line);
    // Arrows (basic)
    translate([x2, y2]) circle(r=0.1);
    translate([x1, y1]) circle(r=0.1);
    // Label
    translate( [(x1+x2)/2, (y1+y2)/2] ) text(label, size=1.5);
}

// Layout (arrange views)
translate([0, 0]) front_view();  // Front

translate([100, 0]) top_view();  // Top

translate([0, -100]) rotate(90) front_view();  // Right (rotated)

// Dimensions (examples)
dim_line(0, 0, 0, 81.5, "81.5");  // Overall
dim_line(5.025, 10.5, 5.025, 64.9, "54.4");  // Sec3

// Labels
translate([0, 85]) text("Front View");
translate([100, 85]) text("Top View");
translate([0, -185]) text("Right View");

// Title
translate([50, -110]) text("Stepped Cylinder Three-View Drawing", size=3, halign="center");