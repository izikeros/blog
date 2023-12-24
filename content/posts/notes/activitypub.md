---
Category: note
Date: '2023-03-06'
Modified: '2023-07-12'
Prompt: Give me long blog post on ActivityPub with examples how you can use it in your apps.
Slug: activitypub-how-it-works-how-to-use-it
Status: published
Tags: activitypub, social-networking, federated-social-web, rss, gitea, xmpp
Title: ActivityPub - How It Works and How to Use It?
---

ActivityPub is a protocol designed to enable decentralized social networking. It is based on the principles of the ***Federated Social Web***, which aims to create a social web that is not owned by any single entity or corporation. In this blog post, we will explore the basics of ActivityPub and how it can be used in your applications.

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [What is ActivityPub?](#what-is-activitypub)
- [How does ActivityPub work?](#how-does-activitypub-work)
- [How can ActivityPub be used in your applications?](#how-can-activitypub-be-used-in-your-applications)
 	- [1.  Social Networking Platforms](#1-social-networking-platforms)
 	- [2.  Chat Applications](#2-chat-applications)
 	- [3.  Content Management Systems](#3-content-management-systems)
 	- [4.  Collaboration Tools](#4-collaboration-tools)
- [Other,  related protocols](#other-related-protocols)
 	- [1.  OStatus](#1-ostatus)
 	- [2.  WebSub \(formerly known as PubSubHubbub\)](#2-websub-formerly-known-as-pubsubhubbub)
 	- [3.  Diaspora](#3-diaspora)
 	- [4.  Zot](#4-zot)
 	- [5.  Matrix](#5-matrix)
- [Conclusion](#conclusion)
- [References](#references)

<!-- /MarkdownTOC -->

<a id="what-is-activitypub"></a>

## What is ActivityPub?

ActivityPub is a decentralized protocol for social networking. It allows users to interact with each other across different social networking platforms, without having to be part of the same network. ActivityPub is designed to be scalable, secure, and decentralized, and it allows users to control their own data and content.

The core of ActivityPub is the activity stream. An activity stream is a list of actions that a user has taken or received, such as posting a message, following someone, or liking a post. ActivityPub uses the JSON-LD format to represent activity streams.

<a id="how-does-activitypub-work"></a>

## How does ActivityPub work?

ActivityPub is based on a decentralized architecture, which means that there is no single central authority that controls the network. Instead, each user has their own server, known as a "node," which is responsible for storing their data and communicating with other nodes.

When a user wants to post a message or perform any other activity, their node creates an activity object, which contains information about the activity, such as the type of activity, the user who performed it, and any additional metadata. The activity object is then sent to the user's followers, who receive a notification of the activity.

If a user wants to follow another user, their node sends a follow request to the other user's node. If the other user accepts the request, their node sends a follow activity to the follower's node, which adds the user to their list of followers.

ActivityPub also supports other types of activities, such as likes, shares, and comments. These activities are all represented using the same activity object format.

![ActivityPub](/images/misc/ActivityPub.png)
*How ActivityPub works (source: W3C)*

<a id="how-can-activitypub-be-used-in-your-applications"></a>

## How can ActivityPub be used in your applications?

ActivityPub can be used in a wide variety of applications, from social networking platforms to chat applications to content management systems. Here are some examples of how ActivityPub can be used in your applications:

<a id="1-social-networking-platforms"></a>

### 1.  Social Networking Platforms

ActivityPub can be used to create decentralized social networking platforms, where users can connect with each other across different networks. For example, Mastodon is a popular social networking platform that uses ActivityPub. Mastodon allows users to post messages, follow other users, and interact with each other in a decentralized manner.

<a id="2-chat-applications"></a>

### 2.  Chat Applications

ActivityPub can also be used to create decentralized chat applications. For example, XMPP is a protocol for instant messaging that supports ActivityPub. XMPP allows users to send messages, share files, and interact with each other in real-time.

<a id="3-content-management-systems"></a>

### 3.  Content Management Systems

ActivityPub can be used to create decentralized content management systems, where users can publish and share content across different networks. For example, Write.as is a blogging platform that uses ActivityPub. Write.as allows users to publish blog posts, follow other bloggers, and interact with each other in a decentralized manner.

<a id="4-collaboration-tools"></a>

### 4.  Collaboration Tools

ActivityPub can be used to create decentralized collaboration tools, where users can work together on projects across different networks. For example, Gitea is a platform for hosting and managing Git repositories that supports ActivityPub. Gitea allows users to collaborate on projects, share code, and interact with each other in a decentralized manner.

<a id="other-related-protocols"></a>

## Other,  related protocols

ActivityPub is just one of several protocols that are designed to support decentralized communication and social networking. Here are some of the related protocols:

<a id="1-ostatus"></a>

### 1.  OStatus

OStatus is an older protocol that was developed before ActivityPub. It includes several components, including ActivityStreams, WebSub, and Salmon. OStatus was originally used for federated microblogging platforms like StatusNet and GNU Social.

**OStatus**: [https://www.w3.org/community/ostatus/wiki/Main_Page](https://www.w3.org/community/ostatus/wiki/Main_Page)

<a id="2-websub-formerly-known-as-pubsubhubbub"></a>

### 2.  WebSub (formerly known as PubSubHubbub)

WebSub is a protocol for real-time notifications on the web. It allows publishers to notify subscribers when new content is available, and it is used by ActivityPub to send notifications of new activities.

**WebSub**: [https://www.w3.org/TR/websub/](https://www.w3.org/TR/websub/)

<a id="3-diaspora"></a>

### 3.  Diaspora

Diaspora is a social networking platform that uses a protocol called the Diaspora protocol. The Diaspora protocol is similar to ActivityPub, but it was designed specifically for the Diaspora platform.

**Diaspora protocol:** [https://diaspora.github.io/diaspora_federation/protocol.html](https://diaspora.github.io/diaspora_federation/protocol.html)

<a id="4-zot"></a>

### 4.  Zot

Zot is a protocol used by the Hubzilla social networking platform. Zot is similar to ActivityPub, but it includes additional features like encryption and private messaging.

**Zot**: [https://zotlabs.org/page/zot/zot-protocol](https://zotlabs.org/page/zot/zot-protocol)
<a id="5-matrix"></a>

### 5.  Matrix

Matrix is a decentralized communication protocol that is designed for real-time messaging and collaboration. It includes features like end-to-end encryption, multi-device syncing, and bridging to other networks like IRC and Slack.

These protocols are all part of the wider ecosystem of decentralized communication and social networking. While they have their own unique features and use cases, they all share a common goal of enabling users to communicate and collaborate in a decentralized, open, and transparent way.

**Matrix**: [https://matrix.org/docs/spec/](https://matrix.org/docs/spec/)
<a id="conclusion"></a>

## Conclusion

ActivityPub is a powerful protocol that enables decentralized social networking. It allows users to interact with each other across different networks, without having to be part of the same network. ActivityPub can be used in a wide variety of applications, from social networking platforms to content management systems to collaboration tools. If you are interested in creating decentralized applications, ActivityPub is definitely worth

See the video: [How To Use ActivityPub In Your Applications? - YouTube](https://www.youtube.com/watch?v=kkvJMiiVRWs)

<a id="references"></a>

## References

links to the protocols mentioned in this chat:

1. ActivityPub: [https://www.w3.org/TR/activitypub/](https://www.w3.org/TR/activitypub/)
2. OStatus: [https://www.w3.org/community/ostatus/wiki/Main_Page](https://www.w3.org/community/ostatus/wiki/Main_Page)
3. WebSub: [https://www.w3.org/TR/websub/](https://www.w3.org/TR/websub/)
4. Diaspora protocol: [https://diaspora.github.io/diaspora_federation/protocol.html](https://diaspora.github.io/diaspora_federation/protocol.html)
5. Zot: [https://zotlabs.org/page/zot/zot-protocol](https://zotlabs.org/page/zot/zot-protocol)
6. Matrix: [https://matrix.org/docs/spec/](https://matrix.org/docs/spec/)
