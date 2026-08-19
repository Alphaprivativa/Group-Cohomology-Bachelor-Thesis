---
aliases:
- additive function on modules
---

# Additivity of length in a short exact sequence

> Let $0 \to M \xrightarrow{f} N \xrightarrow{g} K \to 0$ be a [[Short exact sequence]] of modules admitting [[Composition series]]. Then
> $$\ell(N) = \ell(M) + \ell(K)$$
>
> > [!dim]- #### Proof
> > Let $K = K_0 \supsetneq \ldots \supsetneq K_m = 0$ be a composition series for $K$ and $M = M_0 \supsetneq \ldots \supsetneq M_n = 0$ one for $M$. Glue them via $g$ and $f$:
> > $$g^{-1}(K_0) \supsetneq \ldots \supsetneq g^{-1}(K_m) = f(M_0) \supsetneq \ldots \supsetneq f(M_n)$$
> > using exactness at the center ($g^{-1}(0) = f(M)$). This is a maximal chain: extending it further to the right is impossible because $f$ is injective, so $(M_i)$ being a composition series forces the quotients $f(M_i)/f(M_{i+1})$ to have no nontrivial submodules; extending to the left is impossible because $(K_i)$ being a composition series, together with the correspondence between submodules of $N/f(M)$ and of $N$ containing $f(M)$ (via exactness on the right), forces the same for the $g^{-1}(K_i)/g^{-1}(K_{i+1})$. Hence it is a composition series of $N$ of length $m+n$, and by [[Chains extend to a composition series of the same length]] this is $\ell(N)$.

> [!idea]
> This is the special case, for $\lambda = \ell$, of the general notion of an ==additive function==: a map $\lambda$ from a class of $A$-modules to an abelian group $G$ such that $\lambda(N) - \lambda(M) + \lambda(K) = 0$ for every short exact sequence $0 \to M \to N \to K \to 0$. Any additive function $\lambda$ satisfies, for a longer exact sequence $0 \to M_n \to \ldots \to M_0 \to 0$,
> $$\sum_{i=0}^n (-1)^i \lambda(M_i) = 0$$
> by splitting it into short exact sequences with the images/kernels of the connecting maps and telescoping. This generalization is what makes the [[Poincaré series]] well behaved.
