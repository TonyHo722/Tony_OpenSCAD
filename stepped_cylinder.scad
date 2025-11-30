// Stepped cylinder with threads - Generated based on specs
// Overall length: 81.5 mm
// Download threads.scad from https://dkprojects.net/openscad-threads/ and place in same folder

include <threads.scad>;  // For accurate threads; comment out if not using library

$fn = 100;  // Resolution for smooth cylinders (higher = smoother, but slower render)

union() {
    // Section 1 (left end): 3 mm long, Ø8.4 mm (no thread)
    translate([0, 0, 0])
        cylinder(h=3, r=8.4/2);

    // Section 2: 7.5 mm long, Ø10.0 mm, M10×1.25 external thread
    translate([0, 0, 3])
        metric_thread(diameter=10, pitch=1.25, length=7.5, internal=false);

    // Section 3: 54.4 mm long, Ø10.05 mm (no thread)
    translate([0, 0, 3 + 7.5])
        cylinder(h=54.4, r=10.05/2);

    // Section 4: 9.6 mm long, Ø8 mm (no thread)
    translate([0, 0, 3 + 7.5 + 54.4])
        cylinder(h=9.6, r=8/2);

    // Section 5 (right end): 7 mm long, Ø8 mm, M8×1 external thread
    translate([0, 0, 3 + 7.5 + 54.4 + 9.6])
        metric_thread(diameter=8, pitch=1, length=7, internal=false);
}

// Optional: Add a view helper (uncomment to rotate the model 90° for horizontal view)
// rotate([90, 0, 0]) children();