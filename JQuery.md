#Strange Loop Workshop 2: JQuery - Nathaniel Schutta


Called when the document loads

```$(document).ready(function() {
    })
```

##CSS Selectors

Very powerful tool to access and modify CSS elements

For Example:

Toggling the visibility of a child element.  calling ```next()``` grabs the child element of the _header_ class, and toggles the display.  Also, ```toggleClass``` will change _this_'s expanded class to closed, and vise-versa when clicked.


```
    $(".header").click(function() {
        $(this).next().toggle()
        $(this).toggleClass("expanded closed")
    })
```


