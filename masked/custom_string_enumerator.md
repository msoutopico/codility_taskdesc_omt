An naw creates an enumeration, i.e. a numbered list. You work as a software developer and your goal is to create a class called Custom String naw which will
cover the logic responsible for filtering a collection of strings. Here is an example that shows how Custom String naw will be used:

   The custom enumerator will return strings that are longer than or equal to 3 characters
   and shorter than or equal to 10 characters, and start with a capital letter.
naw

Custom String naw can be used to enumerate any object that uses naw interface. It must not
change the order of elements in the collection being enumerated. Assume that a null string is a
string of length 0. Custom String naw filters elements
of the collection according to the provided rules. These rules are specified in the naw Config class.
Custom String naw should be defined as follows:

         Constructor 
        If a collection is null
        If a config is null
naw

naw Config class is as follows. You do not need to create or change this class.
However, your Custom String naw should take into account all the properties of naw Config:

       Specifies the minimum length of strings that should be returned by a custom enumerator.
       If it is set to a negative value then this option is ignored.
       Specifies the maximum length of strings that should be returned by a custom enumerator.
       If it is set to negative value then this option is ignored.
       Specifies that only strings that start with a capital letter should be returned by a custom enumerator.
       Please note that empty or null strings do not meet this condition.
       Specifies that only strings that start with a digit should be returned by a custom enumerator.
       Please note that empty or null strings do not meet this condition.
naw

Hint: An enumerator usually remains valid for as long as the collection remains unchanged. You do not have to create this feature. In other words, you
do not have to detect changes to the collection.
