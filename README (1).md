# Aplikace pro odhad ztráty na výnosu kukuřice

Tato Streamlit aplikace umožňuje odhadnout procentuální ztrátu na výnosu kukuřice na základě:
- data setí,
- data škodlivé události,
- a míry poškození listové plochy (%).

## Funkce
- Vypočítá odhadovanou ztrátu na výnosu podle zadaných údajů.
- Vykreslí graf ztráty na výnosu v čase od 20. dne od setí.
- Zobrazí všechny body křivky s procentuálními hodnotami.
- Vyznačí škodnou událost a její konkrétní výsledek.

## Spuštění

1. Nainstaluj požadované knihovny:

```bash
pip install streamlit scikit-learn matplotlib
```

2. Spusť aplikaci:

```bash
streamlit run app.py
```

## Autor
Vytvořeno pro účely analýzy poškození výnosu kukuřice – červen 2025.
