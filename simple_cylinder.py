import matplotlib.pyplot as plt
import io
import base64  # Optional: for base64 output if needed

# Create a simple three-view drawing for solid cylinder
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

# Front View
axs[0].set_title('Front View')
axs[0].add_patch(plt.Rectangle((0, 0), 10, 100, fill=False, edgecolor='black'))
axs[0].plot([5, 5], [0, 100], 'k--', linewidth=0.5)  # Centerline
axs[0].set_xlim(-5, 15)
axs[0].set_ylim(-10, 110)
axs[0].set_aspect('equal')
axs[0].axis('off')
axs[0].annotate('100 mm', xy=(5, 105), xytext=(5, 115), ha='center', fontsize=10)
axs[0].annotate('Ø10 mm', xy=(15, 50), xytext=(20, 50), ha='left', fontsize=10)

# Top View
axs[1].set_title('Top View')
circle = plt.Circle((5, 5), 5, fill=False, edgecolor='black')
axs[1].add_patch(circle)
axs[1].plot([0, 10], [5, 5], 'k--', linewidth=0.5)  # Centerline
axs[1].set_xlim(0, 10)
axs[1].set_ylim(0, 10)
axs[1].set_aspect('equal')
axs[1].axis('off')
axs[1].annotate('Ø10 mm', xy=(5, 10), xytext=(5, 12), ha='center', fontsize=10)

# Right View
axs[2].set_title('Right View')
axs[2].add_patch(plt.Rectangle((0, 0), 100, 10, fill=False, edgecolor='black'))
axs[2].plot([50, 50], [5, 5], 'k--', linewidth=0.5)  # Centerline
axs[2].set_xlim(-10, 110)
axs[2].set_ylim(-5, 15)
axs[2].set_aspect('equal')
axs[2].axis('off')
axs[2].annotate('100 mm', xy=(105, 5), xytext=(115, 5), ha='left', fontsize=10)
axs[2].annotate('Ø10 mm', xy=(50, 15), xytext=(50, 20), ha='center', fontsize=10)

plt.tight_layout()

# Save as PNG file
plt.savefig('cylinder_three_view.png', dpi=150, bbox_inches='tight')
print("PNG saved as 'cylinder_three_view.png'")

# Optional: Print base64 for embedding (if you want it)
# buf = io.BytesIO()
# plt.savefig(buf, format='png', dpi=150, bbox_inches='tight')
# buf.seek(0)
# img_base64 = base64.b64encode(buf.read()).decode('utf-8')
# print(f'data:image/png;base64,{img_base64}')