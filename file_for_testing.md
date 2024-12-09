# Test Control File

This file is intended to serve as a control file for testing the Woodchipper Templating script. 

## Things to test

1. Opening and reading a [control file.md|control file].
2. Checking that extraction leaves just the [library/replacement text.md|replacement text].
3. Checking that extraction can have no [library/replacement text.md|replacement text].
4. Extraction of text into a [library/new/relative file.md|relative file] in the same directory.
5. Extraction of text into a [library/new/relative file.md|relative file] in a different directory.
6. Extraction of text into a [library/new/relative file.md|relative file] in a new directory.
7. Extraction of text overwriting a [library/new/relative file.md|relative file]. 
8. Extraction of text to a file with an [/home/osboxes/Documents/Code/woodchipper-templates/library/absolute path.md|absolute path] in an existing directory.
9. Extraction of text to a file with an [/home/osboxes/Documents/Code/woodchipper-templates/library/absolute path.md|absolute path] in a [/home/osboxes/Documents/Code/woodchipper-templates/library/new2/non-existent directory.md|non-existent directory].

## Setup 

> Todo

## Tests

### Test 1: Opening and Reading

This test is simple. Was this file read? This is easy to see if Verbosity is set to 3.

### Test 2: Replacement Text

Is the replacement text below? Note that this is also a test to make sure our script handles a token with no actual file extraction.

@{|Here is some replacement text.}{{}}

### Test 3: No Replacement Text

Make sure that there is only one empty line between this line and the next test header. Also notice that this covers testing for an empty token.
#{}{{}}
### Test 4: Same-Folder Extraction

This test should extract the text of [control file.md|#{control file.md|control file}{{
A control file is a file that includes tokens for controlling the Woodchipper Templating system. 
Tokens can be inserted anywhere in a file. They take the shape of "\@\{file_path|[library/replacement text.md|replacement_text]}{\{file_text}\}" without any of the \ characters.
}}] to its rightful place as a separate file in the working directory.

### Test 5: Different-Directory Extraction

For this test, we will be extracting the [library/replacement text.md|@{library/replacement text.md|replacement text}{{
Text that replaces the token when using the Woodchipper Templating script.
}}] file to `library/replacement text.md`.

### Test 6: New-Directory Extraction

The directory 'library/new' should be non-existent after setup of the tests. When we do the test below, it should create that directory and put the [library/new/relative file.md|relative file] markdown file inside of it.

@{library/new/relative file.md|Test Complete.}{{
A relative file is simply a file defined by a file path that is relative to the current working directory. 
}}

### Test 7: Overwriting Extraction

After setup, the library directory should have a file, `test.md`, which states "The test has not been run.". After this test @{library/test.md|has been completed}{{The test has been successfully completed.}}, it should be overwritten to reflect so.

### Test 8: Absolute Extraction
### Test 9: Absolute Extraction to a new Directory