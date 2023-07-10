# QUBO_SA
2023 Telluride Workshop, exploring the simulated annealing algorithm for general QUBO problems

The repo includes a simulated annealing algorithm for max-cut proposed by Myklebust, T G J, in https://arxiv.org/abs/1505.03068 

The simulated annealing algorithm minimizes the energy function x.TQx, where Q is an upper triangular matrix

To install, in the directory, run
```
pip install -e .
```
Examples of usage are contained in the "test" folder
