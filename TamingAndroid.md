#Taming Android - Eric Burke, Square Inc

http://tamingandroid.com

##Custom View from Scratch

Keep it Square

* Extend View class
    * implement onMeasure method, ask superclass for default width and height (getSuggestedMinimumWidth, getSuggestedMinimumHeight)
    * int min = Math.min(minWidth, minHeight)
    * setMeasuredDimension(min,min)

* Rounded Corners!
    * Don't use ```canvas.clipPath(roundedRect)``` = jagged rounded corners
    * Can use dimensions.xml file, but not scalable
    * use Alpha Compositing (google search _Alpha compositing_)
        * ``paint.setXfermode(new PorterDuffXfermode(PorterDuff.Mode.SRC_IN))```
        * preserves anti-aliasing (smooth, nice corners…yum)
    * How?
        * Create imageDrawable (as bitmapDrawable or image placeholder)
        * Create offscren bitmap to ensure anti-aliasing ```Bitmap.createBitmap(size, size, Bitmap.Config.ARGB_8888)```
        * Create canvas from this bitmap output
        * Draw outerRect
        * draw a round rectangle in a solid color via paint
            * ```paint =  new Paint(Paint.ANTI_ALIAS_FLAG)```
        * set Xfermode for the paint ``paint.setXfermode(new PorterDuffXfermode(PorterDuff.Mode.SRC_IN))```
        * save the layer onto the canvas ```canvas.saveLayer(outerRect, paint, Paint.FILTER_BITMAP_FLAG)
        * ```canvas.restore()```
        

            