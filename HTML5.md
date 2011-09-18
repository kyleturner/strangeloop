#Strange Loop Workshop 1: HTML5 - Nathaniel Schutta

##Userful Links

* http://html5demos.com
* http://diveintohtml5.org

##Modernizr

http://modernizr.com : JavaScript library that detects the availability of native implementations for next-generation web technologies, i.e. features that stem from the HTML5 and CSS3 specifications
    
What Can Your Browser Do:

* http://caniuse.com
* http://findmebyip.com


##HTML5 Goodness
 <!DOCTYPE HTML> - how simple is that?


##Objects/Common Markup

* section
* nav - navigate around page, navigation block
* article - post, blog entry, etc. reusable and distributable
* aside - tangential content, not main content
* hgroup - group headers
* header - doesn't actually create a new 'section' <header></header>
* footer - doesn't actually create a new 'section' <footer></footer>
* time - encode time/date for machine use (calendar events); flexible; doesn't have to match datetime attribute; pubdate is attribute to identify its a publication  <time datetime="2011-02-22" pubdate>February 22, 2011</time>
* mark - highlight; calls attention to something


##New Input Types! (13 in total)

If the browser doesn't support it, its treated as text field.

Some New Types:

* search (with a given cancellation button, wahoo)
* spinner
* slider (range)
* color picker
* telephone number (tel)
* url
* email
* password
* date, month, week, timestamp
* datetime
* number - allows step, value, min, and max attributes

**Why?**

* These input types leverage the _keyboard input types on your mobile device_.
* Replace that silly large space bar with an **@ symbol** and a **period**  when typing an e-mail
* Entering a phone number?  Make the input type **tel** and the number keypad will be displayed

##Handy Javascript Also Included

* _stepUp()_ and _stepUp()_ methods to increase the value of _n_
* _valueAsNumber_ attribute converts string value to an actual number value.

##Other Attributes

* _required_ : a required field on a form (still have to identify to user that it is required)
* _autofocus_ 
* _placeholder_ 
* _novalidate_ : Add this attribute to a form to remove default validation

##Local Storage

Sometimes referenced as 'DOM Storage'.  Simple way to store **key/value pairs**.  Similar to cookies, but bigger and stays local.  Wide support.

Caviats

* Key is a string
* Data can be any JavaScript data type - but stored as a string

* getItem(key) - returns _null_ if bad key provided
* setItem(key, value) - silently overwrites old values

Can treat local storage as associated array, aka **bracket notation**

* ```localStorage['key']``` == ```localStorage.getItem('key')```
* ```localStorage.length``` - number of stored values in local storage
* ```key(index)``` - retrieves key @ given index
* index out of bounds returns **null**

StorageEvent - cannot cancel a storage event!

Default 5MB of max space - if exceeded, _QUOTA_EXCEEDED_ERROR_ 

* ```key```
* ```oldValue```
* ```newValue```
* ```url``` of caller

##Canvas!

**Attributes**

Can be styled just like an image. Any content between the tags are displayed by browsers who don't support canvas.

* width
* height

To draw, we have to get the **context of the canvas**:
```var ctx = canvas.getContext("2D")```

**Rectangle: Methods**

_All take the same x,y,width,height arguements_

* fillStyle
* fillRect
* strokeRect
* clearRect

**Paths: Methods**

* beginPath()
* arc()
* closePath()
* stroke()
* fill()
* moveTo()
* stroke()