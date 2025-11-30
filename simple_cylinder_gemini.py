import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

# Dimensions
LENGTH = 100
RADIUS = 5
DIAMETER = 2 * RADIUS

# Spacing and layout
SPACING = 20 # Space between views
X_FV_START = 0
Y_FV_START = 0

# --- Setup Figure and Plot ---
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_aspect('equal', adjustable='box')
ax.set_title(r'Three-View Orthographic Drawing of a Cylinder' + '\n' + r'$L=100\mathrm{ mm}, R=5\mathrm{ mm}$ (Circle as Front View)')

# --- 1. Front View (FV) - Now the Circle ---
# FV shows the circular end face (Diameter 10)
X_FV_CENTER = X_FV_START + RADIUS
Y_FV_CENTER = Y_FV_START + RADIUS
circ_fv = Circle((X_FV_CENTER, Y_FV_CENTER), RADIUS, fill=False, edgecolor='black', linewidth=1.5)
ax.add_patch(circ_fv)
ax.text(X_FV_CENTER, Y_FV_START - 5, 'FRONT VIEW', ha='center', va='top')

# Centerlines for FV (crosshairs)
ax.plot([X_FV_CENTER - RADIUS, X_FV_CENTER + RADIUS], [Y_FV_CENTER, Y_FV_CENTER], 'k-.', linewidth=0.8)
ax.plot([X_FV_CENTER, X_FV_CENTER], [Y_FV_CENTER - RADIUS, Y_FV_CENTER + RADIUS], 'k-.', linewidth=0.8)

# --- 2. Top View (TV) - Now the rectangle showing length and diameter ---
# TV shows Length (100) and Diameter (10). Aligned above FV.
# The 'height' of the TV (diameter) is aligned with the FV diameter.
# The 'length' of the TV extends horizontally.
Y_TV_START = Y_FV_START + DIAMETER + SPACING
rect_tv = Rectangle((X_FV_CENTER - RADIUS, Y_TV_START), LENGTH, DIAMETER, fill=False, edgecolor='black', linewidth=1.5)
ax.add_patch(rect_tv)
ax.text(X_FV_CENTER - RADIUS + LENGTH / 2, Y_TV_START + DIAMETER + 5, 'TOP VIEW', ha='center', va='bottom')

# Centerline for TV (along length)
ax.plot([X_FV_CENTER - RADIUS, X_FV_CENTER - RADIUS + LENGTH], [Y_TV_START + DIAMETER / 2, Y_TV_START + DIAMETER / 2], 'k-.', linewidth=0.8)

# --- 3. Right Side View (RSV) - Now the rectangle showing length and diameter ---
# RSV shows Length (100) and Diameter (10). Aligned to the right of FV.
X_RSV_START = X_FV_START + DIAMETER + SPACING
rect_rsv = Rectangle((X_RSV_START, Y_FV_START), LENGTH, DIAMETER, fill=False, edgecolor='black', linewidth=1.5)
ax.add_patch(rect_rsv)
ax.text(X_RSV_START + LENGTH / 2, Y_FV_START - 5, 'RIGHT SIDE VIEW', ha='center', va='top')

# Centerline for RSV (along length)
ax.plot([X_RSV_START, X_RSV_START + LENGTH], [Y_FV_START + DIAMETER / 2, Y_FV_START + DIAMETER / 2], 'k-.', linewidth=0.8)


# --- Projection Lines (Visual Aid) ---
# From FV to TV for diameter alignment
ax.plot([X_FV_CENTER - RADIUS, X_FV_CENTER - RADIUS], [Y_FV_START + DIAMETER, Y_TV_START], 'k:', linewidth=0.5)
ax.plot([X_FV_CENTER + RADIUS, X_FV_CENTER + RADIUS], [Y_FV_START + DIAMETER, Y_TV_START], 'k:', linewidth=0.5)

# From FV to RSV for height alignment (diameter)
ax.plot([X_FV_START + DIAMETER, X_RSV_START], [Y_FV_START, Y_FV_START], 'k:', linewidth=0.5)
ax.plot([X_FV_START + DIAMETER, X_RSV_START], [Y_FV_START + DIAMETER, Y_FV_START + DIAMETER], 'k:', linewidth=0.5)

# --- Add basic dimensions for clarity ---
# Diameter dimension (from FV)
ax.plot([X_FV_CENTER + RADIUS + 5, X_FV_CENTER + RADIUS + 5], [Y_FV_CENTER - RADIUS, Y_FV_CENTER + RADIUS], 'k-', linewidth=0.8)
ax.text(X_FV_CENTER + RADIUS + 7, Y_FV_CENTER, 'Dia: 10 mm', ha='left', va='center', fontsize=10, rotation=90)

# Length dimension (from TV)
ax.plot([X_FV_CENTER - RADIUS, X_FV_CENTER - RADIUS + LENGTH], [Y_TV_START + DIAMETER + 10, Y_TV_START + DIAMETER + 10], 'k-', linewidth=0.8)
ax.text(X_FV_CENTER - RADIUS + LENGTH / 2, Y_TV_START + DIAMETER + 15, 'Length: 100 mm', ha='center', va='bottom', fontsize=10)


# --- Set Limits and remove axes ticks/labels ---
X_MAX = X_RSV_START + LENGTH + 10
Y_MIN = Y_FV_START - 20
Y_MAX = Y_TV_START + DIAMETER + 25 # Adjusted for TV dimension

ax.set_xlim(X_FV_START - 10, X_MAX)
ax.set_ylim(Y_MIN, Y_MAX)
ax.axis('off') # Hide axes

# --- Save to PNG ---
output_filename = 'cylinder_three_view_drawing_circle_front.png'
plt.savefig(output_filename, bbox_inches='tight')
print(f"Drawing saved as {output_filename}")