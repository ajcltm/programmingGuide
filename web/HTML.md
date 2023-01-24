### Basic HTML structure
---
~~~html
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- google font -->
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <!-- css style sheet -->
    <link rel="stylesheet" href="./filter.css">
    <title>Filter Project</title>
</head>
<body>
  <!-- javascript -->
   <script src="./filter.js"></script>
</body>
</html>
~~~

### HTML Element Reference - By Category
---
- Basic HTML

Tag|	Description
---|---
\<!DOCTYPE>| 	Defines the document type
\<html>|	Defines an HTML document
\<head>|	Contains metadata/information for the document
\<title>|	Defines a title for the document
\<body>|	Defines the document's body
\<h1> to <h6>|	Defines HTML headings
\<p>|	Defines a paragraph
\<br>|	Inserts a single line break
\<hr>|	Defines a thematic change in the content
\<!--...-->|	Defines a comment
<br>

- Formatting

Tag|	Description
---|---
\<acronym>|	Not supported in HTML5. Use <abbr> instead. Defines an acronym
\<abbr>|	Defines an abbreviation or an acronym
\<address>|	Defines contact information for the author/owner of a document/article
\<b>|	Defines bold text
\<bdi>|	Isolates a part of text that might be formatted in a different direction from other text outside it
\<bdo>|	Overrides the current text direction
\<big>|	Not supported in HTML5. Use CSS instead. Defines big text
\<blockquote>|	Defines a section that is quoted from another source
\<center>|	Not supported in HTML5. Use CSS instead. Defines centered text
\<cite>|	Defines the title of a work
\<code>|	Defines a piece of computer code
\<del>|	Defines text that has been deleted from a document
\<dfn>|	Specifies a term that is going to be defined within the content
\<em>|	Defines emphasized text 
\<font>|	Not supported in HTML5. Use CSS instead. Defines font, color, and size for text
\<i>|	Defines a part of text in an alternate voice or mood
\<ins>|	Defines a text that has been inserted into a document
\<kbd>|	Defines keyboard input
\<mark>|	Defines marked/highlighted text
\<meter>|	Defines a scalar measurement within a known range (a gauge)
\<pre>|	Defines preformatted text
\<progress>|	Represents the progress of a task
\<q>|	Defines a short quotation
\<rp>|	Defines what to show in browsers that do not support ruby annotations
\<rt>|	Defines an explanation/pronunciation of characters (for East Asian typography)
\<ruby>|	Defines a ruby annotation (for East Asian typography)
\<s>|	Defines text that is no longer correct
\<samp>|	Defines sample output from a computer program
\<small>|	Defines smaller text
\<strike>|	Not supported in HTML5. Use <del> or <s> instead. Defines strikethrough text
\<strong>|	Defines important text
\<sub>|	Defines subscripted text
\<sup>|	Defines superscripted text
\<template>|	Defines a container for content that should be hidden when the page loads
\<time>|	Defines a specific time (or datetime)
\<tt>|	Not supported in HTML5. Use CSS instead. Defines teletype text
\<u>|	Defines some text that is unarticulated and styled differently from normal text
\<var>|	Defines a variable
\<wbr>|	Defines a possible line-break
<br>

- Forms and Input

Tag|	Description
---|---
\<form>|	Defines an HTML form for user input
\<input>|	Defines an input control
\<textarea>|	Defines a multiline input control (text area)
\<button>|	Defines a clickable button
\<select>|	Defines a drop-down list
\<optgroup>|	Defines a group of related options in a drop-down list
\<option>|	Defines an option in a drop-down list
\<label>|	Defines a label for an \<input> element
\<fieldset>|	Groups related elements in a form
\<legend>|	Defines a caption for a \<fieldset> element
\<datalist>|	Specifies a list of pre-defined options for input controls
\<output>|	Defines the result of a calculation
<br>

- Frames

Tag|	Description
---|---
\<frame>|	Not supported in HTML5. Defines a window (a frame) in a frameset
\<frameset>|	Not supported in HTML5. Defines a set of frames
\<noframes>|	Not supported in HTML5. Defines an alternate content for users that do not support frames
\<iframe>|	Defines an inline frame
<br>

- Images

Tag|	Description
---|---
\<img>|	Defines an image
\<map>|	Defines a client-side image map
\<area>|	Defines an area inside an image map
\<canvas>|	Used to draw graphics, on the fly, via scripting (usually JavaScript)
\<figcaption>|	Defines a caption for a \<figure> element
\<figure>|	Specifies self-contained content
\<picture>|	Defines a container for multiple image resources
\<svg>|	Defines a container for SVG graphics
<br>

- Audio / Video

Tag|	Description
---|---
\<audio>|	Defines sound content
\<source>|	Defines multiple media resources for media elements (\<video>, \<audio> and \<picture>)
\<track>|	Defines text tracks for media elements (\<video> and \<audio>)
\<video>|	Defines a video or movie
<br>

- Links

Tag|	Description
---|---
\<a>|	Defines a hyperlink
\<link>|	Defines the relationship between a document and an external resource (most used to link to style sheets)
\<nav>|	Defines navigation links
<br>

- Lists

Tag|	Description
---|---
\<ul>|	Defines an unordered list
\<ol>|	Defines an ordered list
\<li>|	Defines a list item
\<dir>|	Not supported in HTML5. Use \<ul> instead. Defines a directory list
\<dl>|	Defines a description list
\<dt>|	Defines a term/name in a description list
\<dd>|	Defines a description of a term/name in a description list
<br>

- Tables

Tag|	Description
---|---
\<tablev>|	Defines a table
\<caption>|	Defines a table caption
\<th>|	Defines a header cell in a table
\<tr>|	Defines a row in a table
\<td>|	Defines a cell in a table
\<thead>|	Groups the header content in a table
\<tbody>|	Groups the body content in a table
\<tfoot>|	Groups the footer content in a table
\<col>|	Specifies column properties for each column within a <colgroup> element
\<colgroup>|	Specifies a group of one or more columns in a table for formatting
<br>

- Styles and Semantics

Tag|	Description
---|---
\<style>|	Defines style information for a document
\<div>|	Defines a section in a document
\<span>|	Defines a section in a document
\<header>|	Defines a header for a document or section
\<footer>|	Defines a footer for a document or section
\<main>|	Specifies the main content of a document
\<section>|	Defines a section in a document
\<article>|	Defines an article
\<aside>|	Defines content aside from the page content
\<details>|	Defines additional details that the user can view or hide
\<dialog>|	Defines a dialog box or window
\<summary>|	Defines a visible heading for a \<details> element
\<data>|	Adds a machine-readable translation of a given content
<br>

- Meta Info

Tag|	Description
---|---
\<head>|	Defines information about the document
\<meta>|	Defines metadata about an HTML document
\<base>|	Specifies the base URL/target for all relative URLs in a document
\<basefont>|	Not supported in HTML5. Use CSS instead. Specifies a default color, size, and font for all text in a document
<br>

- Programming

Tag|	Description
---|---
\<script>|	Defines a client-side script
\<noscript>|	Defines an alternate content for users that do not support client-side scripts
\<applet>|	Not supported in HTML5. Use \<embed> or \<object> instead. Defines an embedded applet
\<embed>|	Defines a container for an external (non-HTML) application
\<object>|	Defines an embedded object
\<param>|	Defines a parameter for an object
<br>

#### **The \<input> Element**
---

Type|	Description
---|---
\<input type="text">|	Displays a single-line text input field
\<input type="radio">|	Displays a radio button (for selecting one of many choices)
\<input type="checkbox">|	Displays a checkbox (for selecting zero or more of many choices)
\<input type="submit">|	Displays a submit button (for submitting the form)
\<input type="button">|	Displays a clickable button
<br>

- Text Fields
~~~html
<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname">
</form>
~~~

- Radio Buttons
~~~HTML
<p>Choose your favorite Web language:</p>

<form>
  <input type="radio" id="html" name="fav_language" value="HTML">
  <label for="html">HTML</label><br>
  <input type="radio" id="css" name="fav_language" value="CSS">
  <label for="css">CSS</label><br>
  <input type="radio" id="javascript" name="fav_language" value="JavaScript">
  <label for="javascript">JavaScript</label>
</form>
~~~

- Checkboxes
~~~html
<form>
  <input type="checkbox" id="vehicle1" name="vehicle1" value="Bike">
  <label for="vehicle1"> I have a bike</label><br>
  <input type="checkbox" id="vehicle2" name="vehicle2" value="Car">
  <label for="vehicle2"> I have a car</label><br>
  <input type="checkbox" id="vehicle3" name="vehicle3" value="Boat">
  <label for="vehicle3"> I have a boat</label>
</form>
~~~

- The Submit Button
    - Notice that each input field must have a name attribute to be submitted.
    - If the name attribute is omitted, the value of the input field will not be sent at all.
~~~html
<form action="/action_page.php">
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value="John"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe"><br><br>
  <input type="submit" value="Submit">
</form>
~~~

- table
~~~html
<table>
  <tr>
    <th>First Name</th>
    <th>Last Name</th>
    <th>Points</th>
  </tr>
  <tr>
    <td>Peter</td>
    <td>Griffin</td>
    <td>$100</td>
  </tr>
  <tr>
    <td>Lois</td>
    <td>Griffin</td>
    <td>$150</td>
  </tr>
  <tr>
    <td>Joe</td>
    <td>Swanson</td>
    <td>$300</td>
  </tr>
  <tr>
    <td>Cleveland</td>
    <td>Brown</td>
    <td>$250</td>
  </tr>
</table>
~~~

