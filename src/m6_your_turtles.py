"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Praveen Rammohan.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg

window = rg.TurtleWindow()
window.delay(10)

tom = rg.SimpleTurtle()
tom.pen = rg.Pen('red', 15)
jerry = rg.SimpleTurtle('turtle')
jerry.pen = rg.Pen('blue', 5)

tom.forward(100)
tom.right(90)
tom.backward(70)

jerry.draw_circle(100)
jerry.pen_up()
jerry.backward(400)
jerry.pen_down()

for k in range(6):

    tom.draw_circle(10*k)
    jerry.draw_regular_polygon(10-k,25+5*k)
    jerry.pen_up()
    jerry.forward(100)
    jerry.pen_down()


window.close_on_mouse_click()
