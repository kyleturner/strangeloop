#Strange Loop Workshop 2: JQuery - Nathaniel Schutta

##Basics 

* Called when the document loads: ```$(document).ready(function() {})```


##CSS Selectors

Very powerful tool to access and modify CSS elements

For Example:

Toggling the visibility of a child element with the _blind_ effect.  calling ```next()``` grabs the child element of the _header_ class, and toggles the display.  Also, ```toggleClass``` will change _this_'s expanded class to closed, and vise-versa when clicked.

```
$(".header").click(function() {
    $(this).next().toggle("blind", {direction: "vertical"}, 500)
    $(this).toggleClass("expanded closed")
})
```


##JQuery UI - Widgets

Include ```ui.core```, ```ui.widget```, and ui specific widget([options])


##Events

* DOM Navigation
* Add HTML to DOM - but this changes the DOM!

If we add an item to a list through ```parent().append()```, we aren't able to handle a **click** event to the newly added item (as it hasn't been updated in the DOM)

How can we update the DOM _live_?  How can we attach to elements that haven't been added yet?

* use live() function so the **new** elements are clickable too!

```
$(".element").live('click', function() {
    $(this).parent().append('<li class="element">Hey here\'s another clickme item!</li>')
})
```


##AutoSuggest

Have a large data source with too many options, and wish to simplify a user's searching ability via autocomplete? Simple enough.

```
<script src="../javascript/jqueryUI/jquery.ui.autocomplete.js" type="text/javascript"></script>
```

```
<script src="../javascript/jqueryUI/jquery.ui.position.js" type="text/javascript"></script>
```

```
$('#element').autocomplete({
    source: providedDataSource
})
```


##Plug-ins


