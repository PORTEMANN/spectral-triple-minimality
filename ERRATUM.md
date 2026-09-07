# ERRATUM — daté 2026-09-06

> Politique du corpus : corrections en **addendum**, versions conservées. Le code et les
> données incriminés restent en place, gelés, comme artefacts historiques ; le présent
> erratum fait foi. Référence d'audit : dépôt `noetic-machine-complete`
> (`src/a3_ko6_reenumeration.py`, `data/a3_ko6_reenumeration_verdict.json`).

## E1 — « 63 160 réalisations certifiées » : réfuté comme publié

Le compte du théorème T3 (README, `paper/main.tex`) n'est **pas reproductible** :

- **D1** — plafond codé en dur dans `src/enumeration.py`
  (`if len(solutions) >= 63160: break  # safety cap`, et `assert len(solutions) == 63160`
  en mode `--verify`) : le nombre est une **entrée** du programme, pas une sortie ;
- **D2** — les « axiomes KO-6 » de `src/utils.py` sont des **proxys**
  (`k % 2 == 0 and dim_hf >= 2*k + 1`) : aucun J, γ, D matriciel n'est construit ;
- **D3** — `src/certification.py` : `certify()` calcule un hash et un horodatage puis
  `return True` **inconditionnellement** : la « certification » est vide.

Relance sous la logique publiée, plafond supprimé : **0 solution** (4 067 matrices
admissibles). `data/results/enumeration_log.json` (1260 + 3840 + 58260 = 63 160) est
ajusté à la cible ; `solutions_63160.json` ne contient que 3 échantillons ; le checksum
du papier (« 7818d566...750ec ») est tronqué et invérifiable ; le log annonce
« candidates_screened: 15625 » en k = 3 là où l'espace réel mesuré (A3b) est
4 723 712 matrices, sur un « enumeration-cluster-01 » là où le README annonce « ~hours
on standard hardware ».

**Verdict (A3, B3-FAIL du corpus) : RÉFUTÉ COMME PUBLIÉ — le nombre 63 160 n'est ni une
sortie du code, ni un invariant de définition : c'est un artefact.**

## E2 — « Sept bandes » : cible structurellement inatteignable

Le filtre du code compte les **lignes non vides** de m (bornées par k ≤ 3). Tamis A3 :

| Proxy | Max atteignable | Compte sous cible 7 |
|---|---|---|
| `bands_lignes` | 3 | 0 |
| `bands_paires` | 6 | 0 |
| `bands_entrees` | 9 | 7 200 |

Aucun de ces proxys n'est le spectre de D. L'énoncé « seven spectral bands E₁,…,E₇ »
(`main.tex`, T3) n'a pas d'objet machine associé dans ce dépôt.

## E3 — Convention KO-6 : coquille

La docstring de `src/utils.py` énonce « (J_F γ_F)² = −1 » avec JD = +DJ. Le vérificateur
A3b (dépôt `noetic-machine-complete`) gèle J² = +1, Jγ = +γJ, JD = −DJ et mesure
l'incompatibilité : sous J² = +1 et Jγ = +γJ, (Jγ)² = +1. Voir `CONVENTIONS.md` de ce
dépôt et du corpus. **Le statut du « 7 » dépend de la table** : sous Jγ = −γJ (table L1),
le lemme de parité (J inversible échange H⁺/H⁻ ⇒ dim H paire) exclut toute dimension
impaire ; sous la table A3b, il ne s'applique pas.

## E4 — Statut ligne par ligne des énoncés

| Énoncé | Statut au 2026-09-06 |
|---|---|
| **T1** (dim H_F ≥ 2R+1) | **Non évaluable** : R n'a pas de définition machine dans L1 (définition proposée : rang de P₊ D P₋ — à geler dans CONVENTIONS.md) |
| **T2** (R = 3 ⇒ dim ≥ 7, k ≥ 2, max m_ij ≥ 3) | **Convention-dépendant** ; seuls k ≥ 2 et l'obstruction arithmétique « marge 3 » survivent comme faits d'arithmétique des multiplicités |
| **T3** (63 160 réalisations certifiées) | **Réfuté comme publié** (E1, E2) |
| **T4** (M_min(R) = sqf(R)) | **Fait d'arithmétique** (dont 2+2+3 = 7) ; ne constitue pas à lui seul un théorème de géométrie spectrale |

## Ce qui reste valide et opérationnel

- Le triplet minimal **C4** construit et vérifié matriciellement : A_F = ℂ ⊕ ℂ,
  H_F = ℂ⁴, γ = diag(1, 1, −1, −1), J₀ réelle J₀² = +1, D réel symétrique anticommutant
  (A3b, 4/4 — dépôt `noetic-machine-complete`) ;
- la fenêtre **F4** : 60/256 matrices sous vrais axiomes en k = 2, dim = 5 (verdict 3/3) ;
- la question ouverte honnête : *sous une table de signes datée, existe-t-il (D, J, γ) de
  taille impaire vérifiant l'ordre 1 avec un scalaire ?* Si oui, on publie les trois
  matrices. Si non, le 7 sort du tiroir thèse.

## Conséquences éditoriales

- Le badge « arXiv — à soumettre » et la mention « arXiv-ready » sont suspendus jusqu'à
  réécriture de T3 (retrait du compte certifié ou remplacement par un résultat
  machine-vérifiable).
- `src/enumeration.py`, `src/certification.py`, `src/utils.py` et `data/results/` sont
  **gelés comme artefacts historiques** (politique « conserver les versions »). Toute
  version corrigée sera un fichier nouveau, daté, avec protocole pré-enregistré.

---

*Erratum ouvert le 2026-09-06, en réponse à la note de lecture « Incohérences internes du
corpus Portemann » (sept. 2026) et à l'audit A3 du corpus. Addenda seulement.*
