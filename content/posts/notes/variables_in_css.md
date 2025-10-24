---
Title: Using CSS Variables for Dynamic and Reusable Styling  
Slug: css-variables-dynamic-reusable-styling  
Date: 2025-10-14  
Modified: 2025-10-14  
Status: published  
tags: 
 - css
 - web-development
 - front-end
Category: note  
---

## The Core Idea

CSS variables (custom properties) let you store reusable values directly in CSS and update them at runtime.  
They use the `--name` syntax and are accessed with `var()`:

```css
:root {
  --bg: #222;
  --text: #eee;
}

body {
  background: var(--bg);
  color: var(--text);
}
````

Variables defined in `:root` are global but can be overridden in specific scopes or components.

## Practical Usage

### Where It Shines

- **Dynamic theming:** dark/light mode, high-contrast themes, seasonal designs.   
- **Design consistency:** same color or spacing reused across multiple components.
- **Runtime manipulation:** interactive UIs where JS can tweak design parameters instantly.
- **Design systems:** variables act as a shared language between designers and developers.

### When Not to Use It

- **Heavy preprocessing needs:** if you rely on loops, conditionals, or functions like `darken()`—Sass still wins there.
    
- **Older browser support:** IE11 doesn’t support CSS variables (and never will).

### Example: color picker that changes page color live

An example of a simple color picker that changes page color live:
```js
<input type="color" id="picker">
<script>
  const picker = document.getElementById('picker');
  picker.addEventListener('input', e => {
    document.documentElement.style.setProperty('--main-bg', e.target.value);
  });
</script>
```

### Example: Theming

```css
:root {
  --bg: #fff;
  --text: #000;
}
.dark {
  --bg: #121212;
  --text: #fff;
}
```

Switch themes easily:

```js
document.body.classList.toggle('dark');
```

### Fallbacks and Responsiveness

```css
h1 {
  color: var(--title-color, #444); /* fallback if missing */
}

@media (min-width: 800px) {
  :root {
    --gap: 2rem;
  }
}
```


## Things to Watch Out For

- **Scoped variables** don’t leak outside their selector
- **IE11** doesn’t support them
- Changing variables with JS triggers **repaints**, so avoid in animations

CSS variables behave like live, inheritable properties—perfect for theming and dynamic UI tweaks without recompiling styles.