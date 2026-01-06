---
Category: note
Date: 2024-08-01
Modified: 2024-08-01
Slug: rss-traffic-analysis-for-a-blog
Status: published
Summary: Learn how to track traffic from RSS/Atom feeds using UTM parameters, Google Analytics, dedicated feed analytics services, and server logs to gain insights into your blog's feed consumption.
ai_summary: true
Title: Rss Traffic Analysis for a Blog
tags:
  - rss
  - atom
  - analytics
  - traffic
  - traffic-sources
  - google-analytics
---
To track traffic coming from RSS/Atom feeds and gather information about your feed consumption, you can use a combination of Google Analytics and some additional methods. Here's how you can approach this:

1. **UTM parameters in RSS/Atom feed links:**
   Add UTM parameters to the links in your RSS/Atom feed. This will help you track traffic from feed readers in Google Analytics.

   Example:
   ```
   https://yourblog.com/post-title/?utm_source=rss&utm_medium=feed&utm_campaign=rss-feed
   ```

2. **Check Google Analytics:**
   - Go to Acquisition > All Traffic > Source/Medium
   - Look for entries with "rss" or "feed" in the source or medium
   - You can create a custom segment for RSS traffic to analyze it separately

3. **Use a feed analytics service:**
   Consider using a dedicated feed analytics service like [FeedPress](https://feedpress.com/) or [Feedburner](https://feedburner.google.com/) (discontinued).

4. **Check server logs:**
   If you have access to your server logs, look for user agents that typically belong to feed readers.

5. **Use a tracking pixel:**
   Include a small, invisible image ([tracking pixel](https://www.digitalmarketer.com/blog/what-is-tracking-pixel/)) in your feed items. Each time the image is loaded, it can be counted as a feed view.

6. **Implement RSS-to-Email:**
   Services like [Mailchimp](https://mailchimp.com/) offer RSS-to-Email, which can provide insights into how many subscribers are engaging with your content.

7. **Check feed aggregators:**
   Some popular feed aggregators like [Feedly](https://feedly.com/) provide public subscriber counts.

8. **Implement a custom tracking solution:**
   You could create a proxy for your RSS feed that logs requests before serving the actual feed content.

> NOTE: Tracking RSS usage is not always straightforward, as many feed readers cache content and may not load images or execute JavaScript. The methods above will give you an approximation rather than exact numbers.
