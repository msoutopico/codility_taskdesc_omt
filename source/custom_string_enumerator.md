You work as a software developer and your goal is to implement a class called `CustomStringEnumerator` which will
encapsulate the logic responsible for filtering the collection of strings. Here is an example that shows how `CustomStringEnumerator` will be used:

```
var collection = new string[] { ... };
var config = new EnumeratorConfig
{
    MinLength = 3,
    MaxLength = 10,
    StartWithCapitalLetter = true
};

// The custom enumerator will return strings that are longer than or equal to 3 characters
// and shorter than or equal to 10 characters, and start with a capital letter.
var enumerator = new CustomStringEnumerator(collection, config);
foreach (var s in enumerator)
{
    Console.WriteLine(s);
}
```

`CustomStringEnumerator` can be used to enumerate any object that implements `IEnumerable<string>` interface. It must not
change the order of elements in the collection being enumerated. Assume that a `null` string is a
string of length 0. Under the hood, `CustomStringEnumerator` filters elements
of the collection according to the provided rules. These rules are specified in the `EnumeratorConfig` class.
`CustomStringEnumerator` should be defined as follows:

```
public class CustomStringEnumerator :  IEnumerable<string>
{
    /// <summary> Constructor </summary>
    /// <exception cref="System.ArgumentNullException">If a collection is null</exception>
    /// <exception cref="System.ArgumentNullException">If a config is null</exception>
    public CustomStringEnumerator(IEnumerable<string> collection, EnumeratorConfig config)
    {
        throw new NotImplementedException();
    }

    public IEnumerator<string> GetEnumerator()
    {
        throw new NotImplementedException();
    }

    IEnumerator IEnumerable.GetEnumerator()
    {
        throw new NotImplementedException();
    }
}
```

`EnumeratorConfig` class is as follows. You do not need to create or modify this class.
However, your implementation of `CustomStringEnumerator` should take into account all the properties of `EnumeratorConfig`:

```
public class EnumeratorConfig
{
    // Specifies the minimum length of strings that should be returned by a custom enumerator.
    // If it is set to a negative value then this option is ignored.
    public int MinLength { get; set; } = -1;

    // Specifies the maximum length of strings that should be returned by a custom enumerator.
    // If it is set to negative value then this option is ignored.
    public int MaxLength { get; set; } = -1;

    // Specifies that only strings that start with a capital letter should be returned by a custom enumerator.
    // Please note that empty or null strings do not meet this condition.
    public bool StartWithCapitalLetter { get; set; }

    // Specifies that only strings that start with a digit should be returned by a custom enumerator.
    // Please note that empty or null strings do not meet this condition.
    public bool StartWithDigit { get; set; }
}
```

Hint: An enumerator usually remains valid for as long as the collection remains unchanged. You do not have to implement this feature, i.e. you
do not have to detect changes to the collection.
