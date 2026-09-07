# CONVENTIONS.md — conventions datées de ce dépôt

> Règle permanente du corpus : **un mot = un objet**. Ce fichier enregistre les
> conventions attestées *dans ce dépôt*. Le registre de référence du corpus est
> `CONVENTIONS.md` du dépôt `noetic-machine-complete`. Addenda seulement.

## C-KO6 — Tables de signes KO-dimension 6 attestées ici

| ID | Signes | Attestée dans | Statut |
|----|--------|----------------|--------|
| **C-KO6-L1** (2026-08) | J² = +1, JD = +DJ, Jγ = −γJ — table dite « usuelle » (géométrie finie du Modèle standard) | docstring de `src/utils.py`, conventions implicites de `paper/main.tex` | Historique de ce dépôt |
| **C-KO6-A3b** (2026-08-31) | J² = +1, JD = −DJ, Jγ = +γJ | vérificateur A3b du dépôt `noetic-machine-complete` | Table de travail du banc |
| « (J_F γ_F)² = −1 » | docstring de `src/utils.py`, texte gelé du registre F4 | **Coquille mesurée** : incompatible avec J² = +1 et Jγ = +γJ (alors (Jγ)² = +1). Conservée comme artefact daté. | Ne pas utiliser |

**Conséquence** : sous C-KO6-L1, le lemme de parité (Jγ = −γJ, J inversible ⇒ J échange
H⁺/H⁻ ⇒ dim H paire) exclut toute dimension impaire — dont 7. Sous C-KO6-A3b, ce lemme
ne s'applique pas. **Tout énoncé de minimalité doit citer sa table.**

## C-R — Entier R

`dim H_F ≥ 2R+1` (T1) n'est pas évaluable tant que R n'a pas de définition machine.
Définition proposée (note sept. 2026, à valider) : **R = rang du bloc Yukawa P₊ D P₋**.
Statut : OUVERT.

## C-BORNES — Fenêtre d'énumération

Amendement Krajewski / C12.1 : m_ij ≤ 3, k ≤ 3, dim H_F ≤ 24. Les bornes sont des
**paramètres de classe** : elles fabriquent l'espace compté ; tout compte est cité avec
sa fenêtre.

## C-COMPTE — « Bandes »

Trois proxys attestés dans le corpus (`bands_lignes`, `bands_paires`, `bands_entrees` →
max 3 / 6 / 9). Aucun n'est le spectre de D. Le nom du proxy accompagne toujours le
nombre.

---

*Registre ouvert le 2026-09-06. Addenda seulement.*
