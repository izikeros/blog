---
Title: HTML5 interactive elements
Slug: html5-interactive-elements
Date: 2024-01-04
Modified: 2024-01-04
Status: published
tags: html5
Category: note
---

# HTML5 Interactive Elements: An Overview and Usage Guide

HyperText Markup Language (HTML) is the standard markup language for documents designed to be rendered in a web browser. Over the years, HTML has evolved to keep up with the growing need for better structure and interactivity. 

HTML5, the latest version, introduces several interactive tags or elements, which makes building interactive, dynamic web content easier without having to resort to JavaScript or CSS. Let's dive into these interactive elements and have a look at some examples to understand their usage better.

## The `<details>` and `<summary>` Elements 

The `<details>` and `<summary>` tags allow us to create an interactive widget that the user can open or close. The `<summary>` tag is a child of the `<details>` tag, representing the summary or brief description of the content in `<details>`.

```html
<details>
    <summary>The Solar System</summary>
    <p>The Solar System includes the Sun, the Earth (where you are now!) and all the other planets.</p>
</details>
```

<details>
    <summary>The Solar System</summary>
    <p>The Solar System includes the Sun, the Earth (where you are now!) and all the other planets.</p>
</details>

## The `<dialog>` Element

The `<dialog>` element presents content in a dialogue box or a window. You can toggle the visibility of the `<dialog>` by changing the 'open' attribute.

```html
<dialog open>
    This is a dialog box!<br>
    <button onclick="this.parentElement.close()">Close</button>
</dialog>
```

<dialog open>
    This is a dialog box!<br>
    <button onclick="this.parentElement.close()">Close</button>
</dialog>

## The `<datalist>` Element

The `<datalist>` element permits the creation of pre-defined options for an `<input>` element. User can either select an option or type in their input.

```html
<label for="browsers">Choose a browser from the list:</label>
<input list="browsers" name="browser" id="browser">
<datalist id="browsers">
  <option value="Chrome">
  <option value="Firefox">
  <option value="Internet Explorer">
  <option value="Opera">
  <option value="Safari">
</datalist>
```

<label for="browsers">Choose a browser from the list:</label>
<input list="browsers" name="browser" id="browser">
<datalist id="browsers">
  <option value="Chrome">
  <option value="Firefox">
  <option value="Internet Explorer">
  <option value="Opera">
  <option value="Safari">
</datalist>

## The `<progress>` Element

The `<progress>` element serves to represent the progress of a task. Use the `value` attribute to specify the current progress and the `max` attribute to indicate the progress bar's maximum value.

```html
<progress value="70" max="100"></progress>
```

<progress value="70" max="100"></progress>

## The `<meter>` Element

The `<meter>` tag is used to represent the scalar measurement within a known range, or a fractional value. This could be the disk usage, the relevance of a query result or any other form of gauge.

```html
Disk usage: <meter value="0.6">60%</meter>
```

Disk usage: <meter value="0.6">60%</meter>

## The `<output>` Element

The `<output>` tag is a container for calculation results. To link the output element with other elements, you can use the `for` attribute. 

```html
<form oninput="x.value=parseInt(a.value)+parseInt(b.value)">
  0<input type="range" id="a" value="50">100 +
  0<input type="range" id="b" value="50">100 =
  <output name="x" for="a b"></output>
</form>
```

<form oninput="x.value=parseInt(a.value)+parseInt(b.value)">
  0<input type="range" id="a" value="50">100 +
  0<input type="range" id="b" value="50">100 =
  <output name="x" for="a b"></output>
</form>

## The `<canvas>` Element

The `<canvas>` tag allows for dynamic and scriptable rendering of shapes and bitmap images. It's a low-level, procedural model that updates a bitmap.

```html
<canvas id="myCanvas" width="200" height="100" style="border:1px solid #000000;">
</canvas>
```



You can then use JavaScript to interact with this element:

```javascript
var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
ctx.fillStyle = "#FF0000";
ctx.fillRect(0, 0, 80, 80);
```
<canvas id="myCanvas" width="200" height="100" style="border:1px solid #000000;">
</canvas>
<script>
var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
ctx.fillStyle = "#FF0000";
ctx.fillRect(0, 0, 80, 80);
</script>

