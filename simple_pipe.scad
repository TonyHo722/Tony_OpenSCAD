// =========================================================
// OpenSCAD Code: 100mm Cylinder (R=5) with Central Hole (r=3)
// =========================================================

// Set fragments per rotation for smoothness (increase $fn for smoother curves)
$fn = 60;

// --- Variables ---
// Define the dimensions for easy parametric modification
cylinder_length = 100; // L = 100 mm
outer_radius = 5;      // R = 5 mm (Outer Diameter = 10 mm)
hole_radius = 3;       // r = 3 mm (Hole Diameter = 6 mm)

// The difference() function takes the first object and subtracts all subsequent objects from it.
difference() {

    // 1. Outer Cylinder (The main body)
    // 'center=true' places the object's center at [0, 0, 0] along the Z-axis,
    // making the cylinder run from Z=-50 to Z=+50.
    cylinder(
        h = cylinder_length,
        r = outer_radius,
        center = true
    );

    // 2. Inner Cylinder (The hole to be subtracted)
    // This hole runs the entire length of the main cylinder.
    cylinder(
        h = cylinder_length,
        r = hole_radius,
        center = true
    );
}