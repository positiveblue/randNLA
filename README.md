# RandNLA

### Introducction

**RandomizedNLA** is an implementation of many Randomized algorithms for Numerical Linear Algebra on top of Numpy/Scipy. 

Some of these methods are being implemented for [scipy](https://github.com/scipy/scipy/issues/7122)

## Motivation

**Randomized matrix algorithms** have been a hot topic in research the last years. Recent developments have shown their utility in large-scale machine learning and statistical data analysis applications.

Sketching is a way to compress matrices that preserve essential matrix properties. For some problems, sketches can be used to get faster ways to find high-precision solutions to the original problem. This tool can be used for least-squares and robust regression, eigenvector analysis, non-negative matrix factorization, etc...

The main idea of sketching matrices is not new. One of the most famous concepts behind the efficiency of random projection is the **Johnson-Lindenstrauss** lemma. It is used for random projections, and it has a "crude" [implementation in scikit-learn](http://scikit-learn.org/stable/modules/random_projection.html)

More recent work has been developed by [Kenneth Clarkson](http://researcher.watson.ibm.com/researcher/view.php?person=us-klclarks) and [David Woodruff](http://www.cs.cmu.edu/~dwoodruf/). In their paper [Low Rank Approximation and Regression in
Input Sparsity Time](https://arxiv.org/pdf/1207.6365.pdf) a new family of **subspace embedding** matrices are defined. They define in the same paper how those matrices can be used to obtain the fastest known algorithms for __overconstrained least-squares regression__, __low-rank approximation__, __approximating all leverage scores__, and __p-regression__.

During my time at IBM Research Almaden, I have been worked on a [xdata](http://www.darpa.mil/program/xdata) open source project for the last year called [libSkylark](https://xdata-skylark.github.io/libskylark/). The library is suitable for general statistical data analysis and optimization applications, but it is heavily focused on distributed systems. The quality of the project is high but it is not as developer friendly as I would like.


## Contributing

First off, thanks for taking the time to contribute! 

Now, take a moment to be sure your contributions make sense 
to everyone else and please make sure to read the [Contributing Guide](https://github.com/jomsdev/randomizedNLA/blob/CONTRIBUTING.md)
before making a pull request.

## Issue tracker

Found a problem? Want a new feature? First of all see if your issue or idea has [already been reported](../../issues).
If it hasn't, just open a [new clear and descriptive issue](../../issues/new).

## License
See the file LICENSE.txt for information on the history of this software, terms & conditions for usage, and a DISCLAIMER OF ALL WARRANTIES.
