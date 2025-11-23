# Vertex Cover com Algoritmo Guloso

Este repositório contém a implementação de um algoritmo **guloso (Greedy)** para encontrar uma **Cobertura de Vértices** em um grafo. O projeto foi desenvolvido como parte do estudo do Problema da Cobertura de Vértices, um tema clássico em Projeto e Análise de Algoritmos (PAA).

---

## Sobre o Problema

Uma **Cobertura de Vértices (Vertex Cover)** é um conjunto de vértices tal que **todas as arestas do grafo possuem pelo menos um de seus extremos** dentro desse conjunto.

Em termos simples:  
> Escolher os menores pontos possíveis do grafo que “tocam” todas as conexões.

O problema é **NP-completo**, ou seja, não existe algoritmo conhecido em tempo polinomial que encontre sempre a solução ótima para qualquer grafo.

---

## Estratégia Implementada — Técnica Gulosa

O algoritmo guloso adotado segue a seguinte lógica:

1. Enquanto existirem arestas não cobertas:
2. Conta quantas vezes cada vértice aparece nas arestas descobertas.
3. Seleciona o vértice com maior incidência.
4. Adiciona esse vértice à cobertura.
5. Remove todas as arestas cobertas por ele.

Essa estratégia gera uma solução rápida e simples, embora não garanta a cobertura mínima ideal em todos os casos.

---

## Complexidade

- **Tempo:** `O(V · E)`  
- **Espaço:** `O(V + E)`

---

## Exemplo de Grafo Utilizado

Instância 3 (Quadrado com diagonal):

- **Vértices:** {1, 2, 3, 4}  
- **Arestas:** (1,2), (2,3), (3,4), (4,1), (1,3)

---

## Código Disponível

O repositório contém o código do algoritmo guloso organizado em funções compactas e padronizadas em inglês.

---

## Representação Visual

O projeto acompanha imagens ilustrando exemplos de Vertex Cover aplicados ao problema de instalação mínima de câmeras em corredores.

---

## Objetivo

Este material foi produzido para fins didáticos, facilitando a compreensão do problema, da técnica gulosa e de seu comportamento em grafos pequenos e médios.

---

## YouTube

**Apresentação do Algoritmo**: [[[LINK PARA O VIDEO NO YOUTUBE]]
](https://www.youtube.com/watch?v=Y-q6nBVu8O8)
---

**Desenvolvido por**:

* Caio Vasconcelos Silva Andrade  
* Ian Sandes Alves
* José Wilson Martins Filho

**Disciplina**: Projeto e Análise de Algoritmos (PAA)  
**Instituição**: UFS - Universidade Federal de Sergipe
