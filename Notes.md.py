##Testing, Testing, iOS

Heath Borders - @heathborders @asyncrhony AtlandAndFuller

https://github.com/hborders/StlMobileDev/iPhone-Testing

https://github.com/hborders/iphonesim

* OCUnit
* Google Toolbox for Mac
* GHUnit
* UISpec
* UIAutomation


------


##OCUnit

#Unit Tests

* Need different targets and platforms for Unit tests and Integration tests
* Extend SenTestCase
* -(void)testMyNameHere(){}
* STAssertEquals (scalar values)
* STAssertEqualsWithAccuracy (comparing two doubles)
* STAssertEqualObjects (compare two objects)

For JUnit style output:

* http://github.com/hborders/BPOCUnitXMLReporter

#Integration Tests

* Integration tests do not integrate into xcode, only show failures in the console


------


##GoogleToolbox for the Mac
* need a separate test target
* extend GTMTestCase
* assertions compatible with OCUnit
* STAssertEqualStrings ()

Running

* Tests run in both simulator and command line!  Integration tests only run in command line.

Error Reporting

* Does not have JUnit style reports

Debugging

* Disable 'Run Script' build phase (if you don't, your build will fail and won't be able to debug!)


------


##**GHUnit**

Docs are great
Use GHUnitIOSAppDelegate

* Need a separate test app target
* Tests run in separte app

Running

* Tests can run on simulator and device, run inside test app - EXCEPT: can't use UIApplicationDelegate's shared instance!
* Doesn't propertly catch unexpected exceptions

Error Reporting

* Can write in JUnit format (WRITE_JUNIT_XML=YES)


------


##UISpec


##UIAutomation

* New to XCode4
* 


