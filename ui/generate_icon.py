from PIL import Image, ImageDraw

icon_size = 256
image = Image.new('RGB', (icon_size, icon_size), color=(30, 144, 255))
draw = ImageDraw.Draw(image)
draw.rectangle((64, 64, 192, 192), fill="white")
draw.text((100, 96), "✓", fill="blue")

output_path = "productivity_icon.ico"
image.save(output_path, format='ICO')
print(f"Icon saved to: {output_path}")
