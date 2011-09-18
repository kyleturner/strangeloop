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


##JQuery UI

**Widgets**
Include ```ui.core```, ```ui.widget```, and ui specific widget([options])



