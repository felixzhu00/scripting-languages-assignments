# Assignment 2 - Advanced Python Programming Challenges

## Overview:
This assignment delves into advanced Python programming concepts, building upon the foundational skills developed in Assignment 1. Each challenge presented here is designed to deepen students' understanding of Python programming, covering topics such as regex manipulation, HTML parsing, and advanced text processing. By tackling these problems, students will sharpen their ability to solve complex programming tasks with efficiency and precision.

## Problem 1 - highlight(pattern, string)
Write a Python function named `highlight()`, which takes a raw string specifying a regex pattern as the first argument, called `pattern`, and a string as the second argument, called `string`. The function will compile `pattern` and apply the compiled pattern to `string`. If a match is found, then the function will return a string in which the matched substring of `string` is enclosed in angle brackets. If no match is found, the function should return `None`.

For example, suppose that:
```python
pattern = r'[a-zA-Z]\d'
string = "ShepardN7"
```
returns: `"Shepard<N7>"`

Test Cases:
```python
pattern = r'\bbook\B'
strings = ["bookstore", "booking", "textbooks", "'returned books'", "audiobook"]
```

## Problem 2 - highlight_all(pattern, string)
Write a Python function named `highlight_all()`. Like the `highlight()` function from Problem 1, this function will take a raw string, named `pattern`, and a target string, named `string`. This function will compile `pattern` and apply it to `string`. However, the `highlight_all()` function will return a string in which all substrings that match `pattern` will be enclosed in angle brackets. If there are no matches, then the function should return `None`.

For example, suppose that:
```python
pattern = r'o\w+'
string = "I'm Commander Shepard and this is my favorite store on the Citadel."
```
returns: `"I'm C<ommander> Shepard and this is my fav<orite> st<ore> <on> the Citadel."`

## Problem 3 - ruin_a_webpage(filename)
Write a Python function named `ruin_a_webpage()`. This function takes a single string argument named `filename`. `filename` will contain the name of an HTML file. Check the extension on the file using a regular expression. If the extension is not ".html" or ".htm", then the function should return `None`.
Otherwise, the function should read in the HTML file and do the following:

1. Use regular expressions to find content enclosed in paragraph tags, `<p>` and `</p>`, remove the paragraph tags, and then append 2 line break tags to the content, `<br><br>`
2. Remove all matched pairs of open and close span tags, `<span>` and `</span>`
3. Write the modified HTML content to a file called, "ruined.html"

For example, if the input file contains:
```html
<html>
<body>
<p>trees of green, red roses too</p>
<p>I <span><span>se</span></span>e them bloom for me and you</p>
<p>(what <span><span>a</span></span> <span><span>wonderful</span> </span>world)</p>
<p></p>
</body>
</html>
```
Then the output file, "ruined.html", should contain:
```html
<html>
<body>
trees of green, red roses too<br><br>
I see them bloom for me and you<br><br>
(what a wonderful world)<br><br>
<br><br>
</body>
</html>
```

## Problem 4 - decompose_path(path)
The shell environment variable $PATH contains a delimiter-separated sequence of directory paths (the delimiter varies between platforms). The shell uses the content of this variable to determine where to look for executables that correspond to commands entered at the command line. You can view this on Linux using the command: `echo $PATH` (using Windows CMD it's: `echo %PATH%`).

Write a function named `decompose_path()` that takes a single string argument, named `path`. `path` will contain the contents of the PATH environment variable as returned by the `echo $PATH` command. Use a regular expression to create a list of each directory in PATH. The function should return that list.

For example:
```python
path = "/usr/openwin/bin:/usr/ucb:/usr/bin:/bin:/etc:/usr/local/bin:/usr/local/lib:/usr/shareware/bin:/usr/shareware/lib:."
```
returns:
```python
["/usr/openwin/bin", "/usr/ucb", "/usr/bin", "/bin", "/etc", "/usr/local/bin", "/usr/local/lib", "/usr/shareware/bin", "/usr/shareware/lib", "."]
```

## Problem 5 - link_mapper(filename)
Write a Python function named `link_mapper()` which takes a single string argument, named `filename`. `filename` will be the name of an HTML file. Check that the extension is correct, as in Problem 3. The function should return `None` if the extension is not ".html" or ".htm".
Create a dictionary. Create an entry in the dictionary whose key is filename and whose value is an empty list.
Read in the HTML file and then use regular expressions to capture every hyperlink in the file. For each hyperlink, you should create a tuple of the link text and the link address (URL). For example, suppose the HTML file contains the following hyperlink definition:
```html
<a href="https://www.google.com">Search at Google</a>
```
You will create the following tuple:
```python
("Search at Google", "https://www.google.com")
```

## Additional Information
For detailed criteria and requirements for each problem, please refer to the assignment document [CSE337-S23-A02.pdf](CSE337-S23-A02.pdf).