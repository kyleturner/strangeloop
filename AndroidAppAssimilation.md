#Android App Assimilation - Logan Johnson

##Building Blocks

* Intents: Way to package up something you want something else to deal with

    Thing that should happen when something is clicked on
    
    I have something that needs to be viewed, shared, and let the system dispatch to whoever
    
    **Implicit**: 'Caught' by intent filters
    
    Intents are parcelable
    
    **PendingIntents** for deferred firing: Way to say I need this data delt with, but hang onto the data and fire when you need to (useful for similar things to callbacks)
    
    May be broadcast by the system
    
    
* Providers: 

    Really "client libraries", encapsulate access to content providers and intents
    
    ContentProviders + Intents + Interface
    
    NOT the same thing as ContentProviders

* Activities: 

* Services: 

* ContentProviders: 
    
    Provide access to your app's data on request (similar to web services)
    
    Classes in andrid.content define, assist with high level protocol
    
    Tabular, no joins
    
    Can also provide InputStreams and OutputStreams, FileHandles, Pipes, etc.
    
    URI's (strings) can point to content providers
    
    **Operations:** 
    
        Encoded as URIs
        Client is ContentResolver or CursorLoader
        
        Query result is a cursor over rows
        
        inserts/updates are packed into ContentValues (sending something into a content providers, pack them into contentvalues)
        
        Batching mechanism - ContentProviderOperations
    
* RemoteViews: 

    "Web markup" essentially
    
    Declarative view definition
    
    Packages a layout with basic behavior
    
    "basic behavior" == PendingINtents for onCLick
    
    Helpful utility methods for common views

    
##Launcher

First big area of integration, not fully exploited

1. Shortcuts - anything intended for an intent can be wired to a shortcut

    Offer ways for users to place items on the launcher (static folder)

2. Live Folders

    Gets filled with data from the selected application
    
    Intent = CREATE_LIVE_FOLDER
    
    Display mode (icons, list, etc.)
    
    Base intent: fired when clicked on, can ovverride intent for individual items
    
    ContentProvider can "back" the live folder to provide the list of items that exist in that folder
    
    set of columns pre-defined for live folders that can be set
  
3. AppWidgets

    For frequently used controls within an application
    
    Have to be able to provide the remote view that gets created, register an AppWidgetProvider that's capable of receiving intents
    
        Update appWidget if new content needs to be displayed within the view
    
    Includes a configuration file for: screen real estate (minWidth, minHeight), refresh frequency (updatePeriodMillis), initialLayout
    
    AppWidgetProvider
    

##