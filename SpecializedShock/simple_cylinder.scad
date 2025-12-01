// Simple Cylinder: 100 mm length, Ø10 mm
// Units: mm

$fn = 100;  // Facet resolution for smoothness (higher = smoother, slower render)

cylinder(h=100, r=10/2);  // h=length, r=radius

// Optional: Rotate for horizontal view (uncomment)
// rotate([90, 0, 0]) cylinder(h=100, r=5);