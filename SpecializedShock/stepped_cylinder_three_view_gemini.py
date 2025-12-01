import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

# --- Stepped Cylinder Dimensions (Analyzed from stepped_cylinder.scad) ---
# Sections: (Length, Major Diameter, Minor Diameter, Start Z, Threaded, Thread Label)
sections_data = [
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
SLASH_PITCH = 3.0 # Spacing between slash lines in mm

# --- Function to draw slash lines for thread convention ---
def draw_slash_lines(ax, start_z, length, radius, center_y, x_offset, orientation='horizontal'):
    """Draws multiple slash lines across the threaded section."""
    num_slashes = int(length / SLASH_PITCH)
    
    if orientation == 'horizontal':
        # Diagonal lines
        for i in range(num_slashes + 1):
            z_pos = start_z + i * SLASH_PITCH
            if z_pos > start_z + length:
                z_pos = start_z + length
            
            x_pos = x_offset + z_pos
            ax.plot([x_pos - r_major, x_pos + r_major], [center_y - r_major, center_y + r_major], 'k-', linewidth=0.5, alpha=0.7)


# --- Setup Figure and Plot ---
fig, ax = plt.subplots(figsize=(15, 10)) # Increased height for new dimensions
ax.set_aspect('equal', adjustable='box')
ax.set_title(r'Complete Dimensioned Drawing of Stepped Threaded Cylinder')

# --- 1. New Front View (FV) - Circular End View (Left End) ---
X_FV_CENTER = X0 + MAX_RADIUS
Y_FV_CENTER = Y0 + MAX_RADIUS
LEFT_END_D = sections_data[0][1] 

all_diameters = sorted(list(set([s[1] for s in sections_data])), reverse=True)
for D in all_diameters:
    R = D / 2
    style = {'linestyle': '-', 'linewidth': 1.5} if D == LEFT_END_D else {'linestyle': '--', 'linewidth': 1.0}
    circ_fv = Circle((X_FV_CENTER, Y_FV_CENTER), R, fill=False, edgecolor='black', **style)
    ax.add_patch(circ_fv)

# Centerlines for FV (crosshairs)
ax.plot([X_FV_CENTER - MAX_RADIUS, X_FV_CENTER + MAX_RADIUS], [Y_FV_CENTER, Y_FV_CENTER], 'k-.', linewidth=0.8)
ax.plot([X_FV_CENTER, X_FV_CENTER], [Y_FV_CENTER - MAX_RADIUS, Y_FV_CENTER + MAX_RADIUS], 'k-.', linewidth=0.8)
ax.text(X_FV_CENTER, Y0 - 5, 'FRONT VIEW ($\emptyset 8.40\mathrm{ mm}$)', ha='center', va='top')


# --- 2. New Right Side View (RSV) - Profile (Horizontal) ---
X_RSV_START = X0 + MAX_DIAMETER + SPACING
Y_RSV_CENTER = Y_FV_CENTER
Y_TOP_PROFILE = Y_RSV_CENTER + MAX_RADIUS
Y_BOT_PROFILE = Y_RSV_CENTER - MAX_RADIUS

# Centerline for RSV
ax.plot([X_RSV_START, X_RSV_START + TOTAL_LENGTH], [Y_RSV_CENTER, Y_RSV_CENTER], 'k-.', linewidth=0.8)
ax.text(X_RSV_START + TOTAL_LENGTH / 2, Y0 - 5, 'RIGHT SIDE VIEW (Profile)', ha='center', va='top')

# --- Diameter Dimensioning on the Left of RSV ---
X_DIM_OFFSET_1 = X_RSV_START - 15  # Ø10.05
X_DIM_OFFSET_2 = X_RSV_START - 25  # Ø8.40
X_DIM_OFFSET_3 = X_RSV_START - 35  # Ø8.00

# Function to place diameter dimensions
def place_diameter_dim(ax, r, x_offset, label):
    y_top = Y_RSV_CENTER + r
    y_bot = Y_RSV_CENTER - r
    ax.plot([X_RSV_START - PADDING, x_offset], [y_top, y_top], 'k-', linewidth=0.5) 
    ax.plot([X_RSV_START - PADDING, x_offset], [y_bot, y_bot], 'k-', linewidth=0.5) 
    ax.plot([x_offset, x_offset], [y_bot, y_top], 'k-', linewidth=0.8) 
    ax.text(x_offset - TEXT_OFFSET, Y_RSV_CENTER, label, ha='right', va='center', rotation=90, fontsize=10, fontweight='bold')

place_diameter_dim(ax, 10.05/2, X_DIM_OFFSET_1, r'$\emptyset 10.05$')
place_diameter_dim(ax, 8.40/2, X_DIM_OFFSET_2, r'$\emptyset 8.40$')
place_diameter_dim(ax, 8.00/2, X_DIM_OFFSET_3, r'$\emptyset 8.00$')


# --- Draw profile segments, thread callouts, and overall length (RSV) ---
for i, data in enumerate(sections_data):
    length, d_major, d_minor, start_z, is_threaded, thread_label = data
    r_major = d_major / 2
    end_z = start_z + length
    
    X_start = X_RSV_START + start_z
    X_end = X_RSV_START + end_z

    # Major Diameter (Profile Outline)
    ax.plot([X_start, X_end], [Y_RSV_CENTER + r_major, Y_RSV_CENTER + r_major], 'k-', linewidth=1.5)
    ax.plot([X_start, X_end], [Y_RSV_CENTER - r_major, Y_RSV_CENTER - r_major], 'k-', linewidth=1.5)
    if i > 0:
        prev_r_major = sections_data[i-1][1] / 2
        ax.plot([X_start, X_start], [Y_RSV_CENTER - prev_r_major, Y_RSV_CENTER - r_major], 'k-', linewidth=1.5)
        ax.plot([X_start, X_start], [Y_RSV_CENTER + prev_r_major, Y_RSV_CENTER + r_major], 'k-', linewidth=1.5)

    # Thread Convention
    if is_threaded:
        # Draw multiple slash lines
        draw_slash_lines(ax, start_z, length, r_major, Y_RSV_CENTER, X_RSV_START, orientation='horizontal')
        # Thread Termination
        termination_z = end_z - length * 0.1 
        X_term = X_RSV_START + termination_z
        ax.plot([X_term, X_term], [Y_RSV_CENTER - r_major, Y_RSV_CENTER + r_major], 'k-', linewidth=0.5)

        # Thread Callout (Above profile)
        # Note: We reuse this space for thread info, which includes the length (MxxLx7.5)
        dim_y = Y_TOP_PROFILE + DIM_OFFSET * (1 + i/4) 
        ax.plot([X_start, X_start], [Y_TOP_PROFILE, dim_y], 'k-', linewidth=0.5)
        ax.plot([X_end, X_end], [Y_TOP_PROFILE, dim_y], 'k-', linewidth=0.5)
        ax.plot([X_start, X_end], [dim_y, dim_y], 'k-', linewidth=0.8)
        ax.text(X_start + length / 2, dim_y + TEXT_OFFSET, thread_label + f' L={length}', ha='center', va='bottom', fontsize=10, fontweight='bold')
        
    # Overall Length dimension (placed below the profile - only on last iteration)
    if i == len(sections_data) - 1:
        dim_y_total = Y_RSV_CENTER - MAX_RADIUS - DIM_OFFSET 
        ax.plot([X_RSV_START, X_RSV_START], [Y_RSV_CENTER - MAX_RADIUS, dim_y_total], 'k-', linewidth=0.5)
        ax.plot([X_RSV_START + TOTAL_LENGTH, X_RSV_START + TOTAL_LENGTH], [Y_RSV_CENTER - MAX_RADIUS, dim_y_total], 'k-', linewidth=0.5)
        ax.plot([X_RSV_START, X_RSV_START + TOTAL_LENGTH], [dim_y_total, dim_y_total], 'k-', linewidth=0.8)
        ax.text(X_RSV_START + TOTAL_LENGTH / 2, dim_y_total - TEXT_OFFSET, f'{TOTAL_LENGTH}', ha='center', va='top', fontsize=10, fontweight='bold')


# End caps
ax.plot([X_RSV_START, X_RSV_START], [Y_RSV_CENTER - sections_data[0][1]/2, Y_RSV_CENTER + sections_data[0][1]/2], 'k-', linewidth=1.5)
ax.plot([X_RSV_START + TOTAL_LENGTH, X_RSV_START + TOTAL_LENGTH], [Y_RSV_CENTER - sections_data[-1][1]/2, Y_RSV_CENTER + sections_data[-1][1]/2], 'k-', linewidth=1.5)


# --- 3. New Top View (TV) - Profile (Vertical) ---
X_TV_CENTER = X_FV_CENTER
Y_TV_START = Y0 + MAX_DIAMETER + SPACING + DIM_OFFSET * 2 
X_TV_LEFT = X_TV_CENTER - MAX_RADIUS

# Centerline for TV
ax.plot([X_TV_CENTER, X_TV_CENTER], [Y_TV_START, Y_TV_START + TOTAL_LENGTH], 'k-.', linewidth=0.8)
ax.text(X_TV_CENTER, Y_TV_START + TOTAL_LENGTH + 5, 'TOP VIEW (Profile)', ha='center', va='bottom')

# --- NEW: Sectional Length Dimensioning on the Left of TV ---
X_DIM_LENGTH_SECT = X_TV_CENTER - MAX_RADIUS - 10

# Iterating to place sectional dimensions
for i, data in enumerate(sections_data):
    length, d_major, d_minor, start_z, is_threaded, thread_label = data
    Y_start = Y_TV_START + start_z
    Y_end = Y_TV_START + start_z + length
    
    # Major Diameter (Profile Outline)
    r_major = d_major / 2
    ax.plot([X_TV_CENTER + r_major, X_TV_CENTER + r_major], [Y_start, Y_end], 'k-', linewidth=1.5)
    ax.plot([X_TV_CENTER - r_major, X_TV_CENTER - r_major], [Y_start, Y_end], 'k-', linewidth=1.5)

    # Step Edges (Horizontal Lines)
    if i > 0:
        prev_r_major = sections_data[i-1][1] / 2
        ax.plot([X_TV_CENTER - prev_r_major, X_TV_CENTER - r_major], [Y_start, Y_start], 'k-', linewidth=1.5)
        ax.plot([X_TV_CENTER + prev_r_major, X_TV_CENTER + r_major], [Y_start, Y_start], 'k-', linewidth=1.5)
    
    # Thread Convention
    if is_threaded:
        # Draw multiple slash lines (horizontal for vertical view)
        num_slashes = int(length / SLASH_PITCH)
        for j in range(num_slashes + 1):
            y_pos = Y_TV_START + start_z + j * SLASH_PITCH
            if y_pos > Y_TV_START + end_z:
                y_pos = Y_TV_START + end_z
                
            ax.plot([X_TV_CENTER - r_major, X_TV_CENTER + r_major], 
                    [y_pos, y_pos], 
                    'k-', linewidth=0.5, alpha=0.7)

        # Thread Termination 
        termination_z = end_z - length * 0.1 
        Y_term = Y_TV_START + termination_z
        ax.plot([X_TV_CENTER - r_major, X_TV_CENTER + r_major], [Y_term, Y_term], 'k-', linewidth=0.5)

    
    # --- ADD SECTIONAL LENGTH DIMENSIONS HERE (Left of TV) ---
    # Extension lines
    ax.plot([X_TV_LEFT, X_DIM_LENGTH_SECT], [Y_start, Y_start], 'k-', linewidth=0.5)
    ax.plot([X_TV_LEFT, X_DIM_LENGTH_SECT], [Y_end, Y_end], 'k-', linewidth=0.5)

    # Dimension line
    ax.plot([X_DIM_LENGTH_SECT, X_DIM_LENGTH_SECT], [Y_start, Y_end], 'k-', linewidth=0.8)
    
    # Dimension text
    text_label = f'{length:.1f}' if length != int(length) else f'{int(length)}'

    if length < 5: 
        text_x = X_DIM_LENGTH_SECT - TEXT_OFFSET * 2
        text_y = Y_start + length / 2
        ax.text(text_x, text_y, text_label, ha='right', va='center', fontsize=10)
    else:
        ax.text(X_DIM_LENGTH_SECT + TEXT_OFFSET, Y_start + length / 2, text_label, ha='left', va='center', fontsize=10, rotation=-90)

# End caps (Horizontal lines at start/end of the part)
ax.plot([X_TV_CENTER - sections_data[0][1]/2, X_TV_CENTER + sections_data[0][1]/2], [Y_TV_START, Y_TV_START], 'k-', linewidth=1.5)
ax.plot([X_TV_CENTER - sections_data[-1][1]/2, X_TV_CENTER + sections_data[-1][1]/2], [Y_TV_START + TOTAL_LENGTH, Y_TV_START + TOTAL_LENGTH], 'k-', linewidth=1.5)


# --- Set Limits and clean up plot ---
X_MIN = X_RSV_START - 45 
X_MAX = X_RSV_START + TOTAL_LENGTH + PADDING + 5
Y_MAX = Y_TV_START + TOTAL_LENGTH + PADDING + 15
Y_MIN = Y_RSV_CENTER - MAX_RADIUS - DIM_OFFSET * 2

ax.set_xlim(X_MIN, X_MAX)
ax.set_ylim(Y_MIN, Y_MAX)
ax.axis('off')

# --- Save to PNG ---
output_filename = 'stepped_threaded_cylinder_final_dim_complete.png'
plt.savefig(output_filename, bbox_inches='tight')

print(f"Drawing saved as {output_filename}")