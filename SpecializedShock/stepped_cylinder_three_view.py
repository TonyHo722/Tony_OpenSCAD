import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

# Stepped Cylinder Dimensions (mm)
sections = [
    {'len': 3, 'dia': 8.4},    # Section 1
    {'len': 7.5, 'dia': 10.0}, # Section 2 (threaded)
    {'len': 54.4, 'dia': 10.05}, # Section 3
    {'len': 9.6, 'dia': 8.0},  # Section 4
    {'len': 7, 'dia': 8.0}     # Section 5 (threaded)
]
OVERALL_LEN = sum(s['len'] for s in sections)
RADI = [s['dia']/2 for s in sections]

# Cumulative lengths for positioning
cum_len = [0]
for s in sections:
    cum_len.append(cum_len[-1] + s['len'])

# Layout params
SPACING = 25
SCALE = 1  # 1:1 mm scale

# --- Setup ---
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_aspect('equal')
ax.set_title('Three-View Orthographic Drawing: Stepped Cylinder\nOverall L=81.5 mm', fontsize=12)

# --- Front/Right View: Stepped Longitudinal Profile (Vertical) ---
# Left edge and right edge polygons for stepped outline
left_x = [0] * len(cum_len)
right_x = [r * SCALE for r in RADI] + [RADI[-1] * SCALE]
y_vals = [c * SCALE for c in cum_len]
front_poly_left = list(zip(left_x, y_vals))
front_poly_right = list(zip(right_x, y_vals[::-1]))
ax.plot([p[0] for p in front_poly_left], [p[1] for p in front_poly_left], 'k-', lw=1.5)
ax.plot([p[0] for p in front_poly_right], [p[1] for p in front_poly_right], 'k-', lw=1.5)
ax.fill_betweenx(y_vals, left_x, right_x, color='lightgray', alpha=0.3, hatch='///')  # Solid hatching

# Centerline
ax.plot([0, 0], [0, OVERALL_LEN * SCALE], 'k--', lw=0.8)
ax.text(OVERALL_LEN * SCALE / 2, OVERALL_LEN * SCALE + 5, 'FRONT / RIGHT VIEW', ha='center', va='bottom', fontsize=11, fontweight='bold')

# --- Top View: Concentric Circles (Horizontal) ---
x_top_start = OVERALL_LEN * SCALE + SPACING
for i, (r, cl) in enumerate(zip(RADI, cum_len)):
    center_x = x_top_start + (cum_len[i+1] - cum_len[i]) * SCALE / 2
    circ = Circle((center_x, 0), r * SCALE, fill=False, edgecolor='black', lw=1.5)
    ax.add_patch(circ)
    # Hatching for solid (approximate with fill)
    circ_fill = Circle((center_x, 0), r * SCALE, color='lightgray', alpha=0.3, hatch='///')
    ax.add_patch(circ_fill)

# Top centerline
ax.plot([x_top_start, x_top_start + OVERALL_LEN * SCALE], [0, 0], 'k--', lw=0.8)
ax.text(x_top_start + OVERALL_LEN * SCALE / 2, -10, 'TOP VIEW', ha='center', va='top', fontsize=11, fontweight='bold')

# --- Dimensions ---
# Overall length (Front) - horizontal arrow
ax.annotate('', xy=(0, OVERALL_LEN * SCALE + 5), xytext=(OVERALL_LEN * SCALE, OVERALL_LEN * SCALE + 5),
            arrowprops=dict(arrowstyle='<->', lw=0.8))
ax.text(OVERALL_LEN * SCALE / 2, OVERALL_LEN * SCALE + 10, '81.5 mm', ha='center', fontsize=10)

# Sample section dia (e.g., Sec3 max) - vertical arrow, rotate text only
max_r = max(RADI)
ax.plot([max_r * SCALE + 2, max_r * SCALE + 2], [cum_len[2] * SCALE, cum_len[3] * SCALE], 'k-', lw=0.8)
ax.text(max_r * SCALE + 7, (cum_len[2] + cum_len[3]) * SCALE / 2, f'Ø{max(RADI)*2:.2f} mm', ha='left', va='center', fontsize=10, rotation=90)

# --- Limits & Style ---
x_max = x_top_start + OVERALL_LEN * SCALE + 20
y_min = -30
y_max = OVERALL_LEN * SCALE + 30
ax.set_xlim(-10, x_max)
ax.set_ylim(y_min, y_max)
ax.axis('off')

# Save & Show
plt.savefig('stepped_cylinder_three_view.png', bbox_inches='tight', dpi=150)
plt.show()  # Optional preview
print("Generated stepped_cylinder_three_view.png")