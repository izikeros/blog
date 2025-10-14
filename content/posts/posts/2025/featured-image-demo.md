Title: Featured Image Demo
Date: 2025-10-13 10:00
Category: Demo
Tags: pelican, theme, featured-image
Slug: featured-image-demo
Author: Krystian Safjan
Summary: A demonstration of the featured image functionality in the Safi theme
Image: https://picsum.photos/800/400?random=1
Image_alt: A beautiful demo image for testing featured images
Image_caption: This is a sample featured image from Lorem Picsum

# Featured Image Demo

This article demonstrates how featured images work with the Safi theme and the pelican-featured-image plugin.

## How Featured Images Work

The featured image plugin automatically extracts images from your articles and makes them available as `featured_image` in templates. This theme supports both manual `Image:` metadata and automatic extraction.

### Supported Image Formats

- JPEG
- PNG
- WebP
- SVG

### Template Variables Available

- `article.featured_image` - The image URL
- `article.featured_image_alt` - Alt text for the image
- `article.featured_image_caption` - Caption text (if available)

## Benefits

1. **SEO Enhancement** - Featured images are used in Open Graph and Twitter Card meta tags
2. **Visual Appeal** - Images make your articles more engaging in listings
3. **Automatic Processing** - No need to manually specify images in every template

## Example Usage

You can specify a featured image in your article metadata like this:

```markdown
Title: My Article
Date: 2025-10-13
Image: /images/my-featured-image.jpg
Image_alt: Description of the image
Image_caption: Caption for the image
```

The theme will automatically use this image in:
- Article pages (hero image)
- Article cards in listings
- Social media previews
- RSS feeds

## Testing

This article uses a random image from Lorem Picsum to demonstrate the functionality. You should see this image displayed prominently at the top of the article and in any article listings.