from PIL import Image, ImageDraw

def color_semicircle(image, color, center_x1, center_y1, startInt, endInt):
    width, height = image.size
    # Create a new image with the same size and a transparent background
    semicircle_image = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(semicircle_image)
    center_x = center_x1
    center_y = center_y1
    # Define the radius and color (red or yellow)
    radius = 50  # Adjust the radius as needed

    # Draw the circle
    draw.pieslice(((center_x - radius, center_y - radius),
                   (center_x + radius, center_y + radius)),
                  0, 360, fill=color)  # -90, 90 for C3
    # Combine the original image and the semicircle image
    result_image = Image.alpha_composite(image.convert('RGBA'), semicircle_image)

    # Save or display the result image
    return result_image
