import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Arc
import numpy as np

# --- Stepped Cylinder Dimensions (Analyzed from stepped_cylinder.scad) ---
# Note: Minor Diameter approximations are used for standard drafting convention
# based on the pitch (Pitch=1.25 -> Minor D=8.475; Pitch=1.0 -> Minor D=6.78).
sections_data = [
    # (Length, Major Diameter, Minor Diameter, Start Z, Threaded, Thread Label)
    (3.0, 8.40, 8.40, 0.0, False, None),           # Section 1 (Plain - Left End)
    (7.5, 10.00, 8.475, 3.0, True, 'M10x1.25'),    # Section 2
    (54.4, 10.05, 10.05, 10.5, False, None),       # Section 3
    (9.6, 8.00, 8.00, 64.9, False, None),          # Section 4
    (7.0, 8.00, 6.78, 74.5, True, 'M8x1.0')        # Section 5 (M8 Thread - Right End)
]

TOTAL_LENGTH = 81.5
MAX_DIAMETER = 10.05
MAX_RADIUS = MAX_DIAMETER / 2

# Plotting constants
SPACING = 15
PADDING = 5
X0 = PADDING
Y0 = PADDING
DIM_OFFSET = 10
TEXT_OFFSET = 3

# --- Setup Figure and Plot ---
fig, ax = plt.subplots(figsize=(15, 8))
ax.set_aspect('equal', adjustable='box')
ax.set_title(r'Reoriented Three-View Drawing with Thread Callouts' + '\n' + r'Overall $L=81.5\mathrm{ mm}, D_{\mathrm{max}}=10.05\mathrm{ mm}$')

# --- 1. New Front View (FV) - Circular End View (Left End) ---
# This view is placed in the standard FV position (bottom-left)
X_FV_CENTER = X0 + MAX_RADIUS
Y_FV_CENTER = Y0 + MAX_RADIUS
LEFT_END_D = sections_data[0][1] # 8.4 mm

# Draw circles for all steps. Outermost (8.4mm) is solid, others hidden.
all_diameters = sorted(list(set([s[1] for s in sections_data])), reverse=True)
for D in all_diameters:
    R = D / 2
    if D == LEFT_END_D:
        style = {'linestyle': '-', 'linewidth': 1.5} # Visible (Solid)
    else:
        style = {'linestyle': '--', 'linewidth': 1.0} # Hidden (Dashed)

    circ_fv = Circle((X_FV_CENTER, Y_FV_CENTER), R, fill=False, edgecolor='black', **style)
    ax.add_patch(circ_fv)

# Centerlines for FV (crosshairs)
ax.plot([X_FV_CENTER - MAX_RADIUS, X_FV_CENTER + MAX_RADIUS], [Y_FV_CENTER, Y_FV_CENTER], 'k-.', linewidth=0.8)
ax.plot([X_FV_CENTER, X_FV_CENTER], [Y_FV_CENTER - MAX_RADIUS, Y_FV_CENTER + MAX_RADIUS], 'k-.', linewidth=0.8)

ax.text(X_FV_CENTER, Y0 - 5, 'FRONT VIEW ($\emptyset 8.4\mathrm{ mm}$)', ha='center', va='top')


# --- 2. New Right Side View (RSV) - Profile (Horizontal) ---
# This view is placed in the standard RSV position (bottom-right)
X_RSV_START = X0 + MAX_DIAMETER + SPACING
Y_RSV_CENTER = Y_FV_CENTER
Y_TOP_PROFILE = Y_RSV_CENTER + MAX_RADIUS

# Centerline for RSV
ax.plot([X_RSV_START, X_RSV_START + TOTAL_LENGTH], [Y_RSV_CENTER, Y_RSV_CENTER], 'k-.', linewidth=0.8)
ax.text(X_RSV_START + TOTAL_LENGTH / 2, Y0 - 5, 'RIGHT SIDE VIEW (Profile)', ha='center', va='top')

# Draw profile segments
for i, data in enumerate(sections_data):
    length, d_major, d_minor, start_z, is_threaded, thread_label = data
    r_major = d_major / 2
    r_minor = d_minor / 2
    end_z = start_z + length

    X_start = X_RSV_START + start_z
    X_end = X_RSV_START + end_z

    # Major Diameter (Profile Outline - Thick Solid)
    ax.plot([X_start, X_end], [Y_RSV_CENTER + r_major, Y_RSV_CENTER + r_major], 'k-', linewidth=1.5)
    ax.plot([X_start, X_end], [Y_RSV_CENTER - r_major, Y_RSV_CENTER - r_major], 'k-', linewidth=1.5)

    # Step Edges (Vertical Lines)
    if i > 0:
        prev_r_major = sections_data[i-1][1] / 2
        ax.plot([X_start, X_start], [Y_RSV_CENTER - prev_r_major, Y_RSV_CENTER - r_major], 'k-', linewidth=1.5)
        ax.plot([X_start, X_start], [Y_RSV_CENTER + prev_r_major, Y_RSV_CENTER + r_major], 'k-', linewidth=1.5)

    # Thread Convention (Minor Diameter and Termination)
    if is_threaded:
        # Minor Diameter (Thin Solid Line)
        ax.plot([X_start, X_end], [Y_RSV_CENTER + r_minor, Y_RSV_CENTER + r_minor], 'k-', linewidth=0.5)
        ax.plot([X_start, X_end], [Y_RSV_CENTER - r_minor, Y_RSV_CENTER - r_minor], 'k-', linewidth=0.5)

        # Thread Termination (Thin Vertical Line)
        termination_z = end_z - length * 0.1
        X_term = X_RSV_START + termination_z
        ax.plot([X_term, X_term], [Y_RSV_CENTER - r_major, Y_RSV_CENTER + r_major], 'k-', linewidth=0.5)

        # --- ADD THREAD CALLOUT AND DIMENSION ---
        # Stagger callouts slightly
        dim_y = Y_TOP_PROFILE + DIM_OFFSET * (1 + i/4)

        # Extension lines
        ax.plot([X_start, X_start], [Y_TOP_PROFILE, dim_y], 'k-', linewidth=0.5)
        ax.plot([X_end, X_end], [Y_TOP_PROFILE, dim_y], 'k-', linewidth=0.5)

        # Dimension line (with arrows, for simplicity using plain line here)
        ax.plot([X_start, X_end], [dim_y, dim_y], 'k-', linewidth=0.8)

        # Dimension text (Thread Callout)
        ax.text(X_start + length / 2, dim_y + TEXT_OFFSET, thread_label, ha='center', va='bottom', fontsize=10, fontweight='bold')

        # Total Length dimension (placed below the profile)
        if i == len(sections_data) - 1:
            dim_y_total = Y_RSV_CENTER - MAX_RADIUS - DIM_OFFSET
            ax.plot([X_RSV_START, X_RSV_START], [Y_RSV_CENTER - MAX_RADIUS, dim_y_total], 'k-', linewidth=0.5)
            ax.plot([X_RSV_START + TOTAL_LENGTH, X_RSV_START + TOTAL_LENGTH], [Y_RSV_CENTER - MAX_RADIUS, dim_y_total], 'k-', linewidth=0.5)
            ax.plot([X_RSV_START, X_RSV_START + TOTAL_LENGTH], [dim_y_total, dim_y_total], 'k-', linewidth=0.8)
            ax.text(X_RSV_START + TOTAL_LENGTH / 2, dim_y_total - TEXT_OFFSET, f'{TOTAL_LENGTH}', ha='center', va='top', fontsize=10)


# End caps (Vertical lines at start/end of the part)
ax.plot([X_RSV_START, X_RSV_START], [Y_RSV_CENTER - sections_data[0][1]/2, Y_RSV_CENTER + sections_data[0][1]/2], 'k-', linewidth=1.5)
ax.plot([X_RSV_START + TOTAL_LENGTH, X_RSV_START + TOTAL_LENGTH], [Y_RSV_CENTER - sections_data[-1][1]/2, Y_RSV_CENTER + sections_data[-1][1]/2], 'k-', linewidth=1.5)


# --- 3. New Top View (TV) - Profile (Vertical) ---
# This view is placed in the standard TV position (top-left)
X_TV_CENTER = X_FV_CENTER
Y_TV_START = Y0 + MAX_DIAMETER + SPACING + DIM_OFFSET * 2

# Centerline for TV
ax.plot([X_TV_CENTER, X_TV_CENTER], [Y_TV_START, Y_TV_START + TOTAL_LENGTH], 'k-.', linewidth=0.8)
ax.text(X_TV_CENTER, Y_TV_START + TOTAL_LENGTH + 5, 'TOP VIEW (Profile)', ha='center', va='bottom')

# Draw profile segments (Z -> Y, R -> X)
for i, data in enumerate(sections_data):
    length, d_major, d_minor, start_z, is_threaded, *thread_info = data
    r_major = d_major / 2
    r_minor = d_minor / 2
    end_z = start_z + length

    Y_start = Y_TV_START + start_z
    Y_end = Y_TV_START + end_z

    # Major Diameter (Profile Outline - Thick Solid)
    ax.plot([X_TV_CENTER + r_major, X_TV_CENTER + r_major], [Y_start, Y_end], 'k-', linewidth=1.5)
    ax.plot([X_TV_CENTER - r_major, X_TV_CENTER - r_major], [Y_start, Y_end], 'k-', linewidth=1.5)

    # Step Edges (Horizontal Lines)
    if i > 0:
        prev_r_major = sections_data[i-1][1] / 2
        ax.plot([X_TV_CENTER - prev_r_major, X_TV_CENTER - r_major], [Y_start, Y_start], 'k-', linewidth=1.5)
        ax.plot([X_TV_CENTER + prev_r_major, X_TV_CENTER + r_major], [Y_start, Y_start], 'k-', linewidth=1.5)

    # Thread Convention (Minor Diameter and Termination)
    if is_threaded:
        # Minor Diameter (Thin Solid Line)
        ax.plot([X_TV_CENTER + r_minor, X_TV_CENTER + r_minor], [Y_start, Y_end], 'k-', linewidth=0.5)
        ax.plot([X_TV_CENTER - r_minor, X_TV_CENTER - r_minor], [Y_start, Y_end], 'k-', linewidth=0.5)

        # Thread Termination (Thin Horizontal Line)
        termination_z = end_z - length * 0.1
        Y_term = Y_TV_START + termination_z
        ax.plot([X_TV_CENTER - r_major, X_TV_CENTER + r_major], [Y_term, Y_term], 'k-', linewidth=0.5)

# End caps (Horizontal lines at start/end of the part)
ax.plot([X_TV_CENTER - sections_data[0][1]/2, X_TV_CENTER + sections_data[0][1]/2], [Y_TV_START, Y_TV_START], 'k-', linewidth=1.5)
ax.plot([X_TV_CENTER - sections_data[-1][1]/2, X_TV_CENTER + sections_data[-1][1]/2], [Y_TV_START + TOTAL_LENGTH, Y_TV_START + TOTAL_LENGTH], 'k-', linewidth=1.5)


# --- Set Limits and clean up plot ---
X_MAX = X_RSV_START + TOTAL_LENGTH + PADDING + 5
Y_MAX = Y_TV_START + TOTAL_LENGTH + PADDING + 15
Y_MIN = Y_RSV_CENTER - MAX_RADIUS - DIM_OFFSET * 2

ax.set_xlim(X0 - 5, X_MAX)
ax.set_ylim(Y_MIN, Y_MAX)
ax.axis('off')

plt.show() # Display the plot