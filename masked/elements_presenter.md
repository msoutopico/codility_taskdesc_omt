Model-View-Presenter with RxJava2 and Kotlin

You are creating a screen in an app in which a list of elements is displayed.
Those elements are returned from an outside data source with naw Single:

naw

where Element is a data class defined as follows:

naw

Your task is to create Presenter, which will download the list of elements and display them on the screen. If there is an error, you should display the error on the screen.
Loading data from an outside source is a long-running operation. So, you should also show loading progress with show Loading and hide Loading methods.

The view is defined by the following interface:
naw

You can assume that:
* The view is always available.
* The view is never set to null.

Long-running operations should be done on background threads. View-related operations should be done on the main thread.
Scheduler Facade is a layer of abstraction for RxJava2 and naw schedulers.
In the app they are created using naw naw main Thread for main threads and naw naw for background threads.
Please do not use direct scheduler imports in your solution. Use the method in Scheduler Facade.

Please create Presenter so that it meets the following requirements:
* when elements Provider returns data, set elements in the view.
* when elements Provider returns an error, display the error in the view.
* when elements Provider returns an empty list, display an error in the view.
* when loading starts, show loading progress.
* when loading ends, hide loading progress.
