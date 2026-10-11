# Arbetsorder

Den här filen är målet. Människan skriver rader under **Kö**; PO tar dem i ordning, en i taget,
när ingen story är i arbete, och skriver varje rad som en story i `.team/backlog/`.

Regler:
- En rad = en story = en PR. Är raden för stor delar PO den i flera stories och bockar raden när alla är skrivna.
- PO bockar raden (`- [x]`) och skriver story-ID:t sist på raden.
- Oklar rad: PO frågar människan i sin ruta och går vidare med nästa rad som är klar.
- Beroenden: skriv `(efter NNN)` på raden; PO parkerar storyn som `_NNN-slug.md` med raden `parked-until: NNN` tills NNN är mergad.
- En rad som ändrar regelboken (AGENTS.md, .team/team.md, REVIEW.md, .team/roles/) säger det uttryckligen.

## Kö

Underlag för alla rader: `.team/briefs/2026-10-site-refresh.md` (beslutat — läs det först).

- [x] Rätta faktapåståenden på sidan: C1, C2, C3, C8 och C9 i briefen (examen, "two decades", juridisk avgränsning, `lang`). Liten PR, går först. 001
- [ ] Synka Dignami-referenser och bevis: C4, C5, C6 och C7 i briefen (ny Dignami-slogan, länk till /en/proof, källa för Mondmodel, AOS-status utan driftpåståenden).
- [ ] Byt "How we work" mot kedjan Advise → Assurance → Platform och lägg till ett tydligt överlämningsblock till Dignami enligt briefen, avsnitt "Strukturändring". (efter rad 2)
- [ ] Design review enligt briefen, avsnitt "Design review": rapport + skärmbilder i `docs/`, ingen kodändring. Görs mot sidan före rad 3:s ändringar om rad 3 inte är mergad, annars mot den mergade sidan.

## Väntar på människan

- [ ] Bygg de design review-fynd Conny väljer (skrivs som ny Kö-rad när rapporten är läst).

## Operatör

PO skriver hit när en mergad PR kräver något bara människan får göra (hemlighet, driftsättning, migrering,
infrastruktur, spend, beslut). Människan tar bort raden när det är gjort.
