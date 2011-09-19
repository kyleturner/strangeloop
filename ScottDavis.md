##Airplane-Mode HTML5

Scott Davis

**The big question: Native or HTML5?**


#Screen/Window size

**Desktop Screen != Window**

http://resizemybrowser.com

_What do you do to get around dimension issues?_

```<meta name="viewport" content="width=device-width", initial-scale=2.0, user-scalable=yes />```

http://html-5.com/metatags


#Portrait/Landscape

**CSS3 Media Queries**

Orientation 

```@media all and (orientation: portrait){ }```

Other query options:

* width (device-width)
* height (device-height)
* orientation (portrait | landscape)
* aspect-ratio (device-aspect-ratio)
* resolution
* color, color-index

Example of resizing for multiple devices - http://2011.dconstruct.org

Responsive Web Design - Ethan Marcotte


#Touch Events

**No mouse == no hover**

"This very blunt meatstick is an incredibly expressive input device"

```addEventListener('event', function(e) {})```

* touchstart
* touchmove
* touchend
* touchcancel
* touches
* targetTouches

* gesturestart
* gestureend
* gesturechange
* event.scale
* event.rotate


##Mobile Ready

1. LocalViews, Remote Data

2. Application Cache

Explicity assure content is available in airplane mode

3. Local Storage

User data is excessible too!


**Concepts**

#Resources 

http://batmanjs.org/

http://www.html5rocks.com/en/

