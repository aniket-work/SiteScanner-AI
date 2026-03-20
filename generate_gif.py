import os
from PIL import Image, ImageDraw, ImageFont
import json

# Configuration
WIDTH, HEIGHT = 900, 550
BG_COLOR = (20, 20, 25)
TERM_COLOR = (30, 30, 35)
TEXT_COLOR = (240, 240, 240)
HEADER_COLOR = (60, 60, 70)
GREEN = (80, 250, 123)
BLUE = (139, 233, 253)
YELLOW = (241, 250, 140)
RED = (255, 85, 85)

def create_terminal_frame(commands, lines, cursor_pos=None, show_table=False):
    """Creates a frame mimicking a Mac-style terminal."""
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Terminal Window
    term_x, term_y = 50, 50
    term_w, term_h = WIDTH - 100, HEIGHT - 100
    draw.rounded_rectangle([term_x, term_y, term_x + term_w, term_y + term_h], radius=10, fill=TERM_COLOR)
    
    # Header Bar
    draw.rounded_rectangle([term_x, term_y, term_x + term_w, term_y + 30], radius=10, fill=HEADER_COLOR)
    # Buttons
    for i, color in enumerate([RED, YELLOW, GREEN]):
        draw.ellipse([term_x + 10 + (i * 20), term_y + 8, term_x + 22 + (i * 20), term_y + 20], fill=color)
    
    # Font
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Monaco.ttf", 16)
        bold_font = ImageFont.truetype("/System/Library/Fonts/Monaco.ttf", 18)
    except:
        font = ImageFont.load_default()
        bold_font = ImageFont.load_default()

    # Content
    y_offset = term_y + 45
    for line in lines:
        draw.text((term_x + 20, y_offset), line, font=font, fill=TEXT_COLOR)
        y_offset += 25
    
    if cursor_pos:
        draw.rectangle([cursor_pos[0], cursor_pos[1], cursor_pos[0] + 10, cursor_pos[1] + 20], fill=TEXT_COLOR)

    if show_table:
        table_lines = [
            "+----------+-------+------------+---------+",
            "| SITE_ID  | SCORE | INCOME     | TRAFFIC |",
            "+----------+-------+------------+---------+",
            "| SITE_020 | 79.55 | $94,690    | 4465    |",
            "| SITE_017 | 78.74 | $104,022   | 3707    |",
            "| SITE_039 | 77.47 | $112,373   | 3997    |",
            "+----------+-------+------------+---------+"
        ]
        for line in table_lines:
            draw.text((term_x + 20, y_offset), line, font=font, fill=YELLOW)
            y_offset += 22

    return img

def create_ui_frame(title, stats):
    """Creates a premium UI frame showing analysis results."""
    img = Image.new("RGB", (WIDTH, HEIGHT), (30, 32, 40))
    draw = ImageDraw.Draw(img)
    
    # Simple UI Cards
    draw.text((50, 50), title, fill=BLUE, font_size=32)
    
    card_x = 50
    card_y = 120
    for key, val in stats.items():
        draw.rounded_rectangle([card_x, card_y, card_x + 350, card_y + 80], radius=12, fill=(45, 48, 60))
        draw.text((card_x + 20, card_y + 15), key.replace('_', ' ').title(), fill=TEXT_COLOR, font_size=18)
        draw.text((card_x + 20, card_y + 40), str(val), fill=GREEN, font_size=24)
        card_y += 100
        if card_y > 400:
            card_x += 400
            card_y = 120
            
    return img

def generate_gif():
    frames = []
    
    # 1. Terminal Part: Typing commands
    cmd = "$ python main.py"
    current_lines = []
    for i in range(len(cmd) + 1):
        lines = [cmd[:i]]
        frames.append(create_terminal_frame(cmd, lines, cursor_pos=(50 + 20 + len(cmd[:i])*10, 50 + 45)))
    
    # 2. Execution Logs
    logs = [
        "--- [SiteScanner-AI] Starting Analysis ---",
        "[1/5] Synthesizing urban geospatial layers...",
        "[2/5] Running spatial optimization models...",
        "[3/5] Identifying strategic corridors...",
        "[4/5] Generating interactive visualization...",
        "[5/5] Analysis complete! Map saved."
    ]
    for i in range(len(logs) + 1):
        display_lines = [cmd] + logs[:i]
        for _ in range(2): # Hold slightly
            frames.append(create_terminal_frame(cmd, display_lines))
    
    # 3. Final Table
    frames.append(create_terminal_frame(cmd, display_lines + ["", "Top Recommendations:"], show_table=True))
    for _ in range(15): # Hold terminal table
        frames.append(create_terminal_frame(cmd, display_lines + ["", "Top Recommendations:"], show_table=True))

    # 4. Transition to UI
    stats = {
        "Total Sites Analyzed": 40,
        "Optimal Locations Found": 5,
        "Avg Reliability Score": "76.4%",
        "Target City": "San Francisco",
        "Competitor Proximity": "Safe"
    }
    ui_frame = create_ui_frame("SiteScanner-AI Dashboard", stats)
    for _ in range(25): # Hold UI
        frames.append(ui_frame)

    # MANDATORY: Savig with Global Palette and P-Mode
    print("Optimizing GIF with global palette...")
    sample = Image.new("RGB", (WIDTH, HEIGHT * 3))
    sample.paste(frames[0], (0,0))
    sample.paste(frames[len(frames)//2], (0, HEIGHT))
    sample.paste(frames[-1], (0, HEIGHT*2))
    palette = sample.quantize(colors=256, method=2)
    
    final_frames = [f.quantize(palette=palette, dither=Image.Dither.NONE) for f in frames]
    os.makedirs("images", exist_ok=True)
    OUTPUT = "images/title-animation.gif"
    final_frames[0].save(OUTPUT, save_all=True, append_images=final_frames[1:], optimize=True, loop=0, duration=100)
    print(f"✅ Saved {OUTPUT}")

if __name__ == "__main__":
    generate_gif()
