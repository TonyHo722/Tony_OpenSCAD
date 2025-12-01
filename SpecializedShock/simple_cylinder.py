import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

# Dimensions
LENGTH = 100
RADIUS = 5
DIAMETER = 2 * RADIUS

# Spacing and layout
SPACING = 20  # Space between views
X_FV_START = 0
Y_FV_START = 0

# --- Setup Figure and Plot ---
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_aspect('equal', adjustable='box')
ax.set_title(r'Three-View Orthographic Drawing of a Cylinder (Improved)' + '\n' + r'$L=100\mathrm{ mm}, R=5\mathrm{ mm}$')

# --- 1. Front View (FV): Now showing circular end face (Circle) ---
# FV: Circular profile (end view)
X_FV_CENTER = X_FV_START + RADIUS
Y_FV_CENTER = Y_FV_START + RADIUS
circ_fv = Circle((X_FV_CENTER, Y_FV_CENTER), RADIUS, fill=False, edgecolor='black', linewidth=1.5)
ax.add_patch(circ_fv)
ax.text(X_FV_CENTER, Y_FV_CENTER - RADIUS - 5, 'FRONT VIEW', ha='center', va='top')
# Centerlines for FV (crosshairs)
ax.plot([X_FV_CENTER - RADIUS, X_FV_CENTER + RADIUS], [Y_FV_CENTER, Y_FV_CENTER], 'k-.', linewidth=0.8)
ax.plot([X_FV_CENTER, X_FV_CENTER], [Y_FV_CENTER - RADIUS, Y_FV_CENTER + RADIUS], 'k-.', linewidth=0.8)

# --- 2. Top View (TV): Side profile (Rectangle, length horizontal) ---
# TV: Length horizontal, diameter vertical, aligned above FV.
Y_TV_START = Y_FV_START + DIAMETER + SPACING
rect_tv = Rectangle((X_FV_START, Y_TV_START), LENGTH, DIAMETER, fill=False, edgecolor='black', linewidth=1.5)
ax.add_patch(rect_tv)
ax.text(X_FV_START + LENGTH / 2, Y_TV_START + DIAMETER + 5, 'TOP VIEW', ha='center', va='bottom')
# Centerline for TV (along length)
ax.plot([X_FV_START, X_FV_START + LENGTH], [Y_TV_START + DIAMETER / 2, Y_TV_START + DIAMETER / 2], 'k-.', linewidth=0.8)

# --- 3. Right Side View (RSV): Side profile (Rectangle, length vertical) ---
# RSV: Length vertical, diameter horizontal, aligned to the right of FV.
X_RSV_START = X_FV_START + DIAMETER + SPACING
Y_RSV_START = Y_FV_START
rect_rsv = Rectangle((X_RSV_START, Y_RSV_START), DIAMETER, LENGTH, fill=False, edgecolor='black', linewidth=1.5)
ax.add_patch(rect_rsv)
ax.text(X_RSV_START + DIAMETER / 2, Y_RSV_START - 5, 'RIGHT SIDE VIEW', ha='center', va='top')
# Centerline for RSV (along length)
ax.plot([X_RSV_START + DIAMETER / 2, X_RSV_START + DIAMETER / 2], [Y_RSV_START, Y_RSV_START + LENGTH], 'k-.', linewidth=0.8)

# --- Add basic dimensions for clarity (using plain text) ---
# Diameter dimension (from FV)
ax.plot([X_FV_CENTER + RADIUS + 5, X_FV_CENTER + RADIUS + 5], [Y_FV_CENTER - RADIUS, Y_FV_CENTER + RADIUS], 'k-', linewidth=0.8)
ax.text(X_FV_CENTER + RADIUS + 7, Y_FV_CENTER, 'Dia: 10 mm', ha='left', va='center', fontsize=10, rotation=90)

# Length dimension (from TV)
ax.plot([X_FV_START, X_FV_START + LENGTH], [Y_TV_START - 10, Y_TV_START - 10], 'k-', linewidth=0.8)
ax.text(X_FV_START + LENGTH / 2, Y_TV_START - 15, 'Length: 100 mm', ha='center', va='top', fontsize=10)

# --- Set Limits and remove axes ticks/labels ---
X_MAX = X_RSV_START + DIAMETER + 30
Y_MIN = Y_FV_START - 20
Y_MAX = Y_TV_START + DIAMETER + 10
ax.set_xlim(X_FV_START - 10, X_MAX)
ax.set_ylim(Y_MIN, Y_MAX)
ax.axis('off')  # Hide axes

# --- Save to PNG ---
output_filename = 'improved_cylinder_three_view_drawing.png'
plt.savefig(output_filename, bbox_inches='tight', dpi=150)
plt.show()  # Optional: Display on screen
print(f"Improved PNG saved as '{output_filename}'")