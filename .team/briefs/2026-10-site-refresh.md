# Brief: transformationbeyond.se — synk mot dignami.com + design review (2026-10)

Ägare: Conny Wadbro. Skriven 2026-10-12 utifrån en jämförelse av transformationbeyond.se (index.html @ ff1b440)
mot dignami.com/en, /assurance, /proof, /about, /products/aos, /contact som de såg ut 2026-10-12.
Läses av PO när raderna i `.team/ORDER.md` skrivs som stories. Allt nedan är beslutat — ompröva inte, fråga bara vid oklarhet.

## Varför

dignami.com har gjorts om (Dignami Assurance som flaggskepp, statusmärkning på varje påstående,
"No certifications we don't hold"). T&B-sidan är från 2026-07-19 och påstår nu saker som systersajten
uttryckligen inte påstår. Två sajter som säljer till samma ledningsgrupp får inte motsäga varandra.

## Fasta beslut

1. **Rollfördelning (från dignami.com/en/about):** "Transformation & Beyond advises; Dignami builds and runs; your counsel gives legal advice."
2. **Erbjudanden:** T&B:s ingång är kvar — *The Architecture Review*, 75 000 SEK ex VAT, fast omfattning, två veckor, Cal.com-bokningen oförändrad.
   Nästa steg efter reviewn är **Dignami Assurance** (Understand · Rethink · Rebuild, med evidence pack). Dignami AOS nämns som Dignamis compliance-plattform, med samma status som Dignami själv anger.
3. **Design:** T&B behåller sin egen identitet (papper/brons, Newsreader + Hanken Grotesk, topografiska band). Ingen omgörning till Dignamis mörka petrol-stil.
   Samordning sker i bevisspråk (statusetiketter, källrader) och i överlämningen till Dignami — inte i palett eller typografi.
4. **Bevisstandard (samma som Dignami):** inga siffror utan källa, inga meriter som inte finns, ingen juridisk rådgivning.

## Innehållsändringar (exakta)

| # | Var i index.html | Nu | Ska bli |
|---|---|---|---|
| C1 | 02 · Law (rad ~271) | "A master's degree in commercial law." | "Master's-level studies in commercial law at Lund University." — **ingen** formulering som antyder magisterexamen |
| C2 | Foundation (rad ~348) | "Master's in commercial law · …" | "Commercial law studies (Lund) · sales leadership in consulting · working AI architect." |
| C3 | 01 · Business | "Two decades in consulting" | "Two decades in IT, consulting and sales leadership" |
| C4 | arc-note (rad ~287) + övriga Dignami-länkar | "Dignami — AI that survives cross-examination ↗" | Dignamis nuvarande budskap: "Dignami — Your AI got faster. Your decisions didn't. ↗", länk till https://www.dignami.com/en |
| C5 | "Read the architecture decisions first →" (rad ~187) | pekar på `#grundaren` | pekar på https://www.dignami.com/en/proof. Påståendet "21 architecture decisions — open for review" får bara stå kvar om det finns en publik URL till besluten; annars "available on request". Hittar Architect ingen publik URL → Operatör-rad till Conny |
| C6 | Mondmodel-raden | "9 destinations · 4 languages · autonomous operations" | samma siffror men med länk till Mondmodels publika sajt som källa (Conny anger URL via Operatör-rad om den inte finns i repot) |
| C7 | Steg 02–04 (How we work) + "Platform"-raden i Who you get | AOS beskrivs som i drift ("The system runs on Dignami AOS — EU-only…", "DIGNAMI · MANAGED") | inga påståenden om drift som Dignami inte själv gör. Använd Dignamis status: AOS-förmågor "built, in demo", "none operates with client records". Statusetiketter i T&B-stil: *Built · In demo · Not in operation* |
| C8 | Law-disciplinen / Advise-steget | — | lägg till en rad: "We read the regulation to shape the design — we don't replace your counsel." |
| C9 | `<html>` | `lang` saknas | `lang="en"` |

## Strukturändring: "How we work"

Ersätt Advise/Build/Run/Operate med en kedja som speglar dignami.com:

1. **Advise — Transformation & Beyond.** The Architecture Review: board-standard answer on where your AI operation stands and what to do next.
2. **Assurance — Dignami.** Understand · Rethink · Rebuild. Every recommendation travels with an evidence pack; every claim has a status.
3. **Platform — Dignami AOS.** Compliance platform for regulated advice, financial advisers first. Status as published on dignami.com/en/proof.

Överlämningen till Dignami blir ett eget tydligt block (inte bara ↗-länkar), som speglar Dignamis sidfot "Advise → Transformation&Beyond".

## Design review (egen story, levererar en rapport — ingen kod)

Leverans: `docs/design-review-2026-10.md` + skärmbilder i `docs/design-review-2026-10/` (desktop 1440 och mobil 390, före ändringar).
Granska mot: T&B:s egen identitet, läsbarhet och hierarki, och samspelet med dignami.com som systersajt. Minst:

- **Kontrast WCAG AA** för alla textfärger mot bakgrund, särskilt `--bronze #8A6430` och `--muted #6B6E72` på `--paper #F7F5F0`, `.book-sub #8F887C`, och 11–12 px mono-texter (`.cta`, `.foot .mono`, `.price span`, `.book-sub`).
- **Scroll-reveal** (`.reveal`/`.r-fade`, 28 element): innehållet är dolt tills IntersectionObserver triggar. Verifiera att allt syns utan JS, med `prefers-reduced-motion: reduce`, i helsidesskärmbild och för sökmotorer/länkförhandsvisning.
- **Mobil 390 px:** hero-rubrikens radbrytning, stegkort, prisblock, sidfot.
- **Fokus/tangentbord:** synliga fokusmarkeringar på alla länkar och CTA.
- **Bevisspråk:** förslag på hur statusetiketter och källrader ser ut i T&B-stil.
- **Överlämningsblocket till Dignami:** skiss eller beskrivning.

Varje fynd: allvarlighetsgrad (Must / Should / Nice), plats, förslag. Conny väljer vilka fynd som byggs i nästa ORDER-rad.

## Utanför scope

- Ny palett, nya typsnitt, ny logotyp.
- Svensk språkversion.
- Ändringar på dignami.com.
- Pris eller bokningsflöde för Architecture Review.

## Källor

- https://www.dignami.com/en, /en/about, /en/assurance, /en/proof, /en/products/aos, /en/contact (läst 2026-10-12)
- https://transformationbeyond.se/ = index.html @ ff1b440
