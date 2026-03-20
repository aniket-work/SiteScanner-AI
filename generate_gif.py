import os
from PIL import Image, ImageDraw, ImageFont
import time

# --- CONFIGURATION ---
WIDTH, HEIGHT = 900, 550
BG_COLOR = (30, 30, 30)
TEXT_COLOR = (240, 240, 240)
BAR_COLOR = (50, 50, 50)
ACCENT_GREEN = (0, 255, 65)  # Matrix/Terminal Green
ACCENT_RED = (255, 95, 87)
ACCENT_YELLOW = (255, 189, 46)
ACCENT_BLUE = (0, 122, 255)

# --- MOCK TERMINAL LOGS ---
COMMANDS = ["$ python main.py --station Etching-04", "... initializing LangGraph workflow", "... meta-cognitive router active", "... complexity HIGH detected", "... triggering Level 3 Deep RCA", "--- YieldArch Report ---"]
REPORT = [
    "+----------------+--------------------------------+",
    "|   PARAMETER    |            VALUE               |",
    "+----------------+--------------------------------+",
    "| Reasoning      | Deep Meta-Cognition (Level 3)  |",
    "| Root Cause     | Chem-Plasma Synergic Defect    |",
    "| Yield Impact   | -4.2% (Prevented)              |",
    "| Recommendation | Halt Line & Inspect Manifold   |",
    "+----------------+--------------------------------+"
]

def draw_window_frame(draw):
    """Draws Mac-style terminal frame."""
    draw.rectangle([0, 0, WIDTH, 35], fill=BAR_COLOR)
    # Traffic lights
    draw.ellipse([12, 12, 22, 22], fill=ACCENT_RED)
    draw.ellipse([28, 12, 38, 22], fill=ACCENT_YELLOW)
    draw.ellipse([44, 12, 54, 22], fill=ACCENT_GREEN)
    draw.text((WIDTH//2 - 50, 10), "YieldArch-AI Terminal", fill=(180,180,180))

def create_frames():
    frames = []
    # Try to load a monospaced font
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Courier New.ttf", 16)
        bold_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Courier New Bold.ttf", 20)
    except:
        font = ImageFont.load_default()
        bold_font = ImageFont.load_default()

    # --- PART 1: TERMINAL TYPING ---
    current_lines = []
    
    # Typing command
    cmd = COMMANDS[0]
    for i in range(len(cmd) + 1):
        img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
        draw = ImageDraw.Draw(img)
        draw_window_frame(draw)
        
        y_offset = 60
        # Draw typed command
        draw.text((20, y_offset), cmd[:i] + ("|" if i < len(cmd) else ""), font=font, fill=ACCENT_GREEN)
        frames.append(img)

    # Scrolling logs
    for log in COMMANDS[1:]:
        current_lines.append(log)
        for _ in range(3): # Hold per log
            img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
            draw = ImageDraw.Draw(img)
            draw_window_frame(draw)
            y_offset = 60
            draw.text((20, y_offset), COMMANDS[0], font=font, fill=ACCENT_GREEN)
            y_offset += 30
            for line in current_lines:
                draw.text((20, y_offset), line, font=font, fill=TEXT_COLOR)
                y_offset += 25
            frames.append(img)

    # --- PART 2: ASCII TABLE ---
    for i in range(len(REPORT) + 1):
        img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
        draw = ImageDraw.Draw(img)
        draw_window_frame(draw)
        y_offset = 60
        draw.text((20, y_offset), COMMANDS[0], font=font, fill=ACCENT_GREEN)
        y_offset += 30
        for line in current_lines:
            draw.text((20, y_offset), line, font=font, fill=TEXT_COLOR)
            y_offset += 25
        
        y_offset += 10
        for line in REPORT[:i]:
            draw.text((20, y_offset), line, font=font, fill=ACCENT_GREEN)
            y_offset += 20
        frames.append(img)

    # Hold terminal for a bit
    for _ in range(15):
        frames.append(frames[-1])

    # --- PART 3: TRANSITION TO UI ---
    # Create UI Frame
    ui_img = Image.new("RGB", (WIDTH, HEIGHT), (245, 245, 250)) # Light premium bg
    draw_ui = ImageDraw.Draw(ui_img)
    draw_ui.rectangle([0, 0, WIDTH, 60], fill=ACCENT_BLUE)
    draw_ui.text((20, 15), "YieldArch Dashboard Analytics", fill=(255, 255, 255), font=bold_font)
    
    # Draw Data Cards
    draw_ui.rectangle([50, 100, 300, 250], fill=(255, 255, 255), outline=(200, 200, 200))
    draw_ui.text((70, 120), "Current Yield", fill=(100, 100, 100), font=font)
    draw_ui.text((70, 150), "98.2%", fill=ACCENT_GREEN, font=bold_font)
    
    draw_ui.rectangle([350, 100, 600, 250], fill=(255, 255, 255), outline=(200, 200, 200))
    draw_ui.text((370, 120), "Agent Status", fill=(100, 100, 100), font=font)
    draw_ui.text((370, 150), "Deep Mode", fill=ACCENT_BLUE, font=bold_font)

    draw_ui.rectangle([650, 100, 850, 250], fill=(255, 255, 255), outline=(200, 200, 200))
    draw_ui.text((670, 120), "Anomalies", fill=(100, 100, 100), font=font)
    draw_ui.text((670, 150), "1 Critical", fill=ACCENT_RED, font=bold_font)

    # Hold UI
    for _ in range(20):
        frames.append(ui_img)

    return frames

def save_optimized_gif(frames, output="images/title-animation.gif"):
    os.makedirs("images", exist_ok=True)
    
    # Generate global palette from sample frames (start, middle, end)
    sample = Image.new("RGB", (WIDTH, HEIGHT * 3))
    sample.paste(frames[0], (0, 0))
    sample.paste(frames[len(frames)//2], (0, HEIGHT))
    sample.paste(frames[-1], (0, HEIGHT * 2))
    
    # Quantize to 256 colors
    palette = sample.quantize(colors=256, method=2)
    
    # Convert all frames to P-mode using global palette (No Dither)
    final_frames = [f.quantize(palette=palette, dither=Image.Dither.NONE) for f in frames]
    
    # Save optimized GIF
    final_frames[0].save(
        output,
        save_all=True,
        append_images=final_frames[1:],
        optimize=True,
        loop=0,
        duration=100
    )
    print(f"Successfully saved {output}")

if __name__ == "__main__":
    frames = create_frames()
    save_optimized_gif(frames)
