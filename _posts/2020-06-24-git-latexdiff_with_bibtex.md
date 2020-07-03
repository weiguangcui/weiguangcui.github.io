---
layout: post
title: git-latexdiff run with bibtex
tags: [latex]
---

Runnning `git-latexdiff` with `-b`, for example:

`git latexdiff -b  4d075428e8511fb3e0424627316cf90773199e8e  origin/master --main paper.tex`

will encounter this problem:

```
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
```

To overcome this, you need to run:

`
git latexdiff  HEAD~1 --allow-space --bibtex --main paper.tex
`

---
Update on 03 July, 202:

Another problem happened when modification in the `\section` command:

```
! Argument of \UL@word has an extra }.
<inserted text> 
                \par 
l.350 ...begin \DIFadd{$z \simeq 5.7$}\DIFaddend }
                     \DIFaddbegin \label{subs:...
? 
! Emergency stop.
```

Fix by including `--exclude-textcmd="section,subsection"`:

`
git latexdiff HEAD~1 --allow-space --bibtex --exclude-textcmd="section,subsection" --main paper.tex
`