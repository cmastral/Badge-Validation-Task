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
