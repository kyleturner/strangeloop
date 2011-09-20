#Taming Android - Eric Burke, Square Inc

http://tamingandroid.com

##Custom View from Scratch

**Keep it Square**

* Extend View class
    * implement onMeasure method, ask superclass for default width and height (getSuggestedMinimumWidth, getSuggestedMinimumHeight)
    * int min = Math.min(minWidth, minHeight)
    * setMeasuredDimension(min,min)

* Rounded Corners!
    * Don't use ```canvas.clipPath(roundedRect)``` = jagged rounded corners
    * Can use dimensions.xml file, but not scalable
    * use Alpha Compositing (google search _Alpha compositing_)
        * ```paint.setXfermode(new PorterDuffXfermode(PorterDuff.Mode.SRC_IN))```
        * preserves anti-aliasing (smooth, nice corners…yum)
    * How?
        * Create imageDrawable (as bitmapDrawable or image placeholder)
        * Create offscren bitmap to ensure anti-aliasing ```Bitmap.createBitmap(size, size, Bitmap.Config.ARGB_8888)```
        * Create canvas from this bitmap output
        * Draw outerRect
        * draw a round rectangle in a solid color via paint
            * ```paint =  new Paint(Paint.ANTI_ALIAS_FLAG)```
        * set Xfermode for the paint ``paint.setXfermode(new PorterDuffXfermode(PorterDuff.Mode.SRC_IN))```
        * save the layer onto the canvas ```canvas.saveLayer(outerRect, paint, Paint.FILTER_BITMAP_FLAG)```
        * ```canvas.restore()```
        
##Suttle Gradient Background

_Adds depth, character, and even a feel of texture_

**invalidate dawables when bounds change**
**test w/ bright, primary colors**

* extend ```LinearLayout```
* ```setBackgroundResource(R.drawable.plaastic_windor_background)``` - defined from the XML file

* Triangular Shine
    * get width/height of view, multiply it by 0.85, will scale to any screen size
    * create a new Path object
    * ```path.moveTo```
    * ```path.lineTo```
    * ```path.close```
    * ```path.setShinePath()``` - shinePath defined variable on object
    
    * override ```dispatchDraw```
        * draw the shine (```drawPath(shinePath, shinePaint)```)
        * draw the childen (```super.dispatchDraw(canvas)```)

    * XML Usage (define fully qualified plastic name)


##Custom Attributes

* ```res/values/attrs.xml```
* declare-styleable, list attributes (caption, captionSize, placeholder)

* Attribute Namespace


##Pro Tips

Anytime you have editable text field, look at ```android:imeOptions``` (you can control buttons on keyboard: actionDone, actionNext, etc.)

* Register an OnEditorActionListener to handle when **done** button is clicked

* set inputType to control what kind of keyboard appears (```phone```, ```textPersonName|textCapWords``` - always caps first letters of names)


##ViewFlipper

_Similar to iOS flipping views, or page view control.  ViewFlipper crashes app prior to Honeycomb_, catch IllegalArgumentExepction with **SaveViewFlipper**!


##Square Contact Tab Screen

* override ```getChildDrawingOrder``` to control stack of how cards are drawn
* override drawChild(), call ```canvas.clipRect()```
* ```canvas.translate()``` and ```canvas.rotate()``` - to portray stack of random cards within card case view
