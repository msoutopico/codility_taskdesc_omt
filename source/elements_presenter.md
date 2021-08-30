Model-View-Presenter with RxJava2 and Kotlin

You are implementing a screen in an app in which a list of elements is displayed.
Those elements are fetched from an external data source with RxJava `Single`:

```kotlin
interface ElementsProvider {
  fun loadElements(): Single<List<Element>>
}
```

where `Element` is a data class defined as follows:

```kotlin
data class Element(
    val id: String,
    val title: String
)
```

Your task is to implement `Presenter`, which will download the list of elements and display them on the screen. In the case of an error, you should display the error on the screen.
Loading data from an external source is considered a long-running operation, so you should also indicate loading progress with `showLoading()` and `hideLoading()` methods.

The view is defined by the following interface:
```kotlin
interface ListContract {
  interface View {
    fun setElements(elements: List<Element>)
    fun showLoading()
    fun hideLoading()
    fun showError()
  }
}
```

You can assume that:
* The view is always available;
* The view is never nullable.

Long-running operations should be executed on background threads, and view-related operations on the main thread.
`SchedulerFacade` is a layer of abstraction for RxJava2 and RxAndroid schedulers.
In the app they are implemented with `AndroidSchedulers.mainThread()` for `main` and `Schedulers.io()` for `background` threads.
Please do not use direct scheduler imports in your solution; use the method provided in `SchedulerFacade`.

Please implement `Presenter` to satisfy the following requirements:
* when `elementsProvider` emits data, set elements in the view;
* when `elementsProvider` emits an error, display the error in the view;
* when `elementsProvider` emits an empty list, display an error in the view;
* when the loading operation starts, show loading progress;
* when the loading operation ends, hide loading progress.
