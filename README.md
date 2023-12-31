## Description
Technical task to verify and validate badges uploaded by users. The tool checks various criteria to determine if the badge meets the required specifications.

## Criteria for Valid Badge
To be considered a valid badge, the uploaded image must meet the following criteria:

- The image size must be exactly 512x512 pixels.
- The non-transparent pixels in the image must fall within a circular region, indicating the badge's circular shape.
- The badge colors are analyzed to determine if they give a "happy" feeling.

## Happy Feeling Criteria 
The "Happy Feeling" criteria for badge verification involve analyzing the colors of the badge. RGB (Red, Green, Blue) and HSV are two popular color spaces used in computer vision and image processing. Each has its strengths, and combining both allows for a more comprehensive analysis of the color properties. 

- RGB Color Space: RGB is an additive color model where colors are represented as a combination of red, green, and blue components. While RGB is straightforward and intuitive, it may not fully capture the perceptual qualities of colors. For this reason, we use it to extract color information from the badge image.

- HSV Color Space: HSV separates color information into three components: Hue, Saturation, and Value. This makes it easier to work with color information and perform color manipulations based on perceptual qualities. HSV is particularly well-suited for capturing color properties related to emotions, such as brightness and vividness. By converting RGB colors to HSV, we can evaluate the "happy feeling" criteria more accurately.
  
### HVS 
By defining color in the HSV color space, we can focus on specific color properties that evoke emotions, such as bright and warm colors for happiness, cool colors for calmness, etc. In the context of determining "happy colors," we want to focus on colors that are warm, bright and vivid:
- Hue (H): represents the type of color and is measured in degrees around a color wheel. The color wheel starts with red at 0 degrees, then goes through yellow, green, cyan, blue, magenta, and back to red at 360 degrees. Hues that fall in the range of approximately 0 to 60 degrees and 330 to 360 degrees are considered warm. This includes hues like red, orange, and yellow.

- Saturation (S): represents the intensity or purity of the color, ranging from 0 to 100%. Lower saturation means the color is closer to grayscale, while higher saturation means a more vivid color.
  
- Value (V): represents the brightness or intensity of the color, ranging from 0 to 100%.


### Function: has_happy_colors
The has_happy_colors function takes the path of an image and two optional thresholds for saturation and value. It uses the ColorThief library to extract the dominant colors palette from the image.

The ColorThief library is utilized to obtain a palette of dominant colors from the image, which represents the most significant colors in the image.

<img src="https://github.com/cmastral/Badge-Validation-Task/assets/48210775/663c83e4-dec1-48ec-8c1a-8d0e18c834ec" width = 300 height = 300>

<img src="https://github.com/cmastral/Badge-Validation-Task/assets/48210775/eb54cc3a-4f6a-4d63-9016-c63eebaf9545" width = 300 height = 100>

The RGB color is normalized to the range 0.0 to 1.0. Each color in the palette is converted to HSV using colorsys.rgb_to_hsv.

The function checks if at least two dominant colors in the palette meet the criteria for a "happy feeling" color.
If the condition is satisfied for at least two dominant colors, the function returns True, indicating that the image contains "happy feeling" colors. Otherwise, it returns False.


### Usage and Error Handling

In the case of an image lacking "happy feeling" colors, the script can be used to identify such images, and corresponding error messages can be appended to an errors list.

### Subjectivity of Color Perception

The emotion analysis based on colors provided in this project is one of several methodologies that can be used to assess the potential emotional impact of colors. The "happy feeling" color detection in this task is based on color psychology, which associates certain colors with positive emotions or happiness. However, it is essential to understand that the perception of colors and their emotional impact can vary widely. Therefore, the classification of colors as "happy" is not definitive but rather an attempt to identify colors that are generally associated with positive emotions.

- The happy_saturation_threshold determines the minimum saturation level required for a color to be considered "happy." Increasing this threshold may result in detecting more vibrant and saturated colors.

- The happy_value_threshold determines the minimum brightness level required for a color to be considered "happy." Raising this threshold may result in detecting brighter colors.

  
## Convert to badge

The 'convert_to_badge function' is designed to transform an input image into a badge with specific characteristics:

- resized to a square shape of 512x512 pixels using high-quality resizing techniques.

- creates a circular mask and applies it to the resized image, resulting in the image being contained within a circular shape.

- the pixels outside the circular area of the image become transparent, while pixels within the circular area retain their original color and transparency.

- the transformed image, now in the form of a badge, is returned as the output.

This function can be utilized for images to be converted into circular badges, such as avatar images. Additionally, it offers the flexibility to save the transformed badge as a PNG file or display it for further analysis.

## Sample Images of Badge/Avatars

A small selection of sample images of badge/avatars used as references during the development of this project is available in the "sample images" folder. 
