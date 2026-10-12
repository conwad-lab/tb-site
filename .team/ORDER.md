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

- **merge: auto bekräftad av Conny 2026-10-12** för hela arbetsordern, även design review-raderna och C6.

Underlag för alla rader: `.team/briefs/2026-10-site-refresh.md` (beslutat — läs det först).

- [x] Rätta faktapåståenden på sidan: C1, C2, C3, C8 och C9 i briefen (examen, "two decades", juridisk avgränsning, `lang`). Liten PR, går först. 001
- [x] Synka Dignami-referenser och bevis: C4, C5, C6 och C7 i briefen (ny Dignami-slogan, länk till /en/proof, källa för Mondmodel, AOS-status utan driftpåståenden). 002
- [x] Byt "How we work" mot kedjan Advise → Assurance → Platform och lägg till ett tydligt överlämningsblock till Dignami enligt briefen, avsnitt "Strukturändring". (efter rad 2) 003
- [x] Design review enligt briefen, avsnitt "Design review": rapport + skärmbilder i `docs/`, ingen kodändring. Görs mot sidan före rad 3:s ändringar om rad 3 inte är mergad, annars mot den mergade sidan. 004

- [x] Bygg design review-fynden D1–D8 enligt beslutslistan i `docs/design-review-2026-10.md`. D9 tas inte. Inom nuvarande identitet (palett, typsnitt, layout). Dela i flera stories om det behövs, D1 först. 005, 007, 008, 009
- [x] C6: stryk "autonomous operations" i Mondmodel-raden — går inte att belägga på mondmodel.com. "9 destinations · 4 languages" med källänk står kvar. 006

## Väntar på människan

Beslut 2026-10-12 (Conny): C5 — "available on request" står kvar, ingen publik URL. C6 och design review — se Kö.

## Operatör

PO skriver hit när en mergad PR kräver något bara människan får göra (hemlighet, driftsättning, migrering,
infrastruktur, spend, beslut). Människan tar bort raden när det är gjort.

- [ ] PR #1 (story 001, faktarättelser) är mergad och ligger live — kontrollera https://transformationbeyond.se/ (examen, "two decades", Law-raden, `lang="en"`).
- [ ] PR #2 (story 002, Dignami-synk) är mergad och ligger live — kontrollera https://transformationbeyond.se/ (ny Dignami-slogan, "Examine the proof first" → /en/proof, statusetiketten "Built · In demo · Not in operation" i steg 03 och Platform-raden, källänk mondmodel.com).
- [ ] PR #3 (story 003, Advise → Assurance → Platform + överlämningsblock) är mergad och ligger live — kontrollera https://transformationbeyond.se/ (tre kort i "How we work", blocket "Hand-off → Dignami", sidfotens "Assurance & Platform → Dignami").
- [ ] PR #5 (story 005, D1 reveal-fallback) är mergad och ligger live — kontrollera https://transformationbeyond.se/ (allt innehåll syns utan att scrolla, t.ex. i en länkförhandsvisning; scroll-animationen spelar fortfarande).
- [ ] PR #6 (story 006, C6) är mergad och ligger live — kontrollera https://transformationbeyond.se/ (Mondmodel-raden: "9 destinations · 4 languages · source: mondmodel.com", inget "autonomous operations").
- [ ] **Merga PR #7** (story 007, D2 + D3 kontrast + fokusring). Reviewern godkände 2026-10-12 men kunde inte merga trots `merge: auto` ("merge blocked by session permissions", `.team/reviews/007-contrast-and-focus.md` på grenen `feat/007-contrast-margin-and-focus-ring`). PR:en är mergeable/clean. Story 008 väntar på den.
