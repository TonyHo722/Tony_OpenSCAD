import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

# Dimensions
LENGTH = 100
RADIUS = 5
DIAMETER = 2 * RADIUS

# Spacing and layout parameters
SPACING = 20

# FV (Circle) Coordinates
X_FV_CENTER = RADIUS
Y_FV_CENTER = RADIUS
X_FV_START = X_FV_CENTER - RADIUS # 0
Y_FV_START = Y_FV_CENTER - RADIUS # 0

# TV (Vertical Rectangle 10x100) Coordinates: Aligned above FV, with 10mm width and 100mm height
Y_TV_START = Y_FV_CENTER + RADIUS + SPACING
X_TV_START = X_FV_CENTER - RADIUS

# RSV (Horizontal Rectangle 100x10) Coordinates: Aligned right of FV
X_RSV_START = X_FV_CENTER + RADIUS + SPACING
Y_RSV_START = Y_FV_CENTER - RADIUS


# --- Setup Figure and Plot ---
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_aspect('equal', adjustable='box')
ax.set_title(r'Three-View Orthographic Drawing of a Cylinder' + '\n' + r'$L=100\mathrm{ mm}, R=5\mathrm{ mm}$ (Vertical Top View)')


# --- 1. Front View (FV) - Circle ---
circ_fv = Circle((X_FV_CENTER, Y_FV_CENTER), RADIUS, fill=False, edgecolor='black', linewidth=1.5)
ax.add_patch(circ_fv)
ax.text(X_FV_CENTER, Y_FV_START - 5, 'FRONT VIEW', ha='center', va='top')

# Centerlines for FV (crosshairs)
ax.plot([X_FV_CENTER - RADIUS, X_FV_CENTER + RADIUS], [Y_FV_CENTER, Y_FV_CENTER], 'k-.', linewidth=0.8)
ax.plot([X_FV_CENTER, X_FV_CENTER], [Y_FV_CENTER - RADIUS, Y_FV_CENTER + RADIUS], 'k-.', linewidth=0.8)


# --- 2. Top View (TV) - Vertical Rectangle (Width=10, Height=100) ---
rect_tv = Rectangle((X_TV_START, Y_TV_START), DIAMETER, LENGTH, fill=False, edgecolor='black', linewidth=1.5)
ax.add_patch(rect_tv)
ax.text(X_TV_START + DIAMETER / 2, Y_TV_START + LENGTH + 5, 'TOP VIEW', ha='center', va='bottom')

# Centerline for TV (vertical length)
ax.plot([X_TV_START + DIAMETER / 2, X_TV_START + DIAMETER / 2], [Y_TV_START, Y_TV_START + LENGTH], 'k-.', linewidth=0.8)


# --- 3. Right Side View (RSV) - Horizontal Rectangle (Width=100, Height=10) ---
rect_rsv = Rectangle((X_RSV_START, Y_RSV_START), LENGTH, DIAMETER, fill=False, edgecolor='black', linewidth=1.5)
ax.add_patch(rect_rsv)
ax.text(X_RSV_START + LENGTH / 2, Y_RSV_START - 5, 'RIGHT SIDE VIEW', ha='center', va='top')

# Centerline for RSV (horizontal length)
ax.plot([X_RSV_START, X_RSV_START + LENGTH], [Y_RSV_START + DIAMETER / 2, Y_RSV_START + DIAMETER / 2], 'k-.', linewidth=0.8)


# --- Projection Lines (Visual Aid) ---
# FV to TV for diameter alignment (width alignment)
ax.plot([X_FV_START, X_FV_START], [Y_FV_START + DIAMETER, Y_TV_START], 'k:', linewidth=0.5)
ax.plot([X_FV_START + DIAMETER, X_FV_START + DIAMETER], [Y_FV_START + DIAMETER, Y_TV_START], 'k:', linewidth=0.5)

# FV to RSV for height alignment (diameter alignment)
ax.plot([X_FV_START + DIAMETER, X_RSV_START], [Y_FV_START, Y_FV_START], 'k:', linewidth=0.5)
ax.plot([X_FV_START + DIAMETER, X_RSV_START], [Y_FV_START + DIAMETER, Y_FV_START + DIAMETER], 'k:', linewidth=0.5)

# --- Add basic dimensions for clarity ---
# Diameter dimension (from FV)
ax.plot([X_FV_CENTER + RADIUS + 5, X_FV_CENTER + RADIUS + 5], [Y_FV_CENTER - RADIUS, Y_FV_CENTER + RADIUS], 'k-', linewidth=0.8)
ax.text(X_FV_CENTER + RADIUS + 7, Y_FV_CENTER, 'Dia: 10 mm', ha='left', va='center', fontsize=10, rotation=90)

# Length dimension (from RSV)
ax.plot([X_RSV_START, X_RSV_START + LENGTH], [Y_RSV_START - 10, Y_RSV_START - 10], 'k-', linewidth=0.8)
ax.text(X_RSV_START + LENGTH / 2, Y_RSV_START - 15, 'Length: 100 mm', ha='center', va='top', fontsize=10)


# --- Set Limits and clean up plot ---
X_MAX = X_RSV_START + LENGTH + 10
Y_MIN = Y_FV_START - 20
Y_MAX = Y_TV_START + LENGTH + 10

ax.set_xlim(X_FV_START - 10, X_MAX)
ax.set_ylim(Y_MIN, Y_MAX)
ax.axis('off') # Hide axes

# --- Save to PNG ---
output_filename = 'cylinder_three_view_drawing_vertical_top_view.png'
plt.savefig(output_filename, bbox_inches='tight')