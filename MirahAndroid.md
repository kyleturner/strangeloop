#Mirah for Android Development - Brendan Ribera

@abscondment - brendan.ribera@gmail.com

http://threebrothers.org/brendan

https://github.com/abscondment/mirah-guide

http://www.mirah.org

##What is Mirah?

An island of Java - Javanese for "Ruby"

* Ruby-like syntax, JVM bytecode (compiled)
* No runtime dependencies
* Type inference

A quick example…

```
class Messenger
    def initialize(m:String)
        @message = m
    end
    
    def message
        @message
    end
end
```

A contrived example...

```
class StrangeHello < Messenger
    def initialize
        super 'Strange Loop'
    end
    
    def message
        "Hello, #{super}!"
    end
end
```

* No abstract classes


##Why Use Mirah On Android?

Alternatives:

* Scala
* Jruby/Ruboto
* Clojure
* Groovy/Jthon/Lua/Others

Benefits: 

* Practical decision: no runtime dependencies or performance penalties
* Fewer type declarations
* Expressive: blocks, macros, etc.

##Blocks

If there is only one method to implement within the interface, it would look something like this:

Java Code: 

```
this.closeButton.setOnClickListener(new OnClickListener() {
    @Override
    public void onClick(View v) {
        finish();
    }
});
```

Ruby Code: 

```
this = self
@close_btn.setOnClickListener do |v|
    this.finish
end
```


##Macros

Compile time function to call when compiler runs


##Showtime

1. Get Android
2. Get Mirah
    rvm install jruby
    rvm jruby
    gem install mirah
    gem install pindah - build tool (typically use master branch on GitHub) http://github.com/mirah/pindah

_First, we'll touch on the "mixed source" (an existing Java app):_

**mirahc can't compile Java sources, so treat one portion of codebase like a library so one gets compiled first (soon to be fixed)**

_Pure Mirah:_

Uses Pindah: Works via rake to generate build files and run them

```pindah create org.example.hello [/path/to/hello_world] [HelloActivity]```

Rakefile

```require "rubygems"
require "pindah"

Pindah.spec = {
    :name => "mirah-guide",
    :target_version => "2.2"
}
```

rake -T

* rake clean
* rake compile
* rake debug
* rake install
* rake javac
* rake logcat
* rake release
etc...

**Checkout the github mirah example project, and run ```git tag -l``` to see steps throughout development process**
