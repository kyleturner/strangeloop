
#Strange Loop Workshop 1: HTML5 - Nathaniel Schutta

##Userful Links

* http://html5examples.com
* http://html5demos.com

##Modernizr!

http://modernizr.com

JavaScript library that detects the availability of native implementations for next-generation web technologies, i.e. features that stem from the HTML5 and CSS3 specifications
    
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