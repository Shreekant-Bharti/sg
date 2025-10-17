"""
Helper script to create placeholder images for the romantic website.
Run this if you don't have photos ready yet - it will create beautiful placeholder images.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder_image(filename, text, bg_color, text_color):
    """Create a beautiful placeholder image with gradient and text"""
    # Create image
    width, height = 800, 800
    image = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(image)
    
    # Add gradient effect (simple version)
    for i in range(height):
        r = int(bg_color[0] + (255 - bg_color[0]) * (i / height) * 0.3)
        g = int(bg_color[1] + (255 - bg_color[1]) * (i / height) * 0.3)
        b = int(bg_color[2] + (255 - bg_color[2]) * (i / height) * 0.3)
        draw.rectangle([(0, i), (width, i+1)], fill=(r, g, b))
    
    # Add decorative elements
    # Draw hearts
    heart_positions = [(150, 150), (650, 150), (150, 650), (650, 650), (400, 400)]
    for x, y in heart_positions:
        draw.ellipse([x-30, y-20, x+30, y+40], fill=(255, 192, 203, 100))
        draw.ellipse([x-60, y-20, x, y+40], fill=(255, 192, 203, 100))
        draw.polygon([(x-60, y+10), (x, y+70), (x+30, y+10)], fill=(255, 192, 203, 100))
    
    # Add text
    try:
        # Try to use a nice font
        font = ImageFont.truetype("arial.ttf", 60)
        emoji_font = ImageFont.truetype("seguiemj.ttf", 80)
    except:
        # Fallback to default font
        font = ImageFont.load_default()
        emoji_font = font
    
    # Calculate text position (centered)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((width - text_width) // 2, (height - text_height) // 2)
    
    # Draw text with shadow
    shadow_offset = 3
    draw.text((position[0] + shadow_offset, position[1] + shadow_offset), text, 
              fill=(0, 0, 0, 100), font=font)
    draw.text(position, text, fill=text_color, font=font)
    
    # Add emoji
    emoji_text = "❤️💕"
    emoji_bbox = draw.textbbox((0, 0), emoji_text, font=emoji_font)
    emoji_width = emoji_bbox[2] - emoji_bbox[0]
    emoji_pos = ((width - emoji_width) // 2, position[1] - 120)
    draw.text(emoji_pos, emoji_text, fill=text_color, font=emoji_font)
    
    # Save image
    image.save(filename, 'JPEG', quality=95)
    print(f"✓ Created {filename}")

def main():
    # Create images directory if it doesn't exist
    images_dir = 'static/images'
    os.makedirs(images_dir, exist_ok=True)
    
    # Create placeholder images with different colors and messages
    placeholders = [
        ('memory1.jpg', 'Our First Date', (255, 182, 193), (139, 0, 69)),    # Pink
        ('memory2.jpg', 'Beautiful Day', (255, 218, 185), (184, 76, 0)),     # Peach
        ('memory3.jpg', 'Sweet Moment', (230, 190, 255), (75, 0, 130)),      # Lavender
        ('memory4.jpg', 'Forever Love', (255, 192, 203), (199, 21, 133))     # Hot Pink
    ]
    
    print("Creating placeholder images...")
    print("=" * 50)
    
    for filename, text, bg_color, text_color in placeholders:
        filepath = os.path.join(images_dir, filename)
        create_placeholder_image(filepath, text, bg_color, text_color)
    
    print("=" * 50)
    print("✓ All placeholder images created successfully!")
    print("\nYou can now run the Flask app with: python app.py")
    print("\nDon't forget to replace these placeholders with your real photos! 💕")

if __name__ == '__main__':
    try:
        main()
    except ImportError:
        print("PIL (Pillow) not found. Installing...")
        print("Run: pip install Pillow")
        print("\nThen run this script again: python create_placeholders.py")
