---
layout: post
title: git-latexdiff run with bibtex
tags: [latex]
---

Runnning `git-latexdiff` with `-b`, for example:

`git latexdiff -b  4d075428e8511fb3e0424627316cf90773199e8e  origin/master --main paper.tex`

will encounter this problem:
`
\AtBegShi@Output ...ipout \box \AtBeginShipoutBox 
                                                  \fi \fi 
l.519 \begin{thebibliography}{}
                               ]
! TeX capacity exceeded, sorry [input stack size=5000].
\hyper@normalise ->\begingroup \catcode `\^^M
                                             \active \def ^^M{ }\catcode `\%...
l.574 ...\mn@doi [\pasp] {\DIFadd{10.1086/376392}}
                                                  \DIFadd{, }\href
!  ==> Fatal error occurred, no output PDF file produced!

....
`

To overcome this, you need to run:

`
git latexdiff  HEAD~1 --allow-space --bibtex --main paper.tex
`
