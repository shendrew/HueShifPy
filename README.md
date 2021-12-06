# PyxelHue
An automatic hue shifter built using Python. 

Hue shift is a technique that helps the artists pick colours for highlights and shadows to give the drawing more depth.

Areas in contact with light is shifted towards yellow, shadows are shifted towards blue.

Example:
![Hue Shift](https://www.davidepesce.com/wp-content/uploads/2020/04/colors_7_limited_colors-1024x334.png)


How to use PyxelHue:

1.
Run "main.py".

2.
Input a colour in HSV format (values separated by space):
h: 0 to 360
s: 0 to 100
v: 0 to 100

3.
The highlight and shading colours will be generated
in HEX values from lightest to darkest.

A link to coolors.co will be generated to visualize the results.

ex:
(input) 120 60 70
(output) https://coolors.co/e0ffa3-93d971-47b247-278a48-106146


To do:
Executable GUI for application.
Local colour visualization.
Customizable hue shift parameters.
