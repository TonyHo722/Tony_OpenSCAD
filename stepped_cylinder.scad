// Stepped cylinder with threads - Optimized for speed
// Overall length: 81.5 mm
// Download threads.scad from https://dkprojects.net/openscad-threads/ and place in same folder

include <threads.scad>;  // For accurate threads; comment out if not using library

$fn = 50;  // Reduced from 100 for ~50% faster render (increase for smoother STL)

// Toggle: Set to false for instant previews (plain cylinders), true for threaded STL
use_detailed_threads = true;  // Change to false for quick tests

module threaded_section(diam, pitch, len, z_pos) {
    if (use_detailed_threads) {
        translate([0, 0, z_pos])
            metric_thread(diameter=diam, pitch=pitch, length=len, internal=false);
    } else {
        // Plain cylinder approximation (fast, no helix)
        translate([0, 0, z_pos])
            cylinder(h=len, r=diam/2);
    }
}

union() {
    // Section 1 (left end): 3 mm, Ø8.4 mm (no thread)
    translate([0, 0, 0])
        cylinder(h=3, r=8.4/2);
    
    // Section 2: 7.5 mm, Ø10.0 mm, M10×1.25 external thread
    threaded_section(10, 1.25, 7.5, 3);
    
    // Section 3: 54.4 mm, Ø10.05 mm (no thread)
    translate([0, 0, 3 + 7.5])
        cylinder(h=54.4, r=10.05/2);
    
    // Section 4: 9.6 mm, Ø8 mm (no thread)
    translate([0, 0, 3 + 7.5 + 54.4])
        cylinder(h=9.6, r=8/2);
    
    // Section 5 (right end): 7 mm, Ø8 mm, M8×1 external thread
    threaded_section(8, 1, 7, 3 + 7.5 + 54.4 + 9.6);
}

// Optional: Rotate for horizontal view in viewer (uncomment)
// rotate([90, 0, 0]) children();