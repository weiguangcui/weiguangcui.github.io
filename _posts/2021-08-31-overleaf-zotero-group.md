---
layout: post
title: Output Zetero groups bibliography to Overleaf
tags: [Zetero] [Overleaf]
---

# The problem

After linking my zetero account to my overleaf account according to this (page)[https://libanswers.caltech.edu/faq/204206], you can only import the zetero library references to overleaf as a .bib file, not groups. 

# Solver

It can be done with the import from external weblink in overleaf:

Specified group settings:
Public: Closed Membership
Group Library: Anyone can view, only members can edit

You can hit the zotero api to fetch the bibfile for a group using something like this:

https://api.zotero.org/groups/2501167/items/top?format=bibtex&style=numeric&limit=100

Replace the group id: 2501167 with your own, finding the id is a bit obscure, click your group setting should be able to see it in the web address.

In overleaf when creating a new file you can specify an external url. Use the one above. For the name use something like "references.bib".

More discussions and details can be found at this page[https://forums.zotero.org/discussion/77185/how-to-link-zotero-private-group-with-overleaf]
