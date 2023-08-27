---
layout: post
title: The new GIZMO-SIMBA clusters
gh-repo: weiguangcui/weiguangcui.github.io
gh-badge: [star, fork, follow]
tags: [astronomy, research-work]
cover-img: /assets/img/postimg/GIZMO-17-image.jpg
comments: false
comments_id: 3
---

Galaxy cluster, the largest number of galaxies assembled in the Universe, is the key laboratory for examinating many theories, from cosmology and dark matter to galaxy formation and intra-galactic medium. Therefore, theoretically understanding it and its formation has always in the central study of modern astronomy. However, numerical simulation is the only way to redisplay its detailed formation history. Limited by the current computation power, hydro-dynamically simulated galaxy clusters -- including all the baryons and the physical baryon processes -- are mostly simulated relying on the zoom-in simulation technique, with which only the targeted galaxy cluster is in the highest resolved region and the outer regions are replaced by low-resolution dark matter particles to represent the large-scale gravitation. [The Three Hundred project](https://the300-project.org) stands as a unique galaxy cluster project for these reasons:
1. it focuses on 324 mass-complete, the most massive galaxy clusters selected from the MDPL2 1Gpc/h cosmological simulation. 
2. instead of only simulate the galaxy cluster itself, the high-resolution zoom-in region has a radius of 15 Mpc/h, about 8 times of the cluster radius. This large surrounding region allows a study of the cluster formation environment.
3. instead of one single simulation code to perform the cluster simulation, Three Hundred project has three different simulation codes: GADGET-MUSIC[^1], GADGET-X[^2] and GIZMO-SIMBA[^3] (*This is the new run, Cui et al. 2022*) to simulate the same galaxy clusters. Benefited from the comparison, we can easily spot the simulated galaxy cluster differences and link these back to the models.

This GIZMO-SIMBA run is based on the SIMBA[^4] model developed by Prof Romeel Dave on top of the [GIZMO simulation code](http://www.tapir.caltech.edu/~phopkins/Site/GIZMO.html). Its unique BH accretion and feedback models with the successes in reproducing many galaxy properties, such as galaxy stellar mass function, galaxy colour bimodality[5], make it a distinctive contribution to The Three Hundred project. By further retuning the baryon model parameters to match these stellar properties in galaxy clusters: 
1. total stellar mass fraction within R_{500} -- f_{*, 500};
2. the brightest central galaxy (BCG) stellar mass -- halo mass relation;
3. the satellite stellar mass function,

we compared the GIZMO-SIMBA simulated galaxy clusters with the same clusters that simulated with GADGET-X. We found:
- Although a similar f_{*, 500} is found between GADGET-X and GIZMO-SIMBA, there are larger difference at higher redshift, thus its evolution. Moreover, the f_{gas, 500} has a clearly difference between GADGET-X and GIZMO-SIMBA at all redshifts, especially at low halo mass range, indicating a much strong AGN feedback in GIZMO-SIMBA than GADGET-X. 
- The BCG and satellite galaxy stellar masses from GIZMO-SIMBA are only slightly improved compared to GADGET-X. However, their colour-magnitude diagrams show better agreement with observation results.
- The BH scaling relations from GIZMO-SIMBA are also in very good agreement with observation results. It predicts higher black hole masses in the most massive galaxies, a shallower slope for the 𝑀_{BH}−𝜎_∗ at the low 𝜎_∗ end, and a shallower 𝑀_{BH}−𝑀_{500} relation at the more massive end.
- Though there are quite significant difference in the gas mass fraction between the two runs, their mock Y-M relations are surprisingly in agreement. It is because that GIZMO-SIMBA removes more gas content with its strong AGN feedback and boosts the gas temperature at the same time.

Written by Weiguang Cui, 2022-06-01
--------

[^1]: <span style="font-family:Papyrus; font-size:0.7em;"> Sembolini F., Yepes G., De Petris M., Gottl{\"o}ber S., Lamagna L., Comis B., 2013, MNRAS, 429, 323. [doi:10.1093/mnras/sts339](doi:10.1093/mnras/sts339) </span>
[^2]: <span style="font-family:Papyrus; font-size:0.7em;"> Rasia E., Borgani S., Murante G., Planelles S., Beck A.~M., Biffi V., Ragone-Figueroa C., et al., 2015, ApJL, 813, L17. [doi:10.1088/2041-8205/813/1/L17](doi:10.1088/2041-8205/813/1/L17) </span>
[^3]: <span style="font-family:Papyrus; font-size:0.7em;"> Cui W., Dave R., Knebe A., Rasia E., Gray M., Pearce F., Power C., et al., 2022, MNRAS.tmp. [doi:10.1093/mnras/stac1402](doi:10.1093/mnras/stac1402) </span>
[^4]: <span style="font-family:Papyrus; font-size:0.7em;"> Dav{\'e} R., Angl{\'e}s-Alc{\'a}zar D., Narayanan D., Li Q., Rafieferantsoa M.~H., Appleby S., 2019, MNRAS, 486, 2827. [doi:10.1093/mnras/stz937](doi:10.1093/mnras/stz937) </span>
