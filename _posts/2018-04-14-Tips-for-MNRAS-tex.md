---
layout: post
title: Tips for MNRAS latex file format
tags: [latex, MNRAS]
---

1.  Wrapping the abstract to the second page

    To wrapping the abstract to the second page because of very long list of co-authors and affiliations, add `\clearpage` after the '\maketitle'.

2.  Including long list of authors

    ```latex
    \author[Cui et al.]{\parbox{\textwidth}{
    Weiguang Cui,$^{1}$\thanks{E-mail: weiguang.cui@uam.es}
    Long list authors \newline
    \emph{\normalsize Affiliations are listed at the end of the paper}
    }}
    ```
3.  For the Affiliations at the end of the paper, just go to the end of the paper and add a new section like this:

    ```latex
    \section*{Affiliations}
    \noindent
    {\it
    $^1$Departamento de F\'isica Te\'{o}rica, Universidad Aut\'{o}noma de Madrid, 28049 Madrid, Spain\\
    $^2$All the other addresses\\
    }
    ```
