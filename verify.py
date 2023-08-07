from PIL import Image, ImageDraw
from colorthief import ColorThief
import colorsys

def verify_badge(image_path):

    # Open Image
    img = Image.open(image_path) 
    errors = []

    # Show Image
    # img.show() 

    # Check if the image is in PNG format
    if img.format != "PNG":
        errors.append("The image must be in PNG format.")

    # Check the image size
    if img.size != (512, 512): 
         errors.append("Image size should be 512x512.")

    # Image should have an alpha channel (RGBA mode) to handle transparency.
    if img.mode != 'RGBA': 
         errors.append("Image should have a transparent background.")
    else:
        # Check if the non-transparent pixels are within a circle 
        width, height = img.size 
        mask = Image.new("L", (width, height), 0) 
        draw = ImageDraw.Draw(mask) 
        draw.ellipse((0, 0, width, height), fill=255) 
        if img.getchannel('A').getbbox() != mask.getbbox(): 
            errors.append("Non-transparent pixels are not contained within a circle.")

    # Check if the colors give a "happy" feeling 
    if has_happy_colors(path) is False:
        errors.append("The badge colors do not give a happy feeling.")

    if errors:
        return False, errors
    
    return True, "Badge image is valid."


def has_happy_colors(image_path, happy_saturation_threshold=0.6, happy_value_threshold=0.7):

    # Extract dominant colors palette
    color_thief = ColorThief(image_path)
    palette = color_thief.get_palette(color_count=3)

    # Convert RGB colors to HSV and check if at least 2 dominant colors are "happy"
    happy_count = 0
    for color in palette:
        r, g, b = color[0] / 255.0, color[1] / 255.0, color[2] / 255.0 # RGB color is normalized to the range 0.0 to 1.0
        (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
        color_h=round(360*h)
        if (0 <= color_h <= 60 or 330<=color_h<=360) and (s >= happy_saturation_threshold or v >= happy_value_threshold):
            happy_count += 1

    return happy_count >= 2



def convert_to_badge(input_image_path):
    # Load the input image
    img = Image.open(input_image_path)

    # Resize the image to 512x512
    img = img.resize((512, 512), Image.ANTIALIAS)

    # Create a circular mask
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, img.size[0], img.size[1]), fill=255)

    # Apply the circular mask to the image
    img.putalpha(mask)

    # Save the result as a PNG file
    # img.save(output_badge_path, "PNG")
    # img.show()

    print("Image converted to badge successfully.")

# Use case:
path = r"path/to/image"
#convert_to_badge(path)
result, message = verify_badge(path) 

if result:
    print(message)
else:
    print("The badge has the following issues:")
    for error in message:
        print("-", error)
