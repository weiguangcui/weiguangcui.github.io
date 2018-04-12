---
layout: post
title: A Wrapper for changing from numerical recipes fft to FFTW3
tags: [c, fftw3]
---

Remember to link the library with ``-lfftw3` in your Makefile.

Here is the function:

```c
#include <fftw3.h>

void fourn(flouble data[], unsigned long nn[], int ndim, int isign)
{
    int i,j,k, *NN;
    unsigned long Ntot=1;
    fftw_plan p1_FFTW;

    NN=malloc(sizeof(int)*ndim);

    for (i=1; i<=ndim; i++)
    {
      Ntot *= nn[i];
      NN[i-1] = nn[i];
    }

    fftw_complex* b1=fftw_malloc(sizeof(fftw_complex)*Ntot);
    fftw_complex* b2=fftw_malloc(sizeof(fftw_complex)*Ntot);

    for (i=0; i < Ntot; i++)
    {
      b1[i][0] =  data[2*i+1];
      b1[i][1] = -data[2*i+2];
    }

    if (isign ==  1)        /* FFT             */
      p1_FFTW=fftw_plan_dft(ndim, NN, b1, b2, FFTW_FORWARD, FFTW_ESTIMATE);

    if (isign == -1)       /* IFFT scale by n */
      p1_FFTW=fftw_plan_dft(ndim, NN, b1, b2, FFTW_BACKWARD, FFTW_ESTIMATE);

    fftw_execute(p1_FFTW);

    for (i=0; i < Ntot; i++)
      {
        data[2*i+1] =  b2[i][0];
        data[2*i+2] = -b2[i][1];
      }

    /* **** Fee memory   **************************/
    fftw_free(b1);
    fftw_free(b2);
    fftw_destroy_plan(p1_FFTW);
}
```

See this [page](http://hep.ph.liv.ac.uk/~hock/My_reports/fftw/readme0.html) if you want to have the wrapper for four1.c.
