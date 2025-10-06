#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FRY Protocol Roadmap Graphic for LinkedIn
==========================================
Creates a professional roadmap visualization
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Set style
fig, ax = plt.subplots(figsize=(14, 8))
fig.patch.set_facecolor('#0A0A0A')
ax.set_axis_bgcolor('#0A0A0A')

# Colors
fry_yellow = '#FFD700'
fry_orange = '#FF8C00'
fry_red = '#FF4444'
text_color = '#FFFFFF'
box_color = '#1A1A1A'

# Title
fig.text(0.5, 0.95, u'FRY Protocol Roadmap', 
         fontsize=32, weight='bold', color=fry_yellow, ha='center')
fig.text(0.5, 0.90, u'Native Stablecoin Liquidity Infrastructure', 
         fontsize=16, color=text_color, ha='center', alpha=0.8)

# Timeline
timeline_y = 0.75
ax.plot([0.1, 0.9], [timeline_y, timeline_y], color=fry_yellow, linewidth=3, alpha=0.6)

# Q1 2026
q1_x = 0.25
q1_box = FancyBboxPatch((q1_x - 0.12, 0.45), 0.24, 0.25,
                         boxstyle="round,pad=0.01", 
                         facecolor=box_color, edgecolor=fry_orange, linewidth=2)
ax.add_patch(q1_box)

ax.text(q1_x, timeline_y + 0.05, u'Q1 2026', fontsize=18, weight='bold', 
        color=fry_orange, ha='center')
ax.plot([q1_x, q1_x], [timeline_y, 0.7], color=fry_orange, linewidth=2, linestyle='--', alpha=0.5)

ax.text(q1_x, 0.65, '10+ DEX', fontsize=12, color=text_color, ha='center', weight='bold')
ax.text(q1_x, 0.61, 'Integrations', fontsize=10, color=text_color, ha='center', alpha=0.8)

ax.text(q1_x, 0.57, '$50M+ TVL', fontsize=12, color=fry_yellow, ha='center', weight='bold')

ax.text(q1_x, 0.53, '500+ Agent B', fontsize=12, color=text_color, ha='center', weight='bold')
ax.text(q1_x, 0.49, 'Instances', fontsize=10, color=text_color, ha='center', alpha=0.8)

# Q2 2026
q2_x = 0.65
q2_box = FancyBboxPatch((q2_x - 0.12, 0.45), 0.24, 0.25,
                         boxstyle="round,pad=0.01", 
                         facecolor=box_color, edgecolor=fry_red, linewidth=2)
ax.add_patch(q2_box)

ax.text(q2_x, timeline_y + 0.05, u'Q2 2026', fontsize=18, weight='bold', 
        color=fry_red, ha='center')
ax.plot([q2_x, q2_x], [timeline_y, 0.7], color=fry_red, linewidth=2, linestyle='--', alpha=0.5)

ax.text(q2_x, 0.65, 'Cross-Chain', fontsize=12, color=text_color, ha='center', weight='bold')
ax.text(q2_x, 0.61, 'Expansion', fontsize=10, color=text_color, ha='center', alpha=0.8)

ax.text(q2_x, 0.57, 'Institutional', fontsize=12, color=fry_yellow, ha='center', weight='bold')
ax.text(q2_x, 0.53, 'Partnerships', fontsize=10, color=text_color, ha='center', alpha=0.8)

ax.text(q2_x, 0.49, 'Advanced ML', fontsize=12, color=text_color, ha='center', weight='bold')

# Current Status
status_y = 0.30
status_box = FancyBboxPatch((0.05, status_y - 0.08), 0.9, 0.15,
                            boxstyle="round,pad=0.01", 
                            facecolor=box_color, edgecolor=fry_yellow, linewidth=2)
ax.add_patch(status_box)

ax.text(0.5, status_y + 0.04, u'Current Status: Production Ready', 
        fontsize=16, weight='bold', color=fry_yellow, ha='center')

# Metrics
metrics_y = status_y - 0.02
ax.text(0.15, metrics_y, '2.26 FRY/$1', fontsize=11, color=text_color, ha='center', weight='bold')
ax.text(0.15, metrics_y - 0.03, 'Minting Rate', fontsize=9, color=text_color, ha='center', alpha=0.7)

ax.text(0.35, metrics_y, '7.4x', fontsize=11, color=text_color, ha='center', weight='bold')
ax.text(0.35, metrics_y - 0.03, 'Capital Efficiency', fontsize=9, color=text_color, ha='center', alpha=0.7)

ax.text(0.55, metrics_y, '61.5%', fontsize=11, color=text_color, ha='center', weight='bold')
ax.text(0.55, metrics_y - 0.03, 'Volatility ↓', fontsize=9, color=text_color, ha='center', alpha=0.7)

ax.text(0.75, metrics_y, 'USDH/USDF', fontsize=11, color=text_color, ha='center', weight='bold')
ax.text(0.75, metrics_y - 0.03, 'Native Only', fontsize=9, color=text_color, ha='center', alpha=0.7)

# Footer
fig.text(0.5, 0.08, 'Native Stablecoin Strategy: Hyperliquid (USDH) • Aster (USDF)', 
         fontsize=12, color=text_color, ha='center', alpha=0.8)
fig.text(0.5, 0.04, 'github.com/aidanduffy68-prog/FRY-Protocol', 
         fontsize=11, color=fry_orange, ha='center')

# Remove axes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Save
plt.tight_layout()
plt.savefig('FRY_Roadmap_LinkedIn.png', dpi=300, bbox_inches='tight', facecolor='#0A0A0A')
print("✅ Roadmap graphic saved: FRY_Roadmap_LinkedIn.png")
print("📐 Size: 1400x800px (optimized for LinkedIn)")
